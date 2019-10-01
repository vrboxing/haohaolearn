# Using Emacs as a Server

## 启动服务器

有若干种启动服务器的方式：

- 在当前Emacs进程中运行`server-start`命令，有2种方式：
  + `M-x server-start`
  + 将`(server-start)`表达式写入初始化文件
  则当前进程就成为了服务器。当退出当前Emacs时，服务器随进程而退出工作。
- 以守护进程方式运行Emacs，用`--daemon`选项之一。此时，初始化后调用
  `server-start`且不打开窗口，等待客户端的编辑请求。
- 若系统用`systemd`管理启动时，可通过守护模式启动Emacs：
```
systemctl --user enable emacs
```

## emacsclient

在我的系统中，采用了`systemd`启动Emacs服务器的方式。每次开机后，Emacs服
务器便运行在后台。当需要打开Emacs窗口时，便可运行`emacsclient`。为了方便
调用这条命令，设置了`Ctrl-Alt-e`快捷键，对应的命令为：

```
emacsclient -create-frame --alternate-editor=""
```


## 参考

- [Emacs Server](https://www.gnu.org/software/emacs/manual/html_node/emacs/Emacs-Server.html)
- [emacsclient Options](https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html#emacsclient-Options)