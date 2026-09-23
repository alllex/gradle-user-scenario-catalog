# Adopt the conventions

**A subproject is missing the build's shared setup. Apply the convention plugin
and its tests run.**

## What happens

One module in the build has not adopted the conventions the others use. Its
tests do not even compile: the test framework the rest of the build takes for
granted is not on its classpath. I open its build script, replace the bare Java
plugin with the shared convention plugin, and run its tests. They run.

I changed one build script, and one line of it. The convention plugin itself is
untouched — I applied what was already there.

## Why it matters at scale

The edit is one line, and what arrives with it is not: a test framework,
quality checks, and whatever else the conventions carry. The module goes from
configured by itself to configured like its neighbours.

That asymmetry is what makes this worth watching. The user's change is small
and local, and its consequence for this module is large — but it is still a
consequence for *this* module. Every other module applies the same plugin and
applied it before the edit; none of them changed. On a build where hundreds of
modules share one convention plugin, the question is whether applying it
somewhere new is priced like the local edit it is.

## The scenario

`adopt-conventions.toml` — three steps: a test run that fails, an edit to the
build script, a test run that passes.

```bash
gradle :lib3:test    # fails: package org.junit.jupiter.api does not exist
# apply java-conventions in lib3/build.gradle.kts
gradle :lib3:test    # passes: 2 tests
```

The tests were there all along; what the edit supplies is what they need to
compile and run.