# CMD

## xclip

- 将当前目录拷贝至粘贴板，进入粘贴板中所存的目录，将该目录写到文件中。
```
pwd | xclip
cd $(xclip -o)
xclip -o > ~/test.txt
```
