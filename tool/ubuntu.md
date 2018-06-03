# ubuntu

## monitor
* `nvidia-smi -l 1` # loop 1 Hz

## ssh without passwd
* create key files: `id_rsa_foo` and `id_rsa_foo.pub`
  * `cd ~/.ssh`
  * `ssh-keygen`
* copy key to remote
  * `ssh-copy-id -i <path/to/id_rsa_goliath.pub> username@remotehost`
* ref: https://www.thegeekstuff.com/2008/11/3-steps-to-perform-ssh-login-without-password-using-ssh-keygen-ssh-copy-id/

## must
* `sudo apt install git`
* `sudo apt install sublime-text`, see [this](https://www.sublimetext.com/docs/3/linux_repositories.html)
* `sudo apt install cmake`
* `sudo apt install tmux`
* `sudo apt install htop`
* `sudo apt-get install openssh-server`
* `sudo apt-get install ncdu` # disk utility

## nice
* VLC media player
* RecordMyDesktop
* [MeshLab](http://www.meshlab.net/)
* `sudo apt install pdftk`
* `sudo apt install kdenlive`

## misc
* https://www.digitalocean.com/community/tutorials/how-to-set-up-python-2-7-6-and-3-3-3-on-centos-6-4
> Do not assume the tools shipped with the operating system are for your use, and start making the habit of setting up all you need on your own.

