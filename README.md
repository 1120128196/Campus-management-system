项目介绍： 本项目是一个学校后台管理系统   完整包含用户登陆、注册、以及登陆成功后的管理员管理、学院管理、学生管理、账号管理、任务管理、订单管理、数据统计、文件上传和导员管理页面

主要功能囊括了各项增删改查以及文件上传和数据图标展示，内部多为modelform形式的表单提交与验证，也有ajax方式的用户交互。

使用方式  ：

项目导入本地pycharm后 尽量创建一个新的虚拟环境用来运行下载项目的各种模块包，本项目用的python版本为3.9 Django版本为4.2，创建虚拟环境时候需要指定好python版本号并安装4.2版本的Django，别的包直接在pycharm中下载导入。
由于本项目使用的是mysql数据库 需要你手动在mysql中创建一个新的数据库来存放本项目的各数据表 （Django可以自动创建数据表但不能创建数据库）这里对数据库的连接是通过mysqlclient包实现 创建完后需要去settings中修改为自己的数据库。
再通过pycharm自带的工具来创建数据库表![image](https://github.com/user-attachments/assets/77472997-781c-478c-ac49-4c692624ef1a)



![QQ_1743919282346](https://github.com/user-attachments/assets/93348cae-4bb6-464d-9b4e-d74acc2e002b) 

