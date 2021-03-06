日期:2018-11-29
课程:git
姓名:王丹波

----------- 主要内容 -----------
1. 版本管理工具git
2. 调试工具pdb

上次内容回顾
1. 固定集合: 创建集合的时候,限定了大小,笔数
   特点: 
     当集合空间用完后,新插入的数据会覆盖之前的数据
   优点:
     插入速度,顺序查找速度快
     能够淘汰早期的数据
     可以控制集合的大小
   应用场景:
     临时缓存,日志
   创建语法:
     db.createCollection(collection,
        {capped:true, size:1000, max:100}   
    )
2. 文件存储
  1) 两种文件存储方式
    - 数据库中存储文件路径,文件单独放到某个目录下
      优点:节约数据库空间
      缺点:存储路径和实际路径不一致时,文件丢失
    - 将这个文件存入数据库
      优点:数据库和文件绑定存在
      缺点:占用数据库空间较多
  2) GridFS: 用来将存取文件
    - 将文件分割成多个片段,存储到数据库中
    - 包含两个集合:
      fs.file: 存储文件元信息(大小,片段数量,MD5值)
      fs.chunks: 存储文件实际内容
    - 示例:
      存文件
      mongofiles -d gridfs put tmp.tar.gz

      取文件
      mongofiles -d gridfs get tmp.tar.gz

3. pymongo:Python操作MongoDB接口
   查看pymongo版本:pip3 list | grep pymongo 

   - MongoClient: 返回数据库连接对象
     e.g. conn = pymongo.MongoClient(host,port)
   
   - list_database_names()
     database_names()
     获得服务器上所有数据库列表

   - 获取数据库对象:  mydb = conn["test"]
     conn: 数据库连接对象

   - 获取集合对象: mycol = mydb["acct"]
     mydb: 数据库对象

   - 插入: 
      insert(), insert_one(), inser_many()
      save()

   - 修改: 
      update(query, update, 
             upsert=False, multi=False)
        query: 筛选条件
        update: 修改的内容
        upsert: 是否执行插入
        multi: 是否修改多行

   - 删除: delete_one, delete_many
   - 查询: find()

作业:
1)创建订单集合(名称orders),包含的域有:
  order_id: 订单编号, 字符串
  cust_name: 订单所属客户, 字符串
  order_date: 下单时间,Date类型
  status: 订单状态, 整数
  order_detail: 订单明细, 文档数组
    product_id: 商品编号, 字符串
    product_name: 商品名称, 字符串
    amt: 商品数量, 整数
    price: 单价, 浮点数
2)插入3笔订单数据,每个订单至少包含1件商品
  至少有一个订单包含多件商品(注意数据规范性)
  db.orders.insert({
      order_id:"201811200001",
      cust_name:"Jerry",
      order_date: new Date(),
      status:1,
      order_detail:[
          {product_id: "P0001",
           product_name:"水杯",
           amt:1,
           price:15.00
          },
          {product_id: "P0002",
           product_name:"C语言编程",
           amt:1,
           price:65.00
          }
      ]
  })

  db.orders.insert({
      order_id:"201811200002",
      cust_name:"Dokas",
      order_date: new Date(),
      status:1,
      order_detail:[{
           product_id: "P0003",
           product_name:"手机",
           amt:1,
           price:1999.00
          }]
  })

3)编写下列语句
  a)查找所有状态为1的订单
   db.orders.find({status:1})

  b)查找某个客户状态为1的订单(cust_name,status)
   db.orders.find({
     cust_name:"Jerry",
     status:1
   })

  c)查找某个时间点以后下单的订单
    db.orders.find({
      order_date:{
        $gt:ISODate("2018-11-20T08:29:45")}
    })

  d)统计订单笔数
    db.orders.find().count()

  e)修改某个订单的状态
    db.orders.update(
      {order_id:"201811200001"},
      {$set:{status:2}})

  f)为所有订单添加一个域:
    支付状态(payment_status),整数
    db.orders.update(
      {},
      {$set:{payment_status:null}},
      false, true
    )

  g)查询所有订单中,商品编号为"P0001"的订单
    db.orders.find({
      "order_detail.product_id": "P0001"
    })

  h)在订单集合的订单编号(order_id)域上创建升序索引
    db.orders.createIndex({order_id:1})

  i)为某个订单增加备注信息(要求为字符串数组)
   db.orders.update(
     {order_id:"201811200001"},
     {$pushAll:{remark:["工作日送达","后付款"]}}
  )

  j)删除一笔无效订单(status判断,具体值自己定)

今天的内容
1. 版本管理工具git
  1)什么是版本控制(Revision Control)
    - 项目文档包含:
      源码
      文档(需求,设计,会议纪要,厂商联系方式)
      软件包(开发工具,数据库,第三方库)

    - 对各种软件所涉及到的文件进行管理
      控制,变更记录,追溯

    - 什么时候,什么人,修改了什么文件,什么内容
      完整记录
      配置管理岗: 专门进行配置管理 

    - 解决什么问题 
      - 版本管理规范性
      - 解决版本更新,冲突
      - 协调不同的开发者的变更,提高协同开发的效率

    - 版本管理的相关术语
      - 检出: 将软件配置(文件)从配置库中提取出来
      - 检入: 将软件配置项(文件)放回配置库
      - 主干版本: 标准配置库
      - 分支版本: 为了某些特殊要求
                 和主干版本有差异的配置库
      - 合并:
        - A,B两个版本,将A的内容附加到B中
        - A,B两个版本,A和B合并,形成新版本Ｃ

      －历史记录：
      　文件变更的详细过程
　　　
