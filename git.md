# git-stuff

## Cleanup deleted branches

```
git fetch -p; git branch -vv|grep ": gone]"|awk '{print $1}'|xargs git branch -D
```
