# A guard on one module

**A check that reads one module's files, run as its own job on every change.**

## What happens

My team owns one module, and its translations keep getting broken by people
editing the properties files by hand. So we wrote a check for it: it reads those
files and complains if a key has gone missing. Now I want it to run on every
change, as its own job, so a broken translation is caught before anyone reviews
the change.

The job does nothing else. It starts on a clean machine, runs that one check,
and reports. Nothing here is warm, and nothing it does is wanted by any other
module.

## Why it matters at scale

Reading a few properties files takes no time at all. Everything this job spends
is spent getting to the point where it can read them, and none of that work is
about translations.

The check is as self-contained as work gets: it reads files in one module and
writes nothing any other module could want — not a dependency, not a consumer,
not a shared output. So there is no reading of this request under which another
module's build script has anything to contribute to the answer.

That is what makes the job worth watching rather than merely slow. It runs on
every change, from cold, forever. On a build with hundreds of modules, a team
that wanted a cheap guard against broken translations instead gets one priced
like a build, and the obvious next move is to stop running it.

## The scenario

`module-guard.toml` — one run, expected to pass.

```bash
gradle :lib1:checkResources
```

`checkResources` belongs to `lib1` alone: it reads `lib1`'s resources and
prints that they are in order.
