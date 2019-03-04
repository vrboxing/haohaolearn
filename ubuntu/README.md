# Ubuntu

- switch only on current workspace in GNOME shell
  https://askubuntu.com/questions/464946/force-alt-tab-to-switch-only-on-current-workspace-in-gnome-shell

- hp 1020
  https://blog.hostonnet.com/how-to-install-hp-laserjet-1020-plus-printer-drivers-in-ubuntu-16-04

## unzip

- [字符集](https://www.iana.org/assignments/character-sets/character-sets.xhtml)
- [以特定字符集解压](https://superuser.com/questions/872596/decompress-zip-with-given-encoding)

- 示例：
```
unzip -O GB18030 xxx.zip -d target_dir
```

## iconv
- [转换命令](https://www.tecmint.com/convert-files-to-utf-8-encoding-in-linux/)
- 示例
```
iconv -f GB18030 -t UTF-8 xxx.rst -o xxx_utf8.rst
```

