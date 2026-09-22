# Narrow to one project

**A broad check fails; rerun it for one subproject to read the failure, fix it,
and rerun the narrow check. Same check, fewer projects.**

## What happens

I run the quality check across the build. It fails, and the failure is one
finding among everything else the run reported. I run the same check again for
the subproject I believe it came from, so that this time the finding is the only
thing on screen: it tells me the file, the line, and the rule. I fix it, and run
that same narrow check to confirm.

The second run tells me nothing I could not have read in the first. I run it to
get an answer I can read, and because it is the command I am going to keep
running while I fix this.

Between the runs I changed one main source file, and only its formatting. I
touched nothing about how the build is defined.

## Why it matters at scale

The first run checks every project. The second checks one, and everything after
it is the narrow one, because that is the loop until the finding is gone.

So the cost that matters is the second run and every repeat of it. Nothing about
the build changed between the broad run and the narrow one, and the narrow run
asks for a fraction of the work — one project's quality check, no tests, no
other project. On a build with hundreds of projects, the difference between
paying for that fraction and paying for the whole request is the difference
between a check worth rerunning and one worth avoiding.

The edit changes only formatting: no behaviour changes, no other project can
observe it, and the tests are not involved at any point.

## The scenario

`narrow-sanitycheck.toml` — four steps: a broad check that fails, a narrow
check that fails, an edit to the main source, a narrow check that passes.

```bash
gradle sanityCheck          # fails: a line over 100 columns, in lib1
gradle :lib1:sanityCheck    # fails the same way, on its own
# wrap the long line in Greeting.java
gradle :lib1:sanityCheck    # passes
```

`sanityCheck` runs Checkstyle across the build without running any tests. Both
failing runs report the same violation; the narrow one reports about half as
many task lines around it.
