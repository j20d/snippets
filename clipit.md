# clipit-actions
stuff I use to transform data inside the clipboard

multiline to sorted space-separated unique line
```
clipit -c|sort -u|xargs| tr -d '\n'|clipit
```
multiline to space-separated
```
clipit -c|xargs| tr -d '\n'|clipit
```
sort
```
clipit -c|sort|clipit
```
sort unique
```
clipit -c|sort -u|clipit
```
space-separated to sorted, unique space-separated
```
clipit -c|tr " " "\n"|sort -u|xargs|clipit
```
space-separated to comma-separated
```
clipit -c |xargs|tr -s " " ","|tr -d '\n'|clipit
```
cleanup inline ansible code
```
clipit -c | tr " " "\n" | sed -es/=/:\ /g|clipit
```
