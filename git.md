# git-stuff

## Cleanup deleted branches

```
git fetch -p; git branch -vv|grep ": gone]"|awk '{print $1}'|xargs git branch -D
```

## Create branch locally and remote
```
git branch $1
git push -u origin $1
git checkout $1
```
