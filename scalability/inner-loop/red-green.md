# Red to green

**Watch a test fail, fix the test, watch it pass.**

## What happens

I run a test in the module I am working in and it fails: the expectation in the
test is wrong. I open the test, correct the expectation, and run the same
command again. It passes.

Between the two runs I changed one test source file. I touched nothing about how
the build is defined.

## Why it matters at scale

This loop runs many times a day, so its cost is paid per iteration rather than
once.

The question is how much of the build reacts to an edit confined to one module's
test sources. Nothing depends on a test source, so the work between the failing
run and the passing run has a floor: recompile the tests of one module, run
them. Anything above that floor is work the edit did not make necessary.

*Fix the production code* covers the same loop with the edit in a main source,
which other modules consume.

## The scenario

`red-green.toml` — three steps: a run that fails, an edit to the test source,
a run that passes.

```bash
gradle :lib1:test --tests 'lib1.GreetingTest'     # fails: 1 of 3
# correct the expectation in GreetingTest.java
gradle :lib1:test --tests 'lib1.GreetingTest'     # passes
```

The first run fails one test of three: a wrong expectation in one test method.
