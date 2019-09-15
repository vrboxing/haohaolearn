# *MOPER

```
*MOPER, ParR, Par1, Oper, Val1, Val2, Val3, Val4, Val5, Val6
Performs matrix operations on array parameter matrices.
```

- ParR

    结果向量参数矩阵。
    
- Par1

    第1个输入算子的向量参数矩阵。
    
- Oper

  + INVERT
  
      `*MOPER, ParR, Par1, INVERT`
      
      计算逆矩阵。矩阵必须是良性的，病态矩阵或有相关列矩阵将产生错误。
        
  + MULT
  
      `*MOPER, ParR, Par1, MULT, Par2`
      
      矩阵乘：Par1 x Par2， Par1列数要等于Par2行数。若Par2行数大于Par1列
      数，矩阵依然相乘，但多余行数不被计入运算中。
      
  + COVAR
   
       `*MOPER, ParR, Par1, COVAR, Par2`
       
       自方差矩阵：度量输入矩阵Par1各列的关联程度。
       
  + CORR
  
       `*MOPER, ParR, Par1, CORR, Par2`
       
       相关性矩阵：度量输入矩阵Par1t各列的相关性系数。
       
  + SOLV

       `*MOPER, ParR, Par1, SOLV, Par2`
       
       解方程组：Par1 x ParR = Par2，Par1必须是方阵。方程必须是线性、独
       立、和良性的。
       

其它功能尚不理解。

## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_MOPER.html)
   
  
    
    
