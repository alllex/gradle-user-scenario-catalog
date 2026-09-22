#!/usr/bin/env python3
"""Checker for the user scenario catalog: catches what a refactor silently
breaks — the repo left plausible but wrong — and runs the scenarios.

    ./test.py            the checks, then every scenario through gust
    ./test.py --quick    the checks only
"""

import re, subprocess, sys, tomllib
from pathlib import Path

ROOT = Path(__file__).parent
# Directory names that never hold scenarios, at any depth: tooling, and the
# template projects scenarios lay out from.
SKIP = {".git", ".gust", "_topic", "templates"}
MD_LINK = re.compile(r"\]\((?!\w+:)([^)#]+\.md)\)")  # relative .md links only

failed: list[str] = []


def check(description, problems):
    """One check; an empty problem list is a pass. Detail lines are printed
    but not tallied: the count is of failed checks, not of output lines."""
    print(f"{'FAIL' if problems else 'pass'}  {description}")
    for problem in problems:
        print(f"        {problem}")
    if problems:
        failed.append(description)


def rel(path):
    return str(path.relative_to(ROOT))


def catalog_files(suffix):
    """Scenario files anywhere below the root, at any depth: no group or family
    directory is named here, so a new one is picked up without a change. Skipped
    are the SKIP directories and READMEs, and anything at the root itself."""
    return sorted(p for p in ROOT.rglob(f"*{suffix}")
                  if p.stem != "README" and p.parent != ROOT
                  and not SKIP.intersection(q.name for q in p.parents))


def check_pairs():
    problems = [f"{rel(t)} has no matching {t.stem}.md"
                for t in catalog_files(".toml")
                if not t.with_suffix(".md").is_file()]
    problems += [f"{rel(m)} has no matching {m.stem}.toml"
                 for m in catalog_files(".md")
                 if not m.with_suffix(".toml").is_file()]
    check("every scenario .toml has a matching .md, and the reverse", problems)


def check_names(tomls):
    problems = []
    for path in tomls:
        try:
            name = tomllib.loads(path.read_text()).get("name", "<absent>")
        except tomllib.TOMLDecodeError as exc:
            problems.append(f"{rel(path)}: unparseable: {exc}")
        else:
            if name != path.stem:
                problems.append(f'{rel(path)}: name = "{name}", expected "{path.stem}"')
    check("every scenario .toml's name matches its filename stem", problems)


def check_links():
    problems = []
    for md in sorted(ROOT.glob("**/*.md")):
        if any(p.name in SKIP or p.name.endswith(".out") for p in md.parents):
            continue
        for lineno, line in enumerate(md.read_text().splitlines(), 1):
            problems += [f"{rel(md)}:{lineno}: dead link to {t}"
                         for t in MD_LINK.findall(line)
                         if not (md.parent / t).is_file()]
    check("no dead relative .md links", problems)


def run_scenarios(tomls):
    """--tmp keeps gust's output in /tmp, so no .out/ lands in the repo."""
    for path in tomls:
        done = subprocess.run(["gust", "run", rel(path), "--tmp"], cwd=ROOT,
                              capture_output=True, text=True)
        tail = [] if done.returncode == 0 else \
            (done.stdout + done.stderr).strip().splitlines()[-20:]
        suffix = "" if done.returncode == 0 else f" (exit {done.returncode})"
        check(f"gust run {rel(path)}{suffix}", tail)


def main():
    quick = "--quick" in sys.argv[1:]
    if sys.argv[1:] and not quick:
        sys.exit(f"usage: {sys.argv[0]} [--quick]")
    if not (tomls := catalog_files(".toml")):
        sys.exit(f"error: no scenarios found under {ROOT}")

    print(f"Scenarios found: {len(tomls)}")
    print(*(f"  {rel(p)}" for p in tomls), sep="\n", end="\n\n")

    check_pairs()
    check_names(tomls)
    check_links()
    if quick:
        print("\n(scenario runs skipped: --quick)")
    else:
        print()
        run_scenarios(tomls)

    if not failed:
        print("\nall checks passed")
        return 0
    print(f"\n{len(failed)} check(s) failed:")
    for description in failed:
        print(f"  {description}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
