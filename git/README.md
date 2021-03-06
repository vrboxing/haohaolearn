# Git

<img src="./Git-Icon-Black.png" style="zoom:100%;" />

Git是由Linus Torvalds在2005年创造的软件版本管理和控制软件，如今已被广泛
应用于所有文档版本控制场景中，成为团队协同工作不可或缺的工具。本项目为
Git笔记，用于记录学习资源和心得。

使用Git很容易，但学习它绝非是10分钟之内就能搞定的事。只要遵循好的教程耐
心阅读、勤于实践，相信很快就会掌握Git，给你的工作带来便利。

本文档在持续更新中，最新版本在[这里](https://github.com/yangdaweihit/haohaolearn/blob/master/git/README.md)。

## 下载和安装

- Windows

  Windows版的Git安装包可从[默认下载地址](https://git-scm.com/download/win)得到，但有访问速度更快的镜像：
  https://github.com/waylau/git-for-win/
  
- Debian/Ubuntu

```
sudo apt install git
```

- Mac OS X

```
brew install git
```

## 配置

安装git后的首个动作便是配置，配置文件为`~/.gitconfig`(Linux)或`C:\Users\xxx\.gitconfig`(Windows)：

```
[user]
	name = xxx
	email = xxx@xxx
[credential]
# 授权方式为本地存储文件：.git-credentials
	helper = store
[http "https://github.com"]
# 对github.com使用代理
	proxy = socks5://127.0.0.1:1080
[core]
	editor = vim
```
### 配置用户名和密码

```
git config --global user.name "xxx"
git config --global user.email "xxx@xxx"
```

### 配置编辑器

```
git config --global core.editor vim
```


## 教程

关于Git的教程有很多，在使用时需要注意类别及特点：

- 文字：表述详细，便于回顾，但可能会有理解困难。
- 视频：讲解和操作同步，便于理解。但不便于跳跃式回顾。
- 命令：以示例演示Git命令用法，便于直观体验。

### 视频

观看短视频可以帮我们迅速理解Git，但视频演示对于Git的基本概念和工作原理介
绍不够系统，建议看过视频后系统阅读教程。

- [8小时入门Git之团队合作](https://www.bilibili.com/video/av46637991/?p=1)
- [16小时从入门到精通](https://www.bilibili.com/video/av59634634/?spm_id_from=333.788.videocard.0)
### 文字

`Pro Git`是官网提供的教程，已被翻译成多国语言，浅显易懂，概念体系完整。
童仲毅的个人教程是官网教程的有益补充。

- [Pro Git(中文)](https://git-scm.com/book/zh/v2)
- [Pro Git(en)](https://git-scm.com/book/en/v2)
- [Zhongyi Tong 教程](https://github.com/geeeeeeeeek/git-recipes)

### 命令

- [GitHowTo](https://githowto.com/)
- [命令清单](http://www.codeceo.com/article/git-command-list.html)

## 笔记

- [Pro Git](./ProGit.org)
- [.gitignore](./gitignore.md)
- [杂项](./misc.org)

