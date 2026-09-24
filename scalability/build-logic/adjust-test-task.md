# Adjust the test task

**The tests need a setting nothing passes them. Adjust the task that runs them
and they pass.**

## What happens

My module's tests need to know which locale to expect, and they read it from a
setting passed in when they run. Nothing passes it, so they fail. I open my
module's build script, hand the setting to its test task, and run them again.
They pass.

I changed one build script, and one line of it. No dependency changed, no
plugin was applied, no shared build logic moved, and the tests themselves are
as they were. The module my module is built on is untouched.

## Why it matters at scale

This is a small kind of build-script change: one call adjusting a task the
module already has, and already runs. Nothing about what the module depends on
changed, and nothing about what it compiles changed.

The module is not alone, though. It is built on another one, and running its
tests means that other module's classes have to be there. None of that is
affected by the edit: what the module below produces, and everything the build
knows about how to produce it, is the same before and after.

So the second run has little to work out that it did not already know a moment
earlier — for this module, and for the one it stands on. On a build with
hundreds of modules, the gap between how small the change is and what it costs
to absorb is the thing to watch, and it widens with every module that the edit
left exactly as it was.

## The scenario

`adjust-test-task.toml` — three steps: a test run that fails, an edit to
the build script, a test run that passes.

```bash
gradle :lib2:test --tests 'lib2.ShoutTest'   # fails: 2 of 2
# add tasks.test { systemProperty(...) } to lib2/build.gradle.kts
gradle :lib2:test --tests 'lib2.ShoutTest'   # passes
```

The setting is a system property the tests read. Both read it, so both fail
without it and both pass once the test task supplies it. `lib2` is built on
`lib1`, so both runs need `lib1`'s classes; the edit changes nothing about
them.