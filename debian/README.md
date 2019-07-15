# Debian

- 主题：[Qogir-win-dark](https://github.com/vinceliuice/Qogir-theme)
- 图标：[Suru++ Dark](https://github.com/gusbemacbe/suru-plus-dark)

## 下载镜像

 从[中国科技大学镜像网站](https://mirrors.ustc.edu.cn)下载镜像文件：
 [debian-live-[version]-amd64-gnome.iso](https://mirrors.ustc.edu.cn/debian-cd/current-live/amd64/iso-hybrid)。

# 制作启动u盘

Windows系统使用`UltraISO`或其它类似工具。在Linux系统中，一般使用`dd`命令。

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

## 源配置 

- [源的设置](resources.md)

## 安装并配置`sudo`

安装`sudo`可方便软件安装和配置

```
su
apt update
apt install sudo
chmod +w /etc/suders
vi /etc/sudoers
```

在`sudoers`中填加`<用户名>`的权限

```
<用户名>  ALL=(ALL) ALL
```

## 字体配置

有时系统内未安装目标字体，系统会自动将既有字体与目标字体对比，将最接近的字体替换目标字体。编辑`fonts.conf`即可人工配置替换字体。
```
vi .config/fontconfig/fonts.conf
```

```
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>

  <match target="pattern">
    <test name="family" qual="any" >
      <string>Times</string>
    </test>
    <edit name="family" mode="assign" binding="strong">
      <string>Times New Roman</string>
    </edit>
  </match>

  <match target="pattern">
    <test name="family" qual="any" >
      <string>Courier</string>
    </test>
    <edit name="family" mode="assign" binding="strong">
      <string>Free Courier</string>
    </edit>
  </match>

</fontconfig>
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

# Emacs服务器开机启动

```
crontab -u <用户名> -e
```
编辑开机启动项：
```
@reboot LC_CTYPE=zh_CN.UTF-8 emacs --daemon
```
将开启emacs命令与快捷键绑定：
```
/usr/bin/emacsclient -c -a "" -F "((fullscreen . maximized))"
```


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

##  fcitx

去除fcitx关于`C-;`的快捷键定义：
- Configure/Addon/Clipboard/Trigger Key ....将`C-;` 改成Empty，用Esc键修改

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

# Spotify

- [Spotfiy](https://www.spotify.com/hk-en/download/linux/)


# variety

- Clock font: Noto Sans Arabic UI ExtraCondensed ExtraBold, 50
- Date font: Sans Regular 20
