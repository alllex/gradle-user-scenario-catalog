# Does it compile?

**A test run stops at a compilation error; fix it and compile, without running
the tests yet.**

## What happens

I run the tests in the module I am working in. They do not run at all: the main
source does not compile, because I misspelled a method name. I correct the
spelling, and now I want the quickest confirmation that the code is valid again,
so I compile that module and nothing else. The tests can wait until I am ready
for them.

Between the two runs I changed one main source file. I touched nothing about how
the build is defined.

## Why it matters at scale

The first run never reaches what I asked for. Before the compiler rejects one
method call, the build is configured, dependencies are resolved, and everything
`lib1` is built from is built. All of that is spent to arrive at an error that
compiling one module would have surfaced.

So the cost of the failed run is set by how much happens before the first thing
that can fail. On a build with hundreds of projects, a typo caught at the
compiler is paid for at the price of the whole request.

The second run is the narrow question, asked on purpose: compile this module,
nothing else. The tests are not skipped by accident — they are not wanted yet.

## The scenario

`does-it-compile.toml` — three steps: a run that fails to compile, an edit to
the main source, a compile that succeeds.

```bash
gradle :lib1:test --tests 'lib1.GreetingTest'     # fails: cannot find symbol
# correct the misspelled call in Greeting.java
gradle :lib1:compileJava                          # passes
```

The first run fails at `:lib1:compileJava`; the test task is never reached.
