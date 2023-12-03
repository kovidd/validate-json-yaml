# Steps for using act

## Install gh cli
Windows

    winget install --id GitHub.cli

Mac

    brew install gh

## Install docker
[Mac](https://docs.docker.com/desktop/install/mac-install/)

[Windows](https://docs.docker.com/desktop/install/windows-install/)

## Change directory

    cd C:\Users\Thor\Documents\data_study\Python\python_programs\validate_json_yaml\.github\workflows\

## Install act
Windows

    winget install nektos.act

Mac

    gh extension install https://github.com/nektos/gh-act

## Check installed version

    act --version

## List all workflows
    act -l

## Validate workflow job with act (dryrun)
    act -j validate_json_schema -n
