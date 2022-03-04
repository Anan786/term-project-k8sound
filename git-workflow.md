# Git Workflow

We follow this workflow to work on the sprint items.

## Create an Issue

Before you start making a change to the code, please make sure there is a corresponding issue describing your task. If there is no existing issue corresponding to your task, please create one and communicate with the product owner.

## Create a New Branch

Please create a new branch for your work and use the following branch naming format.

```
{issue_id}-{description}-{description}
```

For example, if there is an issue regarding fixing the music create API, and the issue’s ID is 12, the branch name should be similar to:

```
12-fix-music-create-api
```

## Create Pull Request

If the branch is ready to be merged after you commit your changes, please create a pull request. In the pull request description, please briefly summarize what you have done to help the reviewers review your code.

Your pull request must be reviewed by at least one reviewer. If the reviewer thinks your changes are good to be merged, the reviewer approves your pull request. The pull request creator will then click on the merge button to merge the changes, and the branch must be deleted after the changes are successfully merged.

## Close the Issue

After the changes are merged, please ensure that the issue is closed. Normally, if the branch naming format is correct (with the issue ID at the beginning), GitHub will close the issue automatically after the changes are merged. However, it is the pull request creator’s responsibility to make sure the issue is closed properly.
