# CMD

## 系统查询

- 查看系统版本
```
lsb_release -a
```
- 查看内核版本
```
uname -a
```

- 查看硬件

  + `lscpu`：查看CPU信息
  + `lspci`：查看PCI设备
  + `fdisk -l`: 查看分区
  + `df -h`：查看磁盘信息
  + `lsmod`：当前加载的驱动

- 查看显卡型号
```
lspci | grep -i vga
sudo lshw -numeric -class video # 使用lshw
nvidia-smi #如果知道是NVIDIA显卡，还可以使用命令：
```

- 查看声卡型号
```
lspci |grep -i audio
cat /proc/asound/cards
```

- 查看网卡型号
```
lspci | egrep -i 'network|ethernet'
lshw -class network
```

- 查看网络设备
```
ip a
```

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