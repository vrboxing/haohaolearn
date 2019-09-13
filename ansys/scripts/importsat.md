# 引入截面

在桥梁的杆系模型中需要定义很多截面，在ANSYS中定义这些截面是非常低效的。
一种实用的方式是在AutoCAD中绘制这些截面并输出为`.sat`文件，由ANSYS的连接
命令`~SATIN`引入为面，然后划分单元生成截面。


## 代码

```
! 文件: importsat.ans
! 日期: 2015年4月9日
! 作者: 杨大伟 
! 描述: 由sat文件中引入截面 

! 说明
! 在AutoCAD中绘制截面，生成相应的面域，输出为.sat文件
! 将所有.sat文件主文件名列入sectionname.txt中
! 将.sat文件和sectionname.txt文件置于工作目录中
! 运行ansys，在命令框中输入：/input,importsat,ans


finish 
/clear

/inquire,isexist,exist,import_record,log
*if,isexist,eq,1,then
    /delete,import_record,log
*endif

/inquire,my_lines,lines,sectionname,txt

*dim,secfile,string,8,my_lines
*sread,secfile(1),sectionname,txt

/prep7
et,1,plane82

*cfopen,import_record,log
  
*do,iloop,1,my_lines
  /copy,secfile(1,iloop),sat,,temp,sat
  ~satin,temp,sat,,surfaces,0
  smrtsize,2
  amesh,all
  secwrite,secfile(1,iloop),sect,,1
  sectype,iloop,beam,mesh,secfile(1,iloop)
  secoffset,cent
  secread,secfile(1,iloop),sect,,mesh
  secplot,iloop,1
  aclear,all
  adele,all,,,1
  *msg,ui,'Importing SAT Files','Section Number: ',%iloop%,'Section Name: ',secfile(1,iloop)
  %c%/%c%i%/%c%c
  *vwrite,secfile(1,iloop)
  (' File ',a10,' has been imported!')
*enddo

*cfclos

```