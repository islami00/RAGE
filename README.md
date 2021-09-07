# Rage - BETA1

## Prereq.

1. A posix shell, [gitbash](https://git-scm.com/downloads)

   - Find a youtube video to follow for installation

   - Some important options: add git to path, include git commands in cmd but not all.

2. git itself. (from prev step)
3. A token for authorisation when pushing and pulling locally [set it up here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)
   1. Or use ssh [more here](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh), simpler english [here](https://www.theodinproject.com/paths/foundations/courses/foundations/lessons/setting-up-git)
   2. You'll need a bashrc that handles the initial client setup on start, and for you to start vscode in to give it git powers

## Local setup

Before all this, this is a private repository, meaning you'll have to fork it as private oyo, then do these steps.

1. Clone this repo

- Download the code zip file

Click the green code button and download as zip  

- Or clone the repo to stay uptodate

Open the folder where you want these files to be, then: 

```sh
$ git clone ${repoUrl} .
```

2. Open this in your favorite editor (cough, pycharm)
   1. Then setup a virtual environment by fiddling with the interpreter settings at the bottom right, add interpreter then venv.
   2. Or follow pycharm's guides when you try the next step as it yells at you.
   3. Or use your default env, then you'll only need to install in the next step.

3. Install pygame - this is where pycharm shines.

It knows pygame isn't installed so it will yell at you like `"module not found!"`

- Right click that and install package.

# Finally

Run the game by running main.py to start
