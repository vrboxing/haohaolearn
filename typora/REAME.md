
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

#  Markdown笔记

来源：https://support.typora.io/Markdown-Reference/

[Typora](https://typora.io/)是目前我们见到的撰写Markdown文档的最佳工具。本文介绍了[Typora](https://typora.io/)所支持的Markdown语法格式和渲染方式。

<div align="center">
<img src="./markdown.png" style="zoom:45%;" />
</div>

[toc]


## 块单元

### 段落和行断

- 一个段落即连续的文字行。
- 段落由一个或多个空白行分隔。
- 回车(`Return`)生成一个新的段落。

[返回](#Markdown笔记)

### 标题(Header)

标题使用1-6个`#`开头，对应1-6级标题。如：

```

# This is an H1 

## This is an H2 

###### This is an H6

```

- > 快捷键：`Ctrl + 1`表示1级标题，以此类推。

[返回](#Markdown笔记)

### 块引用

Markdown用邮件样式`>`符号表示块引用。

源码：

```
> This is a blockquote with two paragraphs. This is first paragraph.
>
> This is second pragraph. Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
```

渲染：

> This is a blockquote with two paragraphs. This is first paragraph.
>
> This is second pragraph. Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

- 快捷键：`Ctrl + Shif + Q`表示1级标题，以此类推。

[返回](#Markdown笔记)

### 列表

- 键入`*`建立一个无顺序列表。（`*`可被`+`或`-`替代）

- 键入`1.`生成一个有顺序列表。

  ```
  ## 无序列表
  *   Red
  *   Green
  *   Blue
  
  ## 有序列表
  1.  Red
  2. 	Green
  3.	Blue
  ```

[返回](#Markdown笔记)

### 任务列表

任务列表用`[ ]`或`[x]`标识，如：

```
- [ ] a task list item
- [ ] list syntax required
- [ ] normal **formatting**, @mentions, #1234 refs
- [ ] incomplete
- [x] completed
```

- [ ] a task list item 

- [x] list syntax required 
- [x] normal ***\*formatting\****, @mentions, #1234 refs 
- [ ] incomplete 
- [x] completed

[返回](#Markdown笔记)

### 代码块

Typora只支持Github风格的代码块Markdown语法，而不是Markdown原始的代码块样式。

使用代码块很容易，键入\```，然后回车。在\```后面跟上一个语言名称，可以对代码进行相应的语法高亮渲染。

源码：

```
​```
function test() {
  console.log("notice the blank line before this function?");
}
​```

语法高亮:
​```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
​```
```
渲染：
```
function test() {
  console.log("notice the blank line before this function?");
}
```

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

[返回](#Markdown笔记)

### 数学式块

Typora可使用**MathJax**渲染$\LaTeX{}$。换成其它编辑器，尚没有找到这样立等可取的效果。要添加一个数学式，可输入`$$`后按`Return`键。如：

$$\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\ \frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\ \end{vmatrix} $$ 

其代码为：

```
$$
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
\end{vmatrix}
$$
```

 更多细节在[这里](https://support.typora.io/Math/)。再来一个漂亮的公式吧：
$$
\begin{align*}
y = y(x,t) &= A e^{i\theta} \\
&= A (\cos \theta + i \sin \theta) \\
&= A (\cos(kx - \omega t) + i \sin(kx - \omega t)) \\
&= A\cos(kx - \omega t) + i A\sin(kx - \omega t)  \\
&= A\cos \Big(\frac{2\pi}{\lambda}x - \frac{2\pi v}{\lambda} t \Big) + i A\sin \Big(\frac{2\pi}{\lambda}x - \frac{2\pi v}{\lambda} t \Big)  \\
&= A\cos \frac{2\pi}{\lambda} (x - v t) + i A\sin \frac{2\pi}{\lambda} (x - v t)
\end{align*}
$$

[返回](#Markdown笔记)

### 表格



[返回](#Markdown笔记)



### 脚标

You can create footnotes like this[^fn1] and this[^fn2]. 



[^fn1]: Here is the **text** of the first ***\*footnote\****. 
[^fn2]: Here is the **text** of the second ***\*footnote\****. ↩

### 水平线

在一个空行处输入 `***` 或`---`然后 `return`即可画出一条水平线。

### 目录

输入`[toc]`后按`Return`即生成一个目录节。目录提取本文档中的所有标题，其内容将随文件内部动态更新。

##   跨越单元

[返回](#Markdown笔记)




### 链接

Markdown支持两类链接：`inline`和`reference`。两种链接中，链接文字都被方括号包围。



#### 行内链接
```
This is [an example](http://example.com/ "Title") inline link.
[This link](http://example.net/) has no title attribute.
```

[返回](#Markdown笔记)

#### 内部链接

用标题样式作为引用即可实现内部链接。按`Ctrl`键同时点击该链接即可跳转到引用处。如：

```
[返回](#Markdown使用说明)
```

[返回](#Markdown笔记)

#### 参考链接

引用风格链接

[返回](#Markdown笔记)

### URLs

Typora支持用`<>`包含的地址作为链接，如`<i@typora.io>`变为： <i@typora.io>。

同时Typora亦可自动将标准地址格式变为链接。

[返回](#Markdown笔记)

### 图片

插图与链接语法相同，只是在链接前额外加一个`!`。语法示例：

```
![Alt text](/path/to/img.jpg) 
![Alt text](/path/to/img.jpg "Optional title")
```

- 可直接拖拽图片到Typora里面。如下面的动画所示：

  ![](./drag-img.gif)

- 若图片与文档在同一文件夹或子文件夹中，则默认采用相对路径。

如果察看的是本文档的`PDF`文档，你将看不到下面的插图动画效果。

[返回](#Markdown笔记)

### 强调

[返回](#Markdown笔记)

### 加粗

[返回](#Markdown笔记)

### 代码

[返回](#Markdown笔记)

### 删除线

[返回](#Markdown笔记)

### Emoji
Emoji :happy:

[返回](#Markdown笔记)

### 行内数学式

[返回](#Markdown笔记)

### 下角标

[返回](#Markdown笔记)

### 上角标

[返回](#Markdown笔记)

### 高亮

[返回](#Markdown笔记)


## HTML				

<span style="color:red">this text is red</span>

### 下划线

[返回](#Markdown笔记)

### 嵌入内容

[返回](#Markdown笔记)

### 视频

[返回](#Markdown笔记)

### 其它HTML支持

[返回](#Markdown笔记)