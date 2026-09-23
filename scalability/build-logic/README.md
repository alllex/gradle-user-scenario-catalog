# Build logic

Scenarios where the user edits the build's own definition. In each one the edit
is confined to a single project's build script, and the sources, the convention
plugins, and the version catalog are as they were.

These are the changes people make while working in a module rather than on the
build: reaching for a library, picking up the shared setup, turning something
on.

| Shorthand | The edit |
|---|---|
| [Add a dependency](add-dependency.md) | a library the module needs |
| [Adopt the conventions](adopt-conventions.md) | the shared convention plugin |
| [Adjust the test task](adjust-test-task.md) | a setting for a task the module has |

The three are ordered by how much arrives with the edit: a library, then a whole
shared setup, then one setting on a task that was already there.
