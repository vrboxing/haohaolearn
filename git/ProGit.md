# 开始

## 首次设置
  * git config --global user.name "John Doe"
  * git config --global user.email johndoe@example.com
  * git config --global core.editor emacs
  * git config --list

# 基础 

## 获得一个仓库
   - 在既有目录下初始化仓库
     + git init
   - 克隆既有仓库
     + git clone https://github.com/libgit2/libgit2
## 记录仓库变化
   - 文件状态：追踪、未追踪
   - 追踪文件：未修改、修改、暂存
   - 检查文件状态
     + git status 
   - 跟踪新文件/暂存文件/标明合并冲突已被解决 
     + git add [files]
   - 当追踪文件被暂取后且未提交时，再次修改该文件，则git status会显示该文件两个状态：
     + to be committed: 这是指暂取后且修改前的版本，将要被提交
     + not staged for commit：这是指修改后的版本，尚未暂存
     此时需要再次运行git add，使编译后文件暂存，再提交
   - 短状态：即状态的简短表述
     + git status -s
   - 忽略文件
     + .gitignore
     + *.a : 忽略.a扩展名文件
     + !lib.a : 在.a文件被忽略的前提下追踪lib.a文件
     + /TODO : 只忽略当前文件夹下的TODO文件
     + build/ : 忽略build/文件夹
     + doc/*.txt : 忽略doc/notes.txt之类的文件
     + doc/**/*.pdf : 所有在doc/中的pdf文件
   - 查看暂存和未暂存变化
     + 如果不仅想知道哪些文件变化了，还想知道变化了什么: git diff
     + git diff: 列出工作目录和暂存区中文件的差异
     + git diff --staged :  列出已暂存、待提交的内容
   - 提交变化
     + git commit -m "提交消息"
   - 跳过暂存区
     + git commit -a -m "提交消息": 提交时跳过已编辑的跟踪文件，这些文
       件没有进入暂存区。
   - 删除文件
     + rm [file] : 在工作区中删除，但未暂存
     + git rm : 暂存这个文件的删除
     + git rm -f [file]: 强制删除的安全措施，避免删除尙未在快照中的数
       据意外删除，且不能从Git中恢复。
     + git rm --cached [file] : 保留该文件在硬盘上，但从工作区删除。
     + git rm log/\*.log : 注意*之前的\，Git有自己的文件名扩展方式。相当于shell中的 *.log。
   - 移动文件
     + git mv file-from file-to

## 回顾提交历史
  
  - 选项
    * git log : 列出所有提交，按反时间顺序，最近的提交在最上面
    * git log -p -2: 每一次提交的差异，且只列出后2项
    * git log --stat: 列出每次提交中的修改文件列表，多少文件被修改，文件中被修改的行数
    * git log --pretty=[option]: 自定义列出方式
        - --pretty=oneline: 每个提交信息写在一行
        - --pretty=format:"%h -- %an, %ar : %s "
    * git log --pretty=format:"%h %s" --graph : 以图形显示分支和合并历史
  - 限制日志输出
    * git log -2: 仅显示最后2次提交
## Undoing

  * 提交过早，忘记加入一些文件，搞乱了提交消息时，需要undo
  * git commit --amend
  ```
  git commit -m "initial commit"
  git add forgotten_files
  git commit --amend
  ```
  再次执行提交，效果同前，但增加了一个文件。 
  
  - 取消暂取
    ```
    git add * 
    git status
    git reset HEAD CONTRIBUTING.md
    ```
  
  - 取消修改
  ```
  git checkout -- CONTRIBUTING.md
  ```
## 远程操作

  * git remote: 显示远程仓库的短名
  * git remote -v : 显示远程仓库的地址
  * git remote add [shortname] [url] : 增加远程仓库
  * git fetch [remote-name] : 从远程仓库中获取数据
  * git push [remote-name] [branch-name] : 将本地分支推送到远程分支。
    若此前已有新的推送，则需要下拉新的提交后再次提交。
  * git remote show [remote-name] : 显示远程仓库信息
  * git remote rename pb paul : 修改远程仓库短名
  * git remote rm paul : 删除远程仓库

## 标签

  * git tag : 列出标签
  * git tag -a v1.4 -m 'my verison 1.4' : 标注式标签
  * git show v1.4 : 轻量标签
  * git tag -a v1.2 9fceb02 : 按校验码加标签
  * git show v1.2 : 显示标签为v1.2版本的信息
  * git push origin v1.5 : 推送v1.5版本
  * git push origin --tags : 推送所有标签版本
  * git checkout -b [branchname] [tagname] : 检出版本

## Git别名

  * git config --global alias.co checkout
  * git config --global alias.br branch
  * git config --global alias.ci commit 
  * git config --global alias.st status
  * git config --global alias.unstage 'reset HEAD --'
  * git config --global alias.last 'log -1 HEAD'
  ```
  git unstage fileA
  git last
  ```

# 分支

## Branches in a Nutshell
  * git branch testing : 生成testing分支
  * log --oneline --decorate : 列出版本，并加上当前所在的分支
  * git checkout testing ： 切换到testing分支
## 基本分支和合并
  * git checkout -b iss53 : 生成并切换到iss53分支
  * git checkout master : 修完iss53后回到主分支
  * git merge hotfix : 合并hotfix分支
  * git branch -d hotfix : 删除hotfix分支
  * 解决冲突：
    - 修改冲突后git commit
  * git branch : 列出分支
  * git branch -v : 列出每个分支最后提交
  * git branch --merged : 列出当前分支合并过的分支
  * git branch --no-merged : 列出当前分支尚未合并过的分支
  * git branch -d testing : 删除分支
  * git branch -D testing : 强制删除分支