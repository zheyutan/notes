# Git and GitHub

https://www.youtube.com/watch?v=xuB1Id2Wxak

## Create repo
git init

## Syncing repos
git remote add origin "link" /n
git pull origin master/branch
### push
1. ssh-keygen
2. cat /***/.ssh/id_rsa.pub
3. paste public key to the SSHkeys in the settings on GitHub
4. ssh -T git@github.com
5. git push origin master/branch

## Making changes
git status
git add (-A)
git commit (-a) -m "notes"

## Parallel Development
### Branching
git branch name_of_new_branch
### Merging
git merge name_of_branch
### rebase
git rebase name_of_branch
