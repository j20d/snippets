# assorted Snippets:

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
