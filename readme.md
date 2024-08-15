# hackernews-api-test

## Pre-requisites
python >= 3.9 and pip3 installed

## Setup and installation
- Clone and navigate to the project directory (hackernews-api-test) in terminal
- Install Homebrew as mentioned here: https://brew.sh/
- Install Allure report: Run the command `brew install allure`
- Install and activate virtual environment by running the below commands:
  - `pip3 install virtualenv`
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
- Install the requirements by running the command `.venv/bin/pip3 install -r requirements.txt`

## How to run tests and generate report
- Increase number of available file descriptors by running the command `ulimit -n 65536`
- Navigate to `tests` package of the project
- To run all the tests, run the command `../.venv/bin/pytest`
- After running the tests, generate Allure report by running the command `allure serve <path to allure-results directory>`. Example: From `tests` directory, run `allure serve ../allure-results`
- Deactivate virtual environment by running the command `deactivate`

## Bug found
In items API, the count of `kids` is more than `descendants`. In other words, deleted comments' IDs are shown in kids but not in descendants. Some examples of stories exhibiting this behavior at the time of testing: 41251170, 41255512, 41257374, 41257378, 41233206, 41247724. The Hackernews team accepted it as a bug and agreed to fix it. 