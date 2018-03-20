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

* Your Gitlab host (`--hostname=https://gitlab.com`);
* Your Gitlab API private token, so that it can connect to the correct place (`--token=asdf123`;
* (optional) the maximum age of branches, in days, before they should be pruned (`--maxage=90`).

You'll see a list of branches to be pruned and be asked for confirmation before pruning takes place.

### Default host and age

The below command would use `https://gitlab.com` as the host and `90` as the age. Branches older than 90 days would be pruned.

```
python app.py --token=asdf123
```

### Default age only

```
python app.py --token=asdf123 --hostname=https://gitlab.mycompany.com
```

### No defaults

```
python app.py --token=asdf123 --hostname=https://gitlab.mycompany.com --maxage=60
```

## Contributions

Any improvements, please fork and submit an MR!
