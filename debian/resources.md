# 源的设置

参考：

- <https://wiki.debian.org/SourcesList>
- <https://www.debian.org/doc/manuals/apt-howto/ch-basico.en.html>
- <https://www.debian.org/doc/manuals/debian-handbook/apt.en.html#sect.apt-sources.list>

## 源文件

编译文件：`sudo vi /etc/apt/sources.list`

```
deb http://mirrors.ustc.edu.cn/debian/ stable main contrib non-free
deb http://mirrors.ustc.edu.cn/debian/ stable-updates main contrib non-free
deb http://mirrors.ustc.edu.cn/debiancn/ stable/updates main contrib non-free
deb http://security.debian.org/ stable/updates main 

# 以下源取自launchpad，需要下载密钥
# sudo apt-key adv --keyserver keyserver.ubuntu.com --recv < PUBKEY >
# <PUBKEY>在首次更新后列出缺失的密钥
deb http://ppa.launchpad.net/wiznote-team/ppa/ubuntu/ trusty main  # 为知笔记
deb http://ppa.launchpad.net/timxx/xmradio/ubuntu trusty main  # 虾米音乐广播
```

## 源速度测试

- 比较镜像网站

  `sudo netselect ftp.debian.org http.us.debian.org  mirrors.163.com mirros.sohu.com`

- 查找stable版本中最快的镜像网站

  `sudo netselect-apt stable`

## 语言配置

- 一般安装时应选择系统语言时为英文，稍后还要安装上中文编码：

  `sudo dpkg-reconfigure locales`

  在弹出的的对话框中选择`zh_CN.UTF-8`、`zh_CN.GB2312`等，按SPC确认。

- 但这会使得稍后在Emacs中无法输入中文。
  因此需要编辑`/etc/default/locale`：

```
LANG=en_US.UTF-8
LC_CTYPE=zh_CN.UTF-8
```

## 时间配置 

```
sudo dpkg-reconfigure tzdata
```
