## crypting openstack credentials
I don't like having my creds uncrypted.
crypting them using pass and having them decrypted on the fly
by utilizing a fifo makes sure they're not exported.
Since pass is using gpg this works with gpg-agent-forwarding
over SSH and will als for a passphrase on your local machine

This also works for ansible vault credentials.

### Prerequisites:
* pass installed und pass initialized with gpg-key (maybe even in git)
* openstack-creds in clouds.yaml and secure.yaml

### crypting creds
```
cat ~/.config/openstack/secure.yaml | pass insert -m openstack-secure.yaml
mv ~/.config/openstack/secure.yaml ~/.config/openstack/secure.yaml.nocrypt
```
### fifo
```
mkfifo ~/.config/openstack/secure.yaml
```
### feeder-script
The empty echo makes sure that we only request a key for decrypting when 
we really need it, otherwise we'd have decrypted credentials waiting in the fifo.
```
echo ""; pass show openstack-secure.yaml
```
### runner-script
```
while true; do path-to-feeder-script > ~/.config/openstack/secure.yaml
```
### starting the runner
```
nohup path-to-runner-script
```
