# 为什么要用Emacs

- [一年成为 Emacs 高手 (像神一样使用编辑器)](https://github.com/redguardtoo/mastering-emacs-in-one-year-guide/blob/master/guide-zh.org)

# 配置

- [陈斌配置](https://github.com/redguardtoo/emacs.d) 
- `cd ~; git clone https://github.com/redguardtoo/emacs.d.git .emacs.d`
- [自定义配置](custom.el)
- `custom.el`改名为`.custom.el`，置于`home`路径

# 常用命令 

- 以`M-x`引导以下命令。
- list-packages: 列出包 
- package-install: 安装包 
- `, e b` 重新加载当前文件
- SPC ss: 存储缓冲布局
- SPC ll: 加载缓冲布局
- , sh: 从搜索命令中查找 

# 常用包

- ess
- auctex
- ess-smart-underscore



# Emacs快捷键

https://kb.iu.edu/d/abis

- Select all contens: `C-x h`
- Capitalize a word: `M-c` or `M-x capitalize-word`
- Capitalize all words in a region: `M-x capitalize-region`
- Making words all uppercase : `M-u` or `M-x upcase-word`
- Making regions all uppercase: `C-x C-u` or `M-x upcase-region` 
- Making words all lowercase: `M-l` or `M-x upcase-word`
- Making regions all lowercase: `C-x C-l` or `M-x downcase-region`

# align-regexp

- [正则表达式30分钟入门教程](https://deerchao.net/tutorials/regex/regex.htm)
- [align-regexp的说明](https://emacs-china.org/t/align-regexp/2159)
- 对齐csv格式文件
  1. `C-x h`
  2. `C-u` `M-x` `align-regexp` RET
  3. `\w\(\),` RET
  4. `1` RET
  5. `1` RET 
  6. `y`
  
- 测试工具：https://www.debuggex.com/

# iedit 

- [iedit](https://www.emacswiki.org/emacs/Iedit)
- 使用：
  + `C-;`切换到iedit模式，自动识别光标所在文字，高亮所有相同文字。
  + 再次`C-;`关闭iedit模式。
