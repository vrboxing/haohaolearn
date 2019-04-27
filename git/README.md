# Git

## What is Git
- https://en.wikipedia.org/wiki/Git_%28software%29
- /git/ or `技特`

## Resources
- http://git.oschina.net/progit/index.html
- https://git-scm.com/book/zh/v2

## Books
- Scott Chacon, Ben Straub. Pro Git, 2015, Apress
- Ravishankar Somasundaram. Git: Version Control for Everyone, 2013, Packet Publishing  
- 蒋鑫. Git权威指南，2011, 机械工业出版社

## Concepts

- `VCS`: version control system，版本控制系统。
- 本地版本控制系统：在本地机上运行的版本控制系统。
- 集中化版本控制系统(`CVCS`)：由一个服务器管理所有客户端机上版本控制系统。
- 分布式版本控制系统(`DVCS`)：客户端管理完整的代码仓库。
- 一句话历史：在`Bitkeeper`不再免费提供代码托管服务后，为了解决全世界`Linux`开发者协同工作的问题，`Linus Torvalds`于2005年4月花了三个星期开发出的世界上最优秀的版本控制系统。
- checksum：版本的校验和，由Git自动计算得出的40个十六进制字符，相当于版本的身份证号。
- 文件状态：包括已提交(`commited`)、已修改(`modified`)、已暂存(`staged`)。
- 工作区域：包括工作目录(`working directory`)、暂存区(`staging area`)、本地仓库(`repository`)。
- 托管网站：提供代码托管的git服务网站，如[github](https://github.com)、[bitbucket.org](https://bitbucket.org)、[coding.net](https://coding.net)、[git.oschina.net](https://git.oschina.net)。不管什么托管网站，于你而言，它只是`origin`。


## Installation
- Debian/Linux: `apt install git`
- Windows: https://git-for-windows.github.io/
- Mac: http://code.google.com/p/git-osx-installer

## Commands

- `config`

- `init`

- `add`

- `commit`

- `branch`

- `checkout`

- `status`

- `merge` 

- `clone` 

- `pull` 

- `push` 

- `fetch` 
## Minor mode in Emacs

- `, v a`: git-add-current-file 
