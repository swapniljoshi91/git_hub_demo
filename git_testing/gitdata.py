from http.cookiejar import request_port
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


