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
cat $foo.conf | grep -v -E '^[[:blank:]]*#|^[[:blank:]]*$' # maybe the same, needs checking
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

wrapping ansible-playbook to support proper logging
```
#!/bin/bash
set -o pipefail
_log_path="path-to-your-logs/with-prefix-if-you-want"
_log_user=${USER}
if [ ! -z ${SUDO_USER} ]; then
  _log_user=${SUDO_USER}
fi
for _arg in "$@"; do
  if [[ "${_arg}" =~ .+\.ya?ml ]]; then
    _playbook=${_arg//./_}
    ANSIBLE_LOG_PATH=${_log_path}$(date +%Y%m%d_%H%M%S)-${_playbook}-${_log_user}.log
    export ANSIBLE_LOG_PATH
  fi
done
cat << EOF >> ${ANSIBLE_LOG_PATH}
---
started: $(date --iso-8601=seconds)
args: $@
USER: ${USER}
SUDO_USER: ${SUDO_USER}
---
EOF
SECONDS=0
ansible-playbook $@
cat << EOF >> ${ANSIBLE_LOG_PATH}
finished: $(date --iso-8601=seconds)
runtime: $(printf "%02d" $((${SECONDS} / 60))):$(printf "%02d" $((${SECONDS} % 60)))
EOF
```

