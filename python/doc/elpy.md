# Elpy

[elpy](https://elpy.readthedocs.io/en/latest/index.html) 是Emacs中的Python开发环境。在Debian中可以通过安装`elpa-elpy`包获得
Elpy。

## 配置

参照：
1. https://elpy.readthedocs.io/en/latest/introduction.html
2. https://elpy.readthedocs.io/en/latest/ide.html#interactive-python
3. https://elpy.readthedocs.io/en/latest/ide.html
4. [elpy-shell-use-project-root](https://github.com/jorgenschaefer/elpy/issues/1300%0A)

### 软件安装
```
sudo apt install elpa-elpy python3-venv
```

### 配置
在`.emacs.d/init.el`或`.custom.el`中插入：
```
(require 'elpy)
(elpy-enable)
(setq elpy-shell-use-project-root nil)
```
    
## 检查配置

- 检查配置： `M-x elpy-config`
- 开启内部python线程：`,-r-p-y`
- 当Eply模式开启时，可以 `C-Enter` 执行当前行语句，并输出到内部Python交
  互界面中

## 功能

### 文档 

- C-c C-d
  显示当前符号的文档 

### Refactoring

- C-c C-e

    对当前光标所属的符号的同现进行编辑

- C-c C-r f

    用当前格式化工具格式化代码，使用了yapf, autopep8和black。

- C-u C-c C-c

    执行当前脚本

