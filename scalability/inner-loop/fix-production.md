# Fix the production code

**Watch the tests fail, fix the code under test, watch them pass.**

## What happens

I run the tests in the module I am working in and they fail — not because the
tests are wrong, but because the code they exercise is. I open the main source,
correct it, and run the same command again. They pass.

Between the two runs I changed one main source file. I touched nothing about how
the build is defined.

## Why it matters at scale

To the user this is an edit-and-rerun loop like *Red to green*, but the edit
lands in a main source rather than a test.

A test source has nothing downstream of it. A main source has everything that
depends on it: the module's own tests, every other module that consumes it, and
their tests in turn. So an edit here has a reason to reach further than an edit
to a test, and the question is how much further it reaches, and whether that
matches what the code requires.

The user's request is narrow — one module's tests — while the edit is to a
source that other modules consume.

## The scenario

`fix-production.toml` — three steps: a run that fails, an edit to the main
source, a run that passes.

```bash
gradle :lib1:test --tests 'lib1.GreetingTest'     # fails: 3 of 3
# correct Greeting.hello in Greeting.java
gradle :lib1:test --tests 'lib1.GreetingTest'     # passes
```

The first run fails all three tests: one defect in the code under test, every
test that exercises it red.
