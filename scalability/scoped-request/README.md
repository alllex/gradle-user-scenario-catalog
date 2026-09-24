# Scoped request

Scenarios where someone wants one part of a large build and nothing came
before: no warm state to reuse, no previous run to compare against. A single
invocation, on a machine that may never have built this project.

Each asks the same question from a different angle: how far does the cost of a
request reach beyond what the request named.

| Shorthand | The request |
|---|---|
| [Does their module build?](build-one-module.md) | build the one module a branch touched |
| [A guard on one module](module-guard.md) | run one module's own check, as a job |

The first names a module and asks for something every module can do. The second
asks for a check that exists in one place and reads only that module's files.

Both arrive from a person and from continuous integration alike: a reviewer
wanting an answer before they read a diff, and a job that runs one check on
every change, from cold, forever.
