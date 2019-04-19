# data_center  


概述
---

data_center以django-ORM管理股票数据。  
包含股票基础数据，K数据，Tick数据，计算用数据，个人历史交易数据等。  


起源
---
想做量化交易，之前一直使用[tushare](https://github.com/waditu/tushare)来获取数据。  
之后接触了[django](https://github.com/django/django)，萌生了借用其ORM来管理数据的念头。  
在django的playing with the API中获取灵感，直接用shell来操作数据，免去了写各种sql的麻烦事。  


功能
--
* 保存股票数据
* shell直接操作数据
* 记录交易，方便统计

App
--
* **stock**
    * URL /stock/
    * 功能
        * /update_stock_data/ 每日更新股票基础信息，名称，ST等。



