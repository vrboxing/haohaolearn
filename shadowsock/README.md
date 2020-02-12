# Shadowsock使用方法

## 编译`/etc/shadowsocks.json`


## 启动脚本

`sudo vi /usr/bin/ssr`

```
#!/bin/sh
cd /path/to/shadowsocksr/shadowsocks/
sudo python local.py -c /etc/shadowsocks.json -d start
```

## 退出

`sudo vi /usr/bin/qssr`

```
#!/bin/sh
cd /path/to/shadowsocksr/shadowsocks/
sudo python local.py -c /etc/shadowsocks.json -d stop
```
