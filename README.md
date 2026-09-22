# User scenario catalog

A catalog of things people do with Gradle.

A scenario is a stretch of work with a beginning and an end: what someone is
trying to get done, and the steps they take to get there. It says what they do,
not how Gradle handles it.

## Layout

```
scalability/
  templates/     the toy project the scenarios are laid out from
  inner-loop/    one .md and one .toml per scenario
```

Each scenario is a pair: a `.md` describing it, beside a `.toml` that
[Gust](https://github.com/alllex/gust) runs.

## Toy projects, large-project scenarios

The project in `templates/` is small: three projects and a build-logic included
build, a handful of tests. Each scenario is formulated for a very large build,
where the module being worked in is one of hundreds, and exercised here on a toy
one.

## Running one

With [Gust](https://github.com/alllex/gust) on PATH, from the repository root:

```bash
gust run scalability/inner-loop/narrow-test.toml \
  --tmp --show-output -- --configuration-cache
```

`--show-output` echoes each run's Gradle output as it happens, and everything
after `--` is appended to every Gradle command, so the scenario runs with the
configuration cache on.

`gust check <scenario>` validates one without running it.
