from http.cookiejar import request_port
from unittest import removeResult
from urllib.response import addbase

git --version           use for check git version.

git config --list       to know configration in to the git
git config global user.name "<USERNAME>"
git config global user.email "<eamilid>"
git init     track created folder through it
git status   to chack the git repo status

git add <file name>
git add *             move all file and folder from the repo
git add -A            move all file/ folder from the repo
gir add .             move all hide file/ folder from the repo

git restore --staged * move undo all file and folder from the stage to rapo
git restore --staged . move undo all hide file/ folder from the stage to rapo

git diff to check the what changes made by user

git commit -m "comment"                move file and folder from staged to main secton

git log it list out commit on the rep

git show <commit id>:<filename>   to check priveus file which is commited

git checkout <commit id> --* goto specific commet no, file

git checkout master/main -- * back to master file

restore

git restore .        undo letest changes
git restore <file name>


git restore --worktree .
git restore --worktree <filename>  restore file from stage secton


resotore after comment
git reset --soft head^    undo privius file commit without data
git reset --hard head^    undo privius file commit with data




git log
git log -p -2 (last 3 comment with diff)
git log --stat (summary of changes)

git log --pretty=online
git log --pretty=format:"%h - %an, %ar:%s"
git log -S function_name

git remote repo


git remote  add origin https://github.com/<username>/<reponame>.git
git branch -M main
git branch -M master
git push -u origin main

git remote

git remote -v


git pull  it is for taking data from online repo

git clone <repo link>





