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
  - 在Emacs配置文件(init.el或.emacs)中填加：`(require 'ess-site)`
- 注释
  编译ess时如果卡在`loading ess...`了，是拜GFW所赐。该怎么做，你懂的。
- 文档
  http://ess.r-project.org/Manual/ess.html#Command_002dline-editing	

# 使用
- 启动
  `M-x R`
- 交互
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

