# Shotcut

Shotcut是一款轻量级视频编辑软件。在Linux中运行界面无法适应显示屏，需要修改其快捷方式中的运行命令：


```
Exec=env QT_AUTO_SCREEN_SCALE_FACTOR=0 sh -c "<path to shotcut>/shotcut "%F""
```
