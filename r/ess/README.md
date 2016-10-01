Emacs Speaks Statistics(ESS) 是Emacs的插件，用于支持各类统计分析程序的脚本编辑和交互。
http://ess.r-project.org/

# 准备
- 下载 
  - http://ess.r-project.org/index.php?Section=download 下载压缩包
  - https://github.com/emacs-ess/ESS git克隆
- 安装
  - make
  - sudo make install
- 配置
```
(require 'ess-site)
(setq tramp-ssh-controlmaster-options nil) ;;解决启动卡死的问题。这个是关于TRAMP的bug，解决方案来自于<https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=810640>。
(eval-after-load "comint"
  '(progn
      (define-key comint-mode-map [up]
        'comint-previous-matching-input-from-input)
      (define-key comint-mode-map [down]
        'comint-next-matching-input-from-input)
      ;; also recommended for ESS use --
      (setq comint-scroll-to-bottom-on-output 'others)
      (setq comint-scroll-show-maximum-output t)
      ;; somewhat extreme, almost disabling writing in *R*, *shell* buffers above promp
      (setq comint-scroll-to-bottom-on-input 'this)
))
```
  
- 文档
  - [使用文档](http://ess.r-project.org/Manual/ess.html#Command_002dline-editingy)
  - [常用命令](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjc1LDKzLnPAhXI9x4KHckjDAwQFggcMAA&url=http%3A%2F%2Fess.r-project.org%2Frefcard.pdf&usg=AFQjCNGgVjKkGEAYjmuzJGBuN5RGEMnP5A&sig2=H5Yx-0VZYcEof1DBTxdxww&bvm=bv.134495766,d.dmo)

# 使用
  
  ## 交互界面
  - `M-x R`
  - 直接输入命令，`RET`。
  - RET 发送命令
  - C-c C-w 删除前一个命令
  - C-c C-u 删除提示符到当前点内容，用于放弃还未执行命令
  - C-c C-a 移动到本行启始处
  - C-c C-p 移动当前点到之前的命令
  - C-c C-n 移动到下一条命令
  - RET 移动到当前命令后再次执行
  - C-c RET 将命令拷贝到当前命令行，编辑后可再执行
  - M-p 输入历史中选择之前的命令
  - M-n 输入历史中选择之后的命令
  - [up] [down] 重复前一个和后一个命令
 
  ## 脚本

  - C-c C-c 运算区域或段落
  - C-<RET> 运算区域或行
  - C-c C-l 加载缓冲区内的源文件
  - C-c C-j 运算本行
  - C-c M-j 运算本行及以下
  - C-c C-f 运算函数
  - C-c M-f 运算函数及以下
  - C-c C-r 运算区域
  - C-c M-r 运算区域及以下
  - C-c C-b 运算缓冲区
  - C-c M-b 运算缓冲区及以下