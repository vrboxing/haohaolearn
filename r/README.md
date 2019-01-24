# r

本文档汇总r语言编程文档。

## 设置镜像

- 镜像列表：https://cran.r-project.org/mirrors.html
- 配置文件：`/etc/R/Rprofile.site`:

```
local({
  r <- getOption("repos")
  r["CRAN"] <- "https://mirrors.ustc.edu.cn/CRAN/"
  options(repos = r)
})
```


## 书评

- Adler2012, R in a Nutshell

  适合初学，打下扎实基础。

- Dalgaard2008, Introducotry Statistics with R

  + describes applications of R for actual sta- tistical analysis
  + 在基本学会R和统计学的基础上，示范统计计算的教程。
  + 适合作为统计学的配套练习教材。

## rJava & xlsx
  + rJava安装不了
    - 解决：https://stackoverflow.com/questions/12872699/error-unable-to-load-installed-packages-just-now
    - 解决：https://www.r-bloggers.com/installing-rjava-on-ubuntu/
