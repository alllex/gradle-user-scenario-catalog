# Inner loop

Scenarios where the build logic is untouched. Between one invocation and the
next, nothing changes about how the build is defined: no build script, no
convention plugin, no version catalog, no property. What changes is the request,
or the sources being worked on.

The cost of each is paid on every iteration.

| Shorthand | What changes |
|---|---|
| [Narrow to one test](narrow-test.md) | the request |
| [Red to green](red-green.md) | a test source |
| [Fix the production code](fix-production.md) | a main source |
| [Does it compile?](does-it-compile.md) | a main source, and the request |
| [Narrow to one project](narrow-sanitycheck.md) | a main source, and the request |

*Red to green* and *Fix the production code* are close relatives: the same loop,
with the edit in a test source or in a main source.

*Narrow to one test* and *Narrow to one project* both ask a narrower question
than the run before, along different axes: fewer tests within a project, or
fewer projects within the build.
