# 配置
- [陈斌配置](https://github.com/redguardtoo/emacs.d) 
- `cd ~; git clone https://github.com/redguardtoo/emacs.d.git .emacs.d`
- [自定义配置](custom.el)
- `custom.el`改名为`.custom.el`，置于`home`路径

# ESS
- `sudo apt install ess`


## ess-smart-underscore
- [ess-smart-underscore](https://github.com/mattfidler/ess-smart-underscore.el)
- 将`ess-smart-underscore.el`拷贝到
  `~/.emacs.d/site-lisp/ess-smart-underscore`中
- 在`.custom.el`中填加`(require 'ess-smart-underscore)`
 
# AUCTEX
- `sudo apt install auctex`

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