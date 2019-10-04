# Xfce

## 事件声音

1. 安装`libcanberra`和`libcanberra-pulse`
2. 在`.profile`中设置`GTK_MODULES`环境变量：
```
GTK_MODULES="canberra-gtk-module"
export GTK_MODULES
```
3. 检查设置管理器中的"Enable event sounds" → Appearance → Settings tab
   → Enable evnet sounds
4. 在声音控制中打开`Sytem sounds`
5. 设置声音主题
```
xfconf-query -c xsettings -p /Net/SoundThemeName -s "sound-theme-freedesktop"
```

在必要时执行如下操作：
```
xfconf-query -c xsettings -p /Net/EnableEventSounds -s true
xfconf-query -c xsettings -p /Net/EnableInputFeedbackSounds -s true
```

试听某个声音文件命令：
```
canberra-gtk-play -f /path/to/<filename>.oga
```

## 参考

- [Sound themes](https://wiki.archlinux.org/index.php/Xfce#Sound_themes)
- [Smooth](https://www.xfce-look.org/p/1187979/)
- [Enable system sounds in Xfce](https://cybergnomer.wordpress.com/2014/11/01/enable-system-sounds-in-xfce/)