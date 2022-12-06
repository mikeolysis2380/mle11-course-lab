<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png" 
     width="200px"
     height="auto"/>
</p>



# <h1 align="center" id="heading">MLE Basic Tools Development</h1>



## ☑️ Objectives

At the end of this session, you will be able to:
- [ ] Have the basic tools for the development of ML applications installed: Command Line Tools, Python3.x, Conda, VS Code, Jupyter Notebook.
- [ ] Understand the benefits of using the above-mentioned tools.
- [ ] Manage environments with `conda` in terminal. 
- [ ] Install packages with `conda` or `pip3` in terminal.
- [ ] Create a GitHub repository for a team project.
- [ ] Create branches, add work to repo, merge branches.
- [ ] Familiarize yourself with CLI tools.
- [ ] Familiarize yourself with pair programming.


## :hammer_and_wrench: Pre-Assignment

### Environment Setup

Let's start off by setting up our environment!  Review the environment setup instructions for the local environment that you'll be using in this course.

<details>
  <summary>Windows</summary>


* Install [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) using Powershell

```powershell
wsl --install -d Ubuntu-20.04
```
* Install [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab) (You can even make it your [default!](https://devblogs.microsoft.com/commandline/windows-terminal-as-your-default-command-line-experience/))

* Install [Ubuntu](https://www.microsoft.com/en-us/p/ubuntu/9pdxgncfsczv?activetab=pivot:overviewtab)

* Make sure you've install the correct version with the command `wsl -l -v`
    
(If you find yourself getting stuck on the WSL2 install, [here](https://www.youtube.com/watch?v=VMZH9Pj2dXw&ab_channel=StefanRows) is a link to video instructions)

Give it a test drive! 

![WindowsTerminal](https://user-images.githubusercontent.com/72572922/160048214-37f08855-8b29-4c13-9d25-e0f69806f752.jpg)

Continue by installing the following tools using [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab) to setup your environment. When prompted, make sure to add `conda` to `init`.

| Tool | Purpose | Command                                                                                           |
| :-------- | :-------- | :------------------------------------------------------------------------------------------------ |
| :snake: **Anaconda**  | Python & ML Toolkits | `wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh` <br> `bash Anaconda3-2021.11-Linux-x86_64.sh` <br> `source ~/.bashrc` |
| :octocat: **Git**  | Version Control | `sudo apt update && sudo apt upgrade` <br> `sudo apt install git-all`   |
| :memo: **VS Code** | Development Environment | [Download](https://code.visualstudio.com/download) |

</details>

<details>
  <summary>Linux (Debian/Ubuntu)</summary>

Open terminal using <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd>. Enter the following commands in terminal to setup your environment. When prompted, make sure to add `conda` to `init`.
| Tool | Purpose | Command                                                                                           |
| :-------- | :-------- | :------------------------------------------------------------------------------------------------ |
| :snake: **Anaconda**  | Python & ML Toolkits | `wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh` <br> `bash Anaconda3-2021.11-Linux-x86_64.sh` <br> `source ~/.bashrc` |
| :octocat: **Git**  | Version Control | `sudo apt update && sudo apt upgrade` <br> `sudo apt install git-all`   |
| :memo: **VS Code** | Development Environment | [Download](https://code.visualstudio.com/download) |

</details>

<details>
  <summary>macOS Intel</summary>

To get started, we need to download the MacOS package manager, <strong>Homebrew</strong> :beer:, so that we can download the tools we'll be using in the course. If you don't already have Homebrew installed, run the following commands:

1. Open terminal using <kbd>⌘</kbd>+<kbd>Space</kbd> and type `terminal`.

2. Install Homebrew using the command below, following the command prompts:

    `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` 

3. Update Homebrew (This may take a few minutes)

    `git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow`

    `git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask fetch`
     
4. Install the `wget` command to continue following along
     `brew install wget`

Enter the following commands in terminal to setup your environment. When prompted, make sure to add `conda` to `init`.

| Tool | Purpose | Command                                                                                           |
| :-------- | :-------- | :------------------------------------------------------------------------------------------------ |
| :snake: **Anaconda**  | Python & ML Toolkits | `wget https://repo.anaconda.com/archive/Anaconda3-2021.11-MacOSX-x86_64.sh` <br> `bash Anaconda3-2021.11-MacOSX-x86_64.sh` <br> `source ~/.bashrc` |
| :octocat: **Git**  | Version Control | `brew install git`   |
| :memo: **VS Code** | Development Environment | [Download](https://code.visualstudio.com/download) |

</details>

<details>
  <summary>macOS ARM</summary><br>

To leverage the Mx chip from Python, you must use a special Python distribution called [Miniforge](https://github.com/conda-forge/miniforge). 
Open terminal using <kbd>⌘</kbd>+<kbd>Space</kbd> and type `terminal`. Enter the following commands in terminal to setup your environment.

Miniforge can be installed using Homebrew or from the source. We suggest trying Homebrew option first.

### Option 1 Homebrew

To get started, we need to download the MacOS package manager, <strong>Homebrew</strong> :beer:, so that we can download the tools we'll be using in the course. If you don't already have Homebrew installed, run the following commands:

1. Open terminal using <kbd>⌘</kbd>+<kbd>Space</kbd> and type `terminal`.

2. Install Homebrew using the command below, following the command prompts:

    `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` 

3. Update Homebrew (This may take a few minutes)

    `git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow`

    `git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask fetch`
     
4. Install the `wget` command to continue following along
     `brew install wget`

5. Install the `xcode-select` command-line utilities by typing the following command in the terminal

    `xcode-select --install`

After running the commands from the table, when prompted, initiate your conda base environment by running `conda init`.
| Tool | Purpose | Command                                                                                           |
| :-------- | :-------- | :------------------------------------------------------------------------------------------------ |
| :snake: **Miniforge**  | Python & ML Toolkits | `brew install miniforge` |
| :octocat: **Git**  | Version Control | `sudo apt update && sudo apt upgrade` <br> `sudo apt install git-all`   |

</details>
<p></p>

## <img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Visual_Studio_Code_0.10.1_icon.png" height=40px/> Let's configure our VS Code environment!

<details>
  <summary>Install the IntelliCode Extension</summary>

  IntelliCode is an AI-powered code completion extension to boost coding productivity. :sunglasses:

  1. Click the `Extensions` <img src="images/vscode_extensions_tab.png" width=30px/> tab in the navigation panel on the left side of VS Code. 

  2. Type "IntelliCode" in the search bar.

  3. Click `install` <img src="images/vscode_install.png" width=30px/> on the <ins><strong>Microsoft IntelliCode Extension</strong></ins>

</details>

<details>
  <summary>Install the Python and Jupyter Notebook Extensions</summary>

  1. Click the `Extensions` <img src="images/vscode_extensions_tab.png" width=30px/> tab on the left side of the window.

  2. Type "Python" in the search bar.

  3. Click `Install` <img src="images/vscode_install.png" width=30px/>  on both the <ins><strong>Python Extension</strong></ins> and on the <ins><strong>Microsoft Jupyter Notebook Extension</strong></ins>

</details>

<details>
  <summary>Set the Python Interpreter</summary>

  1. Open VS Code and click on `New File...`

  2. Open the Command Pallette 
    <strong>(Mac: </strong></ins> <kbd>Shift</kbd><kbd>⌘</kbd>+<kbd>P</kbd> 
    ,<strong> Windows: </strong></ins> <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>)

  3. Type "Python" in the search bar.

  4. Click on `New Python File`

  5. Open the Command Pallette again.  Can you remember the shortcut? If not, see #2 above again.

  6. Type "Python Interpreter".

  7. Click on `Python: Select Interpreter`

  8. Select the `Conda` environment that you installed earlier. 
  
  <p align = "center" draggable=”false”>
  <img src="images/vscode_mlops_interpreter.png"> 
  </p>

  9. Now you're ready to start coding!

</details>

<p> </p>    
     
</details>

<p> </p>

## :rocket: Let's Get Started! 

Being a developer can be quite overwhelming these days. Getting familiar with a codebase and the framework(s) is not the whole story. There is also a real demand of additional skills to get your job done, such as using Git, package managers, and build tooling. This assignment provides an overview to get you up to speed with those tools so you can create, host, and manage your Python projects. To do so, we'll discover how to use many different tools and how they fit into the Python ecosystem. 

### Terminal

For certain tasks you can get away with using the graphical user interface (GUI). This is the application you see on the screen with its buttons and text boxes. For example, there are great GUI tools for working with Git. However, getting familiar with tools like Git from the **terminal** gives you more power and flexibility. In the end, a GUI is a graphical shell in front of a command-line tool. Often limited by screen estate or a minimalistic design, a GUI may feature only a subset of the underlying command-line interface. Being "closer to the metal", it can also help you to get out of trouble in case a GUI is stuck or messed up.

A **terminal** is text-based, and serves as the command-line interface (CLI) you can type your commands in. A shell takes these commands, and tells the operating system to execute them. On macOS, the default terminal application is named `Terminal`, and the default shell is `Bash`. You will also find a `terminal` in Linux distributions like Ubuntu.

### Anaconda

When working with Python in different projects on a single system, the problem of package and version management can get really frustrating. Some projects may require an older Python version like 2.7 compared to another one that needs Python 3.9. Different packages can depend on different versions of other packages. This can result in unknowingly breaking dependencies when updating a package. **Anaconda** solves this as a Python environment manager.

**Anaconda** is a distribution of packages built for data science. It comes with conda, a package, and environment manager. We usually used conda to create environments for isolating our projects that use different versions of Python and/or different version of packages. We also use it to install, uninstall, and update packages in our project environments.

### Jupyter Notebook and VS Code

Now we need a place to write our code. AI/ML Practicioners love to do their research and experiments in **Jupyter Notebook** and **Visual Studio Code (VS Code)**. **Jupyter Notebook** is as a web-based editor for Machine Learning Development, Research, and Experiment for programming languages such as Python, Java, R, Julia, Matlab, Octave, Scheme, Processing, Scala, and many more. **VS Code** is a world class tool to write programs in any language. VS Code also supports many DevOps tools like Ansible, Kubernetes, Yaml and many more.


### GitHub

There comes a certain point in every new developers journey where they need to manage the entirety of their application. We're not talking about deploying a project, but in reference to managing all the files of your project in one specific location. Say you have a project saved to your desktop and one day your system crashes. How terrible would it be if that file was just gone… Days, weeks, months, years of work just gone forever. This is where **GitHub** comes in.

**GitHub** is the social code-hosting platform that’s currently used more than any other and is one of the most essential tools for developers of all levels. It allows for backup and version control, large scale collaboration, expoloring and testing open-source software, emerging technologies, features, and designs. It’s a place to learn and it’s a place to get involved. You can keep code there for work or for school, and you can even hop on another project and start contributing. You can even host websites for free directly from your repository!


## Tasks

There are two tasks and one optional practice assignment to refresh the basics of pandas and sklearn for this session. You will find details in each file. To start, clone this repo. 
1. [Unix-Conda-Pip](nb/unix-conda-pip.ipynb). 
2. [GitHub](md/git-more.md)
3. (Optional)[Pandas-Sklearn-Basics](pandas-sklearn-basics/pandas-sklearn-basics.ipynb)


## How to Submit GitHub Exercise
- Make the project public on GitHub.
- Submit your repo link on canvas. 

## Reference & Advanced Topics
- [Version Control with Git (basics)](https://swcarpentry.github.io/git-novice/)
- [Git Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
- [How Pair Programming Really Works](https://cs.wellesley.edu/~webdb/lectures/01-Overview/PairProgramming.pdf)
- [Cookiecutter: Better Project Templates](https://cookiecutter.readthedocs.io/en/latest/)
- [CI: Building and Testing Python with GitHub Actions](https://docs.github.com/actions/automating-builds-and-tests/building-and-testing-nodejs-or-python?langId=py)
