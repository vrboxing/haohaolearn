# Debian
# 下载镜像
- http://mirrors.hust.edu.cn/debian-cd/current/amd64/iso-cd/debian-9.5.0-amd64-xfce-CD-1.iso

# 制作启动u盘

- 确定u盘的设备名称`sdc`，注意不是分区`sdc1`

```
sudo dd if=<xxx.iso> of=/dev/sdc bs=2M
```


# 配置

## 配置`sources.list`

- 切换到`root`帐号，编辑`sources.list`

```
su
vi /etc/apt/sources.list
```

```
deb http://mirrors.163.com/debian/ buster main contrib non-free
deb http://mirrors.163.com/debian/ buster-updates main contrib non-free
```

- 详见：[源的设置](resources.md)

## 安装并配置`sudo`

安装`sudo`可方便软件安装和配置

```
apt update
apt install sudo
chmod +w /etc/suders
vi /etc/sudoers
```

在`sudoers`中填加`<用户名>`的权限

```
<用户名>  ALL=(ALL) ALL
```


## 安装中文字体

安装开源中文字体，方便中文显示。

```
sudo apt install fonts-wqy-zenhei
```

## 配置中文编码

```
sudo dpkg-reconfigure locales 
```

选择`zh_CN.UTF-8`(SPACE切换选择)，确认退出。

## 中文输入

```
sudo vi /etc/default/locale
```

```
LANG=en_US.UTF-8
LC_CTYPE="zh_CN.UTF-8"
```

```
sudo update-locale
```

## 时区

```
sudo dpkg-reconfigure tzdata
```

选择本地城市。

## 交换`Caps Lock`与`Ctrl`

```
sudo vi /etc/default/keyboard
```

```
XKBOPTIONS="ctrl:nocaps"

```


## 桌面主题配置和`Cinnamon`桌面

```
sudo apt install numix-gtk-theme faenza-icon-theme
sudo apt install cinnamon cinnamon-settings-daemon cinnamon-session
```

## 常用工具

```
sudo apt install git emacs vim gimp inkscape fcitx fcitx-table-wbpy pastebinit
```

## 中文字体下载

```
https://github.com/adobe-fonts/source-han-sans
```

##  粘帖代码

- [代码粘帖](pastebinit.md)
