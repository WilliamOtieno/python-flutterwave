# Contributing to Python Flutterwave

Thank you for showing interest in contributing to this project. Following these guidelines help to communicate that you respect the time of the developers managing and working on this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes and also helping you finalise your pull requests.

### What do I do? How do I get started?

Follow the [README.md](/README.md) guide. If you've noticed a bug, want to add a feature or have a question, [search the issue tracker](https://github.com/WilliamOtieno/python-flutterwave/issues) to see if someone else already created a ticket. If that has not yet been done, go ahead and [make one](https://github.com/WilliamOtieno/python-flutterwave/issues/new) then assign it to any of the other developers or even yourself.
The issue should also be assigned to the project at hand and one should also add tags to the issue to demystify it.


### Fork the repository
Each developer will have his/her own remote fork(copy) of the repository. Developers are therefore encouraged to create said forks in order to work on the forks rather than on the main repository directly.



### Clone & create a branch

If there is something you think you can fix or contribute to, [clone your project](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) and create a branch with a descriptive name. Always checkout from the **master branch**, that is the default and up-to-date stable branch. I know, not the best practice, but I'm sure we won't break stuff.

A good branch name would be:

```sh
git checkout -b 13-fix-url-endpoints
```

### Commits
The goal is that each commit has a **single focus**. Each commit should record a single-unit change. Now this can be a bit subjective (which is totally fine), but each commit should make a change to just one aspect of the project.
This essentially means that you should commit a change and not a file. A file may have many unrelated changes.

Conversely, a commit shouldn't include unrelated changes - changes to the url routes and changes to the authentication service. These two aren't related to each other and shouldn't be included in the same commit. Work on one change first, commit that, and then change the second one. That way, if it turns out that one change had a bug and you have to undo it, you don't have to undo the other change too.

If you have to use "and" in your commit message, your commit is probably doing too many changes - break the changes into separate commits.

#### Commit Messages

Please follow the below format while writing commit messages:

```
  [Title e.g] One line description about your change
  <Blank Line>
  [Description e.g] An optional detailed description of your changes.
```

Explain what the commit does (not how or why).

### Implement your fix or feature

At this point, you're ready to make your changes. Feel free to ask for help; everyone was once a beginner; everyone is learning.

Submit a Pull Request to the branch you had checked out from in order for the maintainers to review your commit and proceed with the necessary action.

Please ensure that the issue you've fixed is related to the branch you're currently working from. If you want to fix something else unrelated to whatever you've worked on, do another checkout from the staging branch and give the new branch an appropriate name.This makes it easy for the maintainers to track your fixes.

If your fix or contribution involved installing a 3rd Party package that has not been implemented yet, be sure to add the dependency to the [requirements](/requirements.txt) file by executing: 
```shell
pip freeze > requirements.txt
```

### Keeping your Pull Request updated

Related to the above, if a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch, so it's easier to merge.

#### Further Steps

After a feature has been merged into master successfully, developers are encouraged to pull those changes from the origin/upstream to their forks to avoid unnecessary merge conflicts down the line.


### Merging a PR (for maintainers only)

A PR can only be merged into staging by a maintainer if:
- It has no requested changes
- It is up-to-date with current staging branch
- It is a valid fix/feature.
- It has been reviewed and accepted by another maintainer.

Any maintainer is allowed to merge a PR if all of these conditions are met.

Thank you again for your support, happy coding and remember it is your [GNU-given](https://www.gnu.org/home.en.html) right to fork.