　　　　－回滚：将配置退回到之前的某个状态

　　２) 版本管理方式
　　　　ａ)集中式管理
　　　　　－配置库集中存放于中央服务器
　　　　　－变更之前，先从中央服务器取得最新版本
　　　　　　然后进行变更，修改
　　　　　－修改完成后，将变更提交到中央服务器
　　　　　－缺点：集中式存放，必须联网，速度较慢
　　　　　－典型工具：SVN
       b)分布式
       　－没有中央服务器
       　－每个开发人员电脑都是一个完整配置库
       　－配置库位于本地，所以不一定需要联网
       　－每个开发者，可以将自己的代码贡献到
       　　其他开发者仓库中
       　－典型工具：git

２.git: 分布式配置管理工具
　１)更适合个人开发，管理配置库
　２)分布式管理，不同ｓｖｎ的集中式管理
　３)支持强大的分支功能
　４)完整性优于ｓｖｎ

３.git安装：sudo apt-get install git

4.git配置
　1)/etc/gitconfig文件：作用于系统所有用户
　2)～/.gitconfig文件：用户目录下，作用于当前用户
　3)工作目录下.git/config文件，作用于当前目录
　优先级：工作目录>用户配置>系统配置
　４)配置示例：
　　－git config --global user.name tarena
   - git config --global user.email wangdb@tedu.cn
   
   查看：cat ~/.gitconfig

   - 查看已有配置: git config --list

5.git基本命令
  1) init: 
    执行如下几个命令:
      cd ~    # 进入用户主目录
      mkdir gittest  # 新建一个空目录
      cd gittest
      git init  # 初始化,成功后当前会多出.git隐藏目录
  
  2) add: 添加文件内容至索引
     vim a.txt     # 新建文本文件
     git add a.txt # 将a.txt添加到仓库中
     git status    # 查看当前目录状态

  3)commit: 提交变更至本地仓库
    git commit 文件名 -m 注释信息

    示例: git commit a.txt -m "create"
    * 必须写注释

  4)diff: 查看工作目录和仓库文件的差异
    例如: git diff a.txt

  5)reset: 版本的回滚
    git reset --hard HEAD^  回退到上一个版本
    git reset --hard HEAD^^ 回退到上上一个版本
    git reset --hard HEAD~n 回退到前面第n个版本

6. 分支管理
  1)分支版本:有别于主版本,例如开发版,某个定制版
  2)分支操作
    - 查看所有分支: git branch
      列出所有版本,带*表示当前所在分支
    - 创建分支版本
      git branch 分支版本名称
     
      e.g.  
      git branch dev #创建名称为dev的分支版本
    
    - 切换分支版本
      git checkout 分支版本名称

      e.g. 
      git checkout dev  #切换到dev分支下

    - 创建并切换分支
      git checkout -b beta #创建并切换到beta分支下
    
    - 版本合并: 
      git merge beta  #把beta版本合并到当前分支

      第一步: 进入到beta分支
             git checkout beta
      第二步: 修改a.txt,并提交(提交到beta分支)
      第三步: 切换到dev分支
             git checkout dev
      第四步: 执行合并 
             git merge beta #把beta分支合并到当前分支
    
    - 删除分支:
      git branch -d beta 
      删除beta分支,如果没有合并则不允许删除
    
    练习常用命令: init,add,commit,diff,checkout,
                log,status,reset
7. 标签管理
  1)如果达到一个重要节点, 并希望永远记住那个提交
    的快照, 可以使用标签
  2)标签可以理解成一个指向某次提交的指针,
    但不能移动
  3)标签命令: git tag 标签名称.例如:
    git tag v1.0   #将v1.0标签打到最新版本上
    git tag        #查看所有标签
    git tag v0.9 0771ec3 #将v0.9标签打到制定的0771ec3版本上

    git reset --hard v0.9 #退回到v0.9标签状态

8. github远程仓库
  第一步:在gitee或github上注册账号
  第二步:创建项目,并且拷贝地址
  第三步:在工作目录下加入远程仓库地址
    git remote add 名称 远程仓库地址

    例如:
    git remot add gitee https://gitee.com/bbsmil/git_test2.git
  
  第四步:从远程仓库获取配置库
    切换到master分支下,做一个pull操作
    git pull 远程仓库名称 分支版本名称
    例如: git pull gitee master
  
  第五步: 修改工作目录文件,并且提交到本地仓库
    例如: 修改a.txt后, 执行提交 
         git commit a.txt -m "remote test"

  第六步: 推送到远程仓库
    git push -u 远程仓库名称 分支版本
    
    例如:git push -u gitee master
       * 推送到gitee仓库的master分支下

9. 调试工具
  1)程序调试(debug): 程序在开发,测试,维护过程中
            需要对程序测试,排除错误
  2)调试工具:提高调试效率的工具
           一般都能单步,打印变量,观察内部执行过程
  3)pdb: Python自带的调试工具
  4)使用:
    - 启动调试: pdb3.5 tmp.py  # 对tmp.py调试
    - l 或 list: 查看当前代码段
    - n 或 next: 执行下一行
    - b 或 break: 打断点
       例如: b 10 或 break 10 #在第10行打断点
    - clear 1    # 删除编号为1的断点
    - p 或 print: 打印变量
    - s 或 step: 进入函数
    - r 或 return: 从当前函数返回

作业:熟悉git,pdb操作
    复习网络多线程服务器编程