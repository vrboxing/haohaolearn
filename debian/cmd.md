# CMD

## apt-cache

apt-cache对APT包进行查询输出。

- 查找<package-name>的依赖包。
```
apt-cache depends <package-name>
```

## xclip

- 将当前目录拷贝至粘贴板，进入粘贴板中所存的目录，将该目录写到文件中。

```
pwd | xclip
cd $(xclip -o)
xclip -o > ~/test.txt
```

## 查看启动中的错误

```
sudo dmesg | grep <错误信息关键字>
```


## apt-mark
标记`sudo`为手动安装，避免因其它程序卸载而被连带卸载。
```
  apt-mark manual sudo
```