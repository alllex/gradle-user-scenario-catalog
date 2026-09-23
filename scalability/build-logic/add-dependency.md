# Add a dependency

**Code in a subproject needs a library it does not have. Add it and compile.**

## What happens

I am writing code in one module and I reach for a library: I import it and call
it. It does not compile, because this module does not depend on that library
yet. I open the module's build script, add the dependency, and compile again.
It compiles.

I changed one build script, and one line of it. Every other project's build
script, the convention plugins, and the version catalog are as they were.

## Why it matters at scale

The dependency is declared in one module's build script and the entry it refers
to already exists in the version catalog. Nothing about any other module
changed, and nothing about how the build is put together changed.

So the second run has one new thing to work out: this module now resolves one
more library. Whatever the build knew about the other modules a moment ago is
still true. On a build with hundreds of modules, the question is how much of
that knowledge survives an edit confined to a single build script, because
adding a dependency is among the most common reasons to open one.

## The scenario

`add-dependency.toml` — three steps: a compile that fails, an edit to the
build script, a compile that passes.

```bash
gradle :lib2:compileJava    # fails: commons.lang3 does not exist
# add commons-lang3 to lib2/build.gradle.kts
gradle :lib2:compileJava    # passes
```

The library is already in the version catalog; what the edit adds is this
module's use of it.