# Adjust the test task

**The tests need a setting nothing passes them. Adjust the task that runs them
and they pass.**

## What happens

The tests in the module I am working in read a setting from the environment
they run in. Nothing sets it, so they fail. I open the module's build script,
pass the setting to its test task, and run them again. They pass.

I changed one build script, and one line of it. No dependency changed, no
plugin was applied, no shared build logic moved, and the tests themselves are
as they were.

## Why it matters at scale

This is a small kind of build-script change: one call adjusting a task the
module already has, and already runs. Nothing about what the module depends on
changed, nothing about what it compiles changed, and no other module is
involved.

What did change is how one task runs, in one project. So the second run has
little to work out that it did not already know a moment earlier. On a build
with hundreds of modules, that gap — between how small the change is and what
it costs to absorb — is the thing to watch, and this scenario keeps the change
about as small as a build-script edit gets.

## The scenario

`adjust-test-task.toml` — three steps: a test run that fails, an edit to
the build script, a test run that passes.

```bash
gradle :lib1:test --tests 'lib1.GreetingTest'   # fails: 2 of 2
# add tasks.test { systemProperty(...) } to lib1/build.gradle.kts
gradle :lib1:test --tests 'lib1.GreetingTest'   # passes
```

The setting is a system property the tests read. Both read it, so both fail
without it and both pass once the test task supplies it.