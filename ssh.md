### scp 
* scp source:pathtosource destination:localfilepath
* /etc/sshd/config

### SSH Config
* sudo apt install openssh-server
* sudo systemctl start ssh
* allow port 22 on firewall
* systemdtools or systemctl

### Port forwarding rules
* protocol: tcp
* host port 2222
* guest port 22
* name ssh

### Bridging allows vm to emulate the computer on the network

## hardening
* sshd is daemon
* ssh is the client

look for these
1. protocol
   1. `Protocol 2`
   2. should be version 2. 
   3. ssh protocol 1 is not secure, not supported in most cases
2. port
   1. port 22 by default
   2. why change?
      1. easier to hide it in a high port number from nmap
      2. if ssh isnt at standard port, nmap might not know what it is running elsewhere
   3. why not?
      1. most client use 22, so its more difficult to manage
3. PermitEmptyPasswords
   1. should be no
   2. obviously... its good for users to have passwords
   3. keep it at no
   4. not important, because good password policies should prohibit this anyway
4. PermitRootLogin
   1. users shouldnt be able to login as root period
   2. no, prohibit-password, without-password, yes
      1. dont allow root login
      2. dont allow password, require pubkey auth
      3. without-password, no password needed
      4. allow any login to root remotely
5. PubkeyAuthentication
   1. yes, more secure than password
   2. no reason to not have this
   3. `ssh-keygen`
   4. secure copy paste server pubkey to your client
6. PasswordAuthentication
   1. if set to no, only allows via key
   2. keys harder to break than passwords
   3. to set up pubkey authentication, you must login by password firs
   4. is there a way to allow password auth on a user to user basis?
7. AllowUsers
   1. what users can login via ssh?
8. AllowGroups
   1. what groups can login via ssh?
      1. make an ssh group for ssh users
9. DenyUsers
10. DenyGroups
    1.  both are these are blacklisting users and groups
11. X11 forwarding
   1.  gui server
   2.  allow rdp
   3.  no unless they REALLY need a gui
12. ClientAliveInterval
    1.  how long can they be connected without doing anything
    2.  0 is indefinitely
    3.  anything above that is time to auto-boot out in seconds
    4.  5 minutes is good, 30 minutes is pretty good too
13. ClientAliveCountMax
    1.  how many times they can check the alive check
    2.  if the interval is 5 minutes, and the client alive count max is 3, every 5 minutes the connection prompts the user to confirm theyre still there. If the check failes 3 times, the connection is dropped
    3.  1 check means first check fails, user booted

* to add groups, and group members etc/groups
* usermod also works

### Whoami, who, w
* whoami
  * username
* who
  * username, terminal name, login date
  * shows all instances of user being logge din
  * find unauthorized connectiosn
* w
  * username, terminal name, login date, login time, processes
* chsh is change shell command
* PS1 environment variable controls terminal prompt

### Kill unauthorized connections
* `ps aux` to find user process
* `who` reveals process name
* `kill (pid)` will kill the process whicht eh ssh user is connecting with
  * `kill -9 (pid)` will force the kill if the first doesnt work
* you could also do `pkill (process name)`

### SSH keygen
* `ssh-keygen`
  * key saved in .ssh
* login to server via ssh password
* `scp` the server pubkey to client
* you could also use `ssh-copy-id`
* you could also copy the pubkey from the client to the server, then move the public key to `.ssh/authorized_keys`
* always keep stuff updates
* always apt install your apps periodically!
