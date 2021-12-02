# Jobstats

## Overview 
Provides a toolkit of scripts to easily view and pipe data on a user or account's resource usage data from Slurm's `sacct` tool.

## Usage
```
Usage:  jobstats [JOBID] [OPTIONS...]
Show usage statistics for past slurm jobs

  JOBID                a comma-separated list of jobids
  -A                   run jobstats on an entire account
  -S                   show jobs since start date (format m/d/yy)
  -r, --show-running   show running jobs
  -p, --parsable       make output parseable
  -c, --no-color       do not print colored stats
  -s, --no-size-limit  ignore dynamic terminal size limits
  -G, --gpu-stats      show gpu hours and gpu efficiency
  All other arguments in 'sacct' are accepted

Got bugs? Report to hpcsupport@nau.edu
```

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
* `TRACK_SINGLE_CORE_JOBS`: Include single core jobs when calculating CPU efficiency
