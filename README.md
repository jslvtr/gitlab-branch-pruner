# Gitlab Branch Pruner

## Installation

### Requirements

* Python3.6+
* Pipenv

### Setup

Clone the repository or download as a .ZIP.

```
git clone https://github.com/jslvtr/gitlab-branch-pruner.git
```

Then, install dependencies and create virtualenv using Pipenv:

```
cd gitlab-branch-pruner
pipenv install
```


## Usage

The script takes two command-line arguments:

* Your Gitlab host;
* Your Gitlab API private token, so that it can connect to the correct place;
* (optional) the maximum age of branches, in days, before they should be pruned.

You'll see a list of branches to be pruned and be asked for confirmation before pruning takes place.

## Contributions

Any improvements, please fork and submit an MR!
