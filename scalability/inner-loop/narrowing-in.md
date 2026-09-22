# Narrowing in

**Run the whole test class, then run the one test.**

## What happens

I am working in one module of a large build. I have a test class open, and I run
all of it to see where I stand. It is green. Then I narrow to the single test I
am iterating on, and I run it again. It is green too.

Between the two runs I touched nothing. No build script, no convention plugin,
no version catalog, no property. I asked a narrower question.

## Why it matters at scale

The second run does strictly less work than the first: one test method instead
of the whole class, in the same module, in the same build. A user reading these
two commands expects the second to be the cheaper of the two, and to get cheaper
still the more they narrow.

The narrowing is expressed in the request rather than in the project. Nothing
about the build definition distinguishes the second invocation from the first,
so any cost the second run pays beyond running one test method is cost the user
did not ask for. On a build with hundreds of projects, that cost is the
difference between a loop that feels immediate and one that does not.

## The scenario

`narrowing-in.toml` — two runs, both expected to pass.

```bash
gradle :lib1:test --tests 'lib1.GreetingTest'
gradle :lib1:test --tests 'lib1.GreetingTest.capitalizes'
```
