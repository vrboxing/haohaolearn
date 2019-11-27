# pip

- 安装pip有若干种方式，最方便的是从Linux包管理器中安装，如：

```
sudo apt install python-pip # Python 2
sudo apt install python3-pip # Python 3
```

- 运行pip

```
pip <pip argument> # 经常会出错
python -m pip <pip argument>
python3 -m pip <pip argument>
```

- 用pip安装包

```
python -m pip install <package>
```

- Linux

    修改`~/.pip/pip.conf`(若没有就新建一个)：

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

- Windows

    直接在user目录中创建一个pip目录，如：`C:\Users\xx\pip`，新建文件`pip.ini`，内容如下：

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```