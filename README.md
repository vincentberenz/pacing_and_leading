# pacing_and_leading

## Installation

```
pip3 install pacing_and_leading
```

## Usage

```
# will run for 4 minutes
pacing_and_leading
```

```
# will run for 10 seconds
pacing_and_leading 10
```

```
# will show similarity scores during runtime
pacing_and_leading console
```

```
# will show hard and soft targets
pacing_and_leading show
```

```
# will run for 10 seconds, display the similarity scores
# and show the soft and hard target
pacing_and_leading show console 15
```

When the duration is passed, the main window will freeze and ugly error messages will be displayed. This should be corrected.
When the main window is closed, a file "pacing_and_leading.save" is written in the current directory.

The following :
```
pacing_and_leading_simlog
```
will parse the "pacing_and_leading.save" file that is in the current directory and plot similarity score vs time.

