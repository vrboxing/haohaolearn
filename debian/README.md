# Debian

本文记录安装Debian/Linux系统的个人习惯。操作前提为：

- 熟悉`vi/vim`的一般编辑功能；
- u盘容量大于`1G`。

# 下载镜像
- [mirrors.ustc.edu.cn](http://mirrors.ustc.edu.cn)中有获取镜像的入口，可由链接下载镜像。 
- 亦可直接下载：[http://mirrors.ustc.edu.cn/debian-cd/current/amd64/iso-cd/debian-9.5.0-amd64-xfce-CD-1.iso ](http://mirrors.ustc.edu.cn/debian-cd/current/amd64/iso-cd/debian-9.5.0-amd64-xfce-CD-1.iso)
- 若版本有变，可访问文件夹下载：[http://mirrors.ustc.edu.cn/debian-cd/current/amd64/iso-cd](http://mirrors.ustc.edu.cn/debian-cd/current/amd64/iso-cd)

# 制作启动u盘

## Windows
- 启动盘制作工具，如`UltraISO`

## Debian/Unbuntu

- 插入u盘，查看u盘设备名称。
```
sudo df  # 以/dev/sdc1为例，其挂载点为 /media/wall-e/sony
sudo umount /media/wall-e/sony  # 卸载u盘

```

- 确定u盘的设备名称`sdc`，注意不是分区`sdc1`，写入iso镜像文件 

```
sudo dd if=<xxx.iso> of=/dev/sdc bs=2M
sync # 注意要做同步，确保完成拷贝
```

# 配置

## 配置`sources.list`

- 切换到`root`帐号，编辑`sources.list`

```
su
vi /etc/apt/sources.list
```

```
deb http://mirrors.ustc.edu.cn/debian/ buster main contrib non-free
deb http://mirrors.ustc.edu.cn/debian/ buster-updates main contrib non-free
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
sudo apt install papirus-icon-theme moka-icon-theme
```
[papirus-libreoffice-theme](https://github.com/PapirusDevelopmentTeam/papirus-libreoffice-theme)

LibreOffice Calc: Options > LibreOffice > View > User Inferface > Icon style = Epapirus


## 常用工具

```
sudo apt install git emacs vim gimp inkscape fcitx fcitx-table-wbpy pastebinit
sudo apt install thunderbird
sudo apt install gparted variety 
```

## 中文字体下载

Adobe公司提供的开源字体： 
[思源无衬线](https://github.com/adobe-fonts/source-han-sans/tree/release)，
[思源有衬线](https://github.com/adobe-fonts/source-han-serif/tree/release)

##  粘帖代码

- [代码粘帖](pastebinit.md)

## 微信

```
sudo apt install libgconf2-dev libgail-dev
```

- 托[Zhongyi Ton](https://github.com/geeeeeeeeek)的福：
[electronic-wechat](https://github.com/geeeeeeeeek/electronic-wechat/releases/)

下载`linux-x64.tar.gz`解压后运行`./electronoic-wechat`

- 在`/usr/sharep/applications/`新建`wechat.desktop`

```
[Desktop Entry]
Name=WeChat
GenericName=Net Social Message
Comment=Net Social Message
Exec=/path/to/electronic-wechat
Icon=/path/to/wechat.png
Terminal=false
Type=Application
Categories=Network
```


# 命令行

[CMD](./cmd.md)

# apt-mark
标记`sudo`为手动安装，避免因其它程序卸载而被连带卸载。
```
  apt-mark manual sudo
```
# crontab

启机时自动执行脚本，需要`root`权限。

```
sudo crontab -e
```
填加：
```
@reboot bash /path/to/script.sh
```
