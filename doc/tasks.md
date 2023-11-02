# Tasks

The **`nmk-badges`** plugin defines the tasks described below.

## Setup tasks

All tasks in this chapter are dependencies of the base [**`setup`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#setup-task) task.

(badgesTask)=
### **`badges`** -- insert badges in README.md file

This tasks inserts the configured **{ref}`${badges}<badgesConfig>`** in the project **README.md** file.

| Property | Value/description |
|-         |-
| builder  | {py:class}`nmk_badges.builder.NmkBadgesBuilder`
| input    | **{ref}`${badgesTarget}<badgesTarget>`** file (may be modified manually)
| output   | **{ref}`${badgesStamp}<badgesStamp>`** stamp file
| deps     | base [**`out`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#out-output-folder-creation) task

The builder is invoked with the following parameters mapping:

| Name | Value |
|- |-
| badges | **{ref}`${badges}<badgesConfig>`**
| begin_pattern | **{ref}`${badgesBeginPattern}<badgesBeginPattern>`**
| end_pattern | **{ref}`${badgesEndPattern}<badgesEndPattern>`**
