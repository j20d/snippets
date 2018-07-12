# shell & co

## awk

sum up counts for a histogram:
```
awk '{a[$1]++} END {for (i in a) print a[i],i}' 
```

filter multiple matches:
```
awk '$1 != "foo" && $2 != "bar" && $2 != "baz"  {print}' 
```

## bash

sort IPv4-adresses
```
sort -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 
```

do stuff linewise
```
cat foobar | while read line; do echo $line; done
```

strip config files
```
cat $foo.conf | grep -v -E '^[[:space:]]*(#|$)'
```

## bash-aliases and functions

I keep forgetting sudo
```
alias fuck='sudo $(history -p \!\!)'
```

I also keep forgetting that scp needs a colon in source or destination to work with remotes
```
scp() { if [[ $@ == *":"* ]]; then /usr/bin/scp $@; else echo "Damnit Jim, SRC or DST has to be remote!"; fi; }
```
