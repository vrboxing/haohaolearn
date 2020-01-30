# 杂项

- Trackpoint和Touchpad未启动

```
sudo modprobe -r psmouse
sudo modprobe psmouse proto=imps
```

## 参照

- [Touchpad not working after Debian Buster clean install](https://www.reddit.com/r/debian/comments/compbe/touchpad_not_working_after_debian_buster_clean/)