# 源的设置

## 源文件

编译文件：`sudo vi /etc/apt/sources.list`

```
deb http://mirrors.162.com/debian stable main non-free contrib
deb http://mirrors.163.com/debian/ stable-updates main non-free contrib
deb http://security.debian.org/ stable/updates main contrib non-free

#以下源取自launchpad，需要下载密钥
#sudo apt-key adv --keyserver keyserver.ubuntu.com --recv < PUBKEY >
#<PUBKEY>在首次更新后列出缺失的密钥
deb http://ppa.launchpad.net/wiznote-team/ppa/ubuntu/ trusty main  #为知笔记
deb http://ppa.launchpad.net/fcitx-team/nightly/ubuntu/ trusty main  #fcitx输入法
deb http://ppa.launchpad.net/numix/ppa/ubuntu/ trusty main #numix桌面主题
deb http://ppa.launchpad.net/peterlevi/ppa/ubuntu/ trusty main  #variety墙纸
deb http://ppa.launchpad.net/tiheum/equinox/ubuntu trusty main #faenza图标主题
deb http://ppa.launchpad.net/timxx/xmradio/ubuntu trusty main  #虾米音乐广播
```

## 源速度测试

- 比较镜像网站

  `sudo netselect ftp.debian.org http.us.debian.org  mirrors.163.com mirros.sohu.com`

- 查找stable版本中最快的镜像网站

  `sudo netselect-apt stable`
