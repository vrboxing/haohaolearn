# 杂项

- Trackpoint和Touchpad未启动

```
sudo modprobe -r psmouse
sudo modprobe psmouse proto=imps
```

- 缺少固件

```
W: Possible missing firmware /lib/firmware/i915/icl_dmc_ver1_07.bin for module i
915
W: Possible missing firmware /lib/firmware/i915/tgl_dmc_ver2_04.bin for module i
915
W: Possible missing firmware /lib/firmware/i915/bxt_huc_ver01_8_2893.bin for mod
ule i915
```

1. 建立文件夹
```
sudo mkdir -p /lib/firmware/i915
```

2. 拷贝相应的固件[i915](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/i915)

3. 重新配置`initramfs-tools`包

```
sudo dpkg-reconfigure initramfs-tools
```

## 参照

- [Touchpad not working after Debian Buster clean install](https://www.reddit.com/r/debian/comments/compbe/touchpad_not_working_after_debian_buster_clean/)

- https://askubuntu.com/questions/811453/w-possible-missing-firmware-for-module-i915-bpo-when-updating-initramfs