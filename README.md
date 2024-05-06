# Notion-GoogleTasks-Sync
A Python script for synchronizing tasks between Notion and Google Tasks
# Notion-GoogleTasks-Sync

This repository contains a Python script that enables the synchronization of tasks between Notion and Google Tasks. The script periodically retrieves tasks from Google Tasks and adds any new tasks to a specified Notion database. This allows you to manage your tasks in both Notion and Google Tasks, ensuring that they stay in sync.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `subprocess` package
- `json` package
- `requests` package
- `schedule` package

You will also need valid API credentials and tokens for both Notion and Google Tasks. Please refer to the respective documentation for instructions on obtaining these credentials.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip`:
## Configuration

The script uses cURL commands to interact with the Notion API. You may need to adjust the cURL command in the script to match your specific API version and requirements. Additionally, you can modify the scheduling interval by changing the `schedule.every` line in the script.
