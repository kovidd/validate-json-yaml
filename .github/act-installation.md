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

Bash

    curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash


## Check installed version

    act --version

## List all workflows
    act -l

## Validate workflow job with act (dryrun)
    act -j validate_json_schema -n


### Potential error
`Error: failed to start container: Error response from daemon: network-scoped alias is supported only for containers in user defined networks`

he error message you are encountering suggests that the network-scoped aliases feature is only supported for containers in user-defined networks and not for the default network.

The act tool uses Docker to run GitHub workflows locally. By default, Docker containers are connected to a default network, which might not support network-scoped aliases.

To resolve this issue, you can try running act with the **--network host flag**, which uses the host's network stack instead of creating a separate network for the container:

    act -v --network host

By using the host's network stack, you should be able to avoid the error related to network-scoped aliases.

Alternatively, you can create a user-defined Docker network and specify it while running act. To create a network, use the following command:


    docker network create mynetwork

Then, when running act, provide the network name like this:

    act -v --network mynetwork

By using a user-defined network, you should also be able to avoid the error.

Try these suggestions and see if it resolves the issue for you.
