# Git

## DoD (Definition of Done)
At a high level, get comfortable with [Git Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow); specifically, you should complete the following
- [ ] Create a public repo on GitHub
- [ ] Several commits with meaningful messages.
- [ ] Create a branch and the branch name should be descriptive.
- [ ] Create Pull requests on GitHub
- [ ] Conduct Code Review 
- [ ] Merge pull requests into the `main` branch
- [ ] Delete the branch remotely and locally when done
- [ ] Pull changes from a remote repository

## Step by Step Instructions
Detailed instructions for a team project repo, adapted from the example in Git Feature Branch Workflow. 

IMPORTANT. Explain explicitly what each step does to your partner. If the code or instruction looks unfamiliar/unclear, ask for help and clarification.

0. Determine who Apple and Bill are
    - Apple - Team Member A
    - Bill - Team Member B

1. Bill creates a new repo on GitHub called `naive-addition` and adds Apple as a collaborator.
    - [ ] Repo is made public.
    - [ ] Repo includes README.md.
    - [ ] Repo includes LICENSE (e.g., MIT).
    - [ ] Repo includes .gitignore file (e.g., for Python).

2. Apple and Bill clone the repo locally ( replace the handle and repo with the names of your GitHub repo ).
    - `git clone git@github.com:<handle>/naive-addition.git`
    - check your local repo and make sure it looks like ( hint: use`tree -a -L 1` )
    ```
        .
        ├── .git
        ├── .gitignore
        ├── LICENSE
        └── README.md
    ```

3. Work on separate features
    - Apple works on a feature to add a source folder with two new python files:
        - `git checkout -b feature-add-src`
        - `mkdir src`
        - `touch src/__init__.py`
        - `touch src/add.py`
        - Open `src/add.py` and write the following:
            ```
            def add(x:int, y:int=100) -> int:
                """
                Add two numbers together.

                Args:
                    x (int): The first number.
                    y (int): The second number. Defaults to 100.
                Returns:
                    int: The sum of the two numbers.
                """
                return x + y
            ```
        - `git add src/__init__.py src/add.py`
        - `git commit -m "add src directory and add.py"`
        - `git push origin feature-add-src`
    - Bill works on a feature to include all of the python modules and packages that the project depends on.
        - `git checkout -b feature-add-requirements`
        - `touch requirements.txt`
        - `git add requirements.txt`
        - Open `requirements.txt` and write the following:
            ```
            numpy==1.22.3
            pandas
            ```
        - `git commit -m "add requirements.txt"`
        - `git push origin feature-add-requirements`
4. Each creates a pull request (PR) back to the `main` on GitHub (see [doc](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)). In your pull request, you should include a description of the changes you made and assign your partner to be the reviewer.
5. Review your own pull request on GitHub. This step is often overlooked yet important. You want to make sure that the changes in each file are correct and exactly what you wish to do and NOT waste anyone's time reviewing changes that are incorrect.
6. Review your teammate's pull request on GitHub. Bill reviews `feature-add-src` and Apple does `feature-add-requirements`. If there's any feedback from your reviewer, resolve it under the feature branch and repeat steps 4 and 5. Otherwise, procceed to step 7.
7. Merge the changes into the `main` branch. Bill merges `feature-add-src` and Apple is responsible for merging `feature-add-requirements`. You can do this step in command line (i.e., `git merge`), yet it is straightforward to do it on GitHub after reviewing the pull request.
8. Follow the instructions on GitHub to merge the changes into the `main` branch. In the end there is option to delete the feature branches, click `Delete Branch` if you finish the feature development. This deletes the remote branch. If you miss this step, you always find the page again under Pull requests/# Closed. 
9. Pull changes from the `main` branch and merge them into your local branch.
    - make sure you are on the `main` branch
        ```
        % git status
        On branch main
        ...
        ```
        if not: `git checkout main`
    - `git pull origin main`
10. Delete the feature branches locally to keep your local space clean. 
    - Apple runs `git branch -d feature-add-src`
    - Bill runs `git branch -d feature-add-requirements`


In the end, the `main` branch should look like this:
```
.
├── .git
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── src
    ├── __init__.py
    └── add.py
```

### Best Practices
- decide who works on which feature of the project among team members
- use descriptive branch names
- always be committing with meaningful messages
- NEVER commit to the `main` branch directly
- do code review frequently

## Frequently Used Git Commands
### Solo
`git clone` - clone a repository

`git status` - check the status of your local repository; do it often

`git diff` - see the changes between commits

`git add` - add a file to the staging area

`git commit` - commit your changes: ABC = Always Be Committing

`git push` - push your changes to a remote repository

`git log` - see the history of your commits

### On a team
`git pull` - pull changes from a remote repository

`git branch` - list the branches in your repository

`git checkout` - switch to a different branch
