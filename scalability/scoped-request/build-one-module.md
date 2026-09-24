# Does their module build?

**Someone else's changes are in one module. Build that module, not the
repository.**

## What happens

I have just pulled a colleague's branch to review it. Their changes are in one
module, and before I read any of it I want to know the thing builds at all. I
am not going to wait for the whole repository to compile to find that out, and
I do not want its tests yet — I want the one module they touched, and then I
want to start reading.

This is the first thing I have run since pulling. Nothing here is warm.

## Why it matters at scale

Naming the module is the plainest way anyone has of saying "only this part of
the build". It is what people reach for the moment a repository is big enough
that building all of it is not worth the wait — and on a build that size, the
wait is the entire reason they are being specific.

What the answer needs is that module and whatever it is built from. Not the
modules that depend on it: they are unaffected by whether this one compiles.
Not the ones unrelated to it in either direction.

So the question is how closely the cost follows the request. If naming one
module out of hundreds costs about what naming all of them would, then being
specific bought nothing, and the reviewer who wanted a quick answer before
reading a diff waits anyway — or gives up asking and reads the diff blind.

## The scenario

`build-one-module.toml` — one run, expected to pass.

```bash
gradle :lib1:compileJava
```

Nothing is edited and nothing fails. The scenario is the request, and how far
its cost reaches past the module it names.
