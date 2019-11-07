# ubuntu

## monitor
* `nvidia-smi -l 1` # loop 1 Hz

## mount iso
* Create a directory to serve as the mount location:
`sudo mkdir /media/iso`
* Mount the ISO in the target directory:
`sudo mount -o loop path/to/iso/file/YOUR_ISO_FILE.ISO /media/iso`
* Unmount the ISO:
`sudo umount /media/iso`
* see also
  * https://askubuntu.com/questions/164227/how-to-mount-an-iso-file

## ssh without passwd
* create key files: 
  * `cd ~/.ssh`
  * `ssh-keygen`
    * `id_rsa_foo` # will create `id_rsa_foo` and `id_rsa_foo.pub`
* copy key to remote
  * `ssh-copy-id -i <path/to/id_rsa_goliath.pub> username@remotehost`
* may need to edit `.ssh/config`
* See also:
  * https://www.thegeekstuff.com/2008/11/3-steps-to-perform-ssh-login-without-password-using-ssh-keygen-ssh-copy-id/
  * https://askubuntu.com/questions/762541/ubuntu-16-04-ssh-sign-and-send-pubkey-signing-failed-agent-refused-operation

## must
* `sudo apt install git`
* `sudo apt install sublime-text`, see [this](https://www.sublimetext.com/docs/3/linux_repositories.html)
* `sudo apt install cmake`
* `sudo apt install tmux`
* `sudo apt install htop`
* `sudo apt-get install openssh-server`
* `sudo apt-get install ncdu` # disk utility
* `sudo apt install compizconfig-settings-manager`
  * General -> General Options -> Desktop Size

## nice
* VLC media player
* RecordMyDesktop
* [MeshLab](http://www.meshlab.net/)
* `sudo apt install pdftk`
* `sudo apt install kdenlive`

## misc
* https://www.digitalocean.com/community/tutorials/how-to-set-up-python-2-7-6-and-3-3-3-on-centos-6-4
> Do not assume the tools shipped with the operating system are for your use, and start making the habit of setting up all you need on your own.

