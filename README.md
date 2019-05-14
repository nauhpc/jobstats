# Jobstats

## Overview 
Provides a toolkit of scripts to easily view and pipe data on a user or account's resource usage data from Slurm's `sacct` tool.

## Installation

### Requirements
1. Python 3.5+ 
2. Slurm toolkit

### Install

#### PyPi
```
pip install jobstats
```

#### Manual
```
git clone https://github.com/nauhpc/jobstats.git
cd jobstats
python3 setup.py install
```

#### Extremely manual
1. Clone and enter repository `git clone https://github.com/nauhpc/jobstats.git`
2. Add `jobstats` and `group_efficiency` to your PATH

## Configuration
All config values for `jobstats` are accessed from `jobstats-config.ini`. These two files should always be in the same directory.

* `*_WEIGHT`: Weight each value holds in calculating the average total efficiency.
* `SHOW_JOB_CHILDREN`: Show each job along with the child jobs from each `srun` command in the batch script. Leaving this off will give you the sum total for each resource for the overall job.
* `COLUMN_MAX`: Max width of the presented table. Setting to `auto` will set the max width to the terminal size on call.
* `GRADE_INCREMENT_*`: Grade scale from red, to yellow, to green for each value.
