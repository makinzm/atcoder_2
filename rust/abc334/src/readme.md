I think it is good to find the answer about c. 
However, the way to implement is not good. I need to consider what is the most simple and efficient way to implement it.

```bash
================================================
  NLOC    CCN   token  PARAM  length  location  
------------------------------------------------
      11      2     40      0      11 main@8-18@../rust/abc334/src/a.rs
      28      6    172      0      29 main@7-35@../rust/abc334/src/b.rs
      55      9    341      0      64 main@8-71@../rust/abc334/src/c.rs
3 file analyzed.
==============================================================
NLOC    Avg.NLOC  AvgCCN  Avg.token  function_cnt    file
--------------------------------------------------------------
     16      11.0     2.0       40.0         1     ../rust/abc334/src/a.rs
     33      28.0     6.0      172.0         1     ../rust/abc334/src/b.rs
     61      55.0     9.0      341.0         1     ../rust/abc334/src/c.rs

===============================================================================================================
No thresholds exceeded (cyclomatic_complexity > 15 or length > 1000 or nloc > 1000000 or parameter_count > 100)
==========================================================================================
Total nloc   Avg.NLOC  AvgCCN  Avg.token   Fun Cnt  Warning cnt   Fun Rt   nloc Rt
------------------------------------------------------------------------------------------
       110      31.3     5.7      184.3        3            0      0.00    0.00
```