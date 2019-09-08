# Ubuntu

- switch only on current workspace in GNOME shell
  https://askubuntu.com/questions/464946/force-alt-tab-to-switch-only-on-current-workspace-in-gnome-shell

- hp 1020
  https://blog.hostonnet.com/how-to-install-hp-laserjet-1020-plus-printer-drivers-in-ubuntu-16-04

# 将capslock设置为ctrl
- 编辑`/etc/profile`
- /usr/bin/setxkbmap -option "ctrl:nocaps"
 

# Themes 

- Applications: Numix

- Cursor: DMZ-Black

- Icons: Faenza-Ambiance

# PATH 

`/etc/enviornment` --> `.profile`

```
PATH=$PATH:~/.local/bin;
export PATH
```

# 启动时自动执行脚本 

`/etc/rc.local`

```
#! /bin/sh 
ssr
exit 0
```

`sudo chmod +x /etc/rc.local`

## 重命名

安装`rename`

例如重命名`[NS]D[1-13]索力时程.png`为`[NS]D[1-3].png`：

```
rename 's/索力时程//' *.png
```

## unzip

- [字符集](https://www.iana.org/assignments/character-sets/character-sets.xhtml)
- [以特定字符集解压](https://superuser.com/questions/872596/decompress-zip-with-given-encoding)

- 示例：
```
unzip -O GB18030 xxx.zip -d target_dir
```

## iconv

- 查看文档编码
```
file -i xxx.srt
```

- [转换命令](https://www.tecmint.com/convert-files-to-utf-8-encoding-in-linux/)
- 示例
```
iconv -f GB18030 -t UTF-8 xxx.rst -o xxx_utf8.rst
```

## 网易云音乐


```
sudo vi /usr/share/applications/netease-cloud-music.desktop
Exec=sh -c "unset SESSION_MANAGER && netease-cloud-music %U"
```
