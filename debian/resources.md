# 源的设置

编译文件：`sudo vi /etc/apt/sources.list`

```
deb http://mirrors.162.com/debian stable main non-free contrib
deb http://mirrors.163.com/debian/ stable-updates main non-free contrib
deb http://security.debian.org/ stable/updates main contrib non-free

#以下源取自launchpad，需要下载密钥
#sudo apt-key adv --keyserver keyserver.ubuntu.com --recv < PUBKEY >
#<PUBKEY>在首次更新后列出缺失的密钥
deb http://ppa.launchpad.net/wiznote-team/ppa/ubuntu/ trusty main
deb http://ppa.launchpad.net/fcitx-team/nightly/ubuntu/ trusty main
deb http://ppa.launchpad.net/numix/ppa/ubuntu/ trusty main
deb http://ppa.launchpad.net/peterlevi/ppa/ubuntu/ trusty main
deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main
deb http://ppa.launchpad.net/timxx/xmradio/ubuntu trusty main
```
