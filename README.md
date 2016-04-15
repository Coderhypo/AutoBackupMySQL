# MySQL自动备份

每天自动备份Docker或服务集成（DaoCloud）中的MySQL数据库，并将备份信息发送到指定邮箱。

## 配置

因为是将容器中的MySQL备份到Volume中，因此需要配置数据库和邮箱和Volume信息到环境变量中

### 数据库信息

+ DATABASE_NAME: 将要备份的数据库名
+ HOST: 数据库主机，默认localhost
+ USERNAME: 用户名 
+ PASSWORD: 密码
+ PORT: 数据库端口，默认3306

### 邮箱信息

+ TO: 收件人邮箱 eg. wenter@126.com
+ FROM: 发件人邮箱 eg. wenter@126.com
+ PASSWORD: 发件人邮箱密码 eg. wenteriscoming
+ SMTP: 发件邮箱SMTP地址 eg. smtp.126.com

### Volume信息

因为要将数据库备份到Volume中，因此需要添加一个环境变量来记录Volume的挂载位置

+ BACKUP_DIR: Volume的挂载位置，默认 /backup

