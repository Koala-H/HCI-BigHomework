# 带图片风格变迁和智能水印的瀑布流图片网站：

## 实现方案：

实现了基于Token的注册登录鉴权方案。

在前后端都对邮箱和密码进行了强度鉴定。

实现了验证码以避免爬虫和恶意攻击。

以瀑布流形式排布图片更加美观

可以切换主界面的风格

允许使用邮箱/手机号注册登录

允许以一种或两种图片风格对图片进行风格变迁

可以给图片添加智能水印防止盗用

为了方便检查，登录页面点击登录现在直接跳转到mainpage，mainpage又可以跳转到图片风格变迁页面和水印解密网站

## 安装

本次作业使用了`express@next`，`bcryptjs`, `jsonwebtoken`, `mongoose`, `password-quality-calculator`, 需要系统中安装mongoDB。可以解压后在根目录运行命令`npm install`以获得依赖。此外还使用到了yarn，也需要按照下面的指示进行安装。

## 运行过程：

在使用时，需要先开启mongoDB，以管理员身份在cmd中输入以下指令：

```shell
启动服务：net start MongoDB
关闭服务：net stop MongoDB
移除服务：D:\developer\env\MongoDB\bin\mongod.exe –remove
```

并打开mongoDB的GUI点击“connect”

先在pic_style目录下执行以下指令：

```shell
npm install --global yarn #用来安装yarn

yarn run prep #用yarn安装依赖包

yarn run start #启动服务
```

再进入client目录执行以下指令：

```shell
node server.js
```

启动服务

启动后架设在端口3001，即通过[localhost:3001（服务器IP:3001）](localhost:3001)可访问主页index.html，然后点击右上角的登录与注册链接即可注册与登录。

对原内容做了部分改进，在进行转化时消耗时间可能不稳定。

## 参考文献

[1、常用密码强度正则表达式](https://www.section.io/engineering-education/password-strength-checker-javascript/)

[2、登录注册功能的设计](https://www.woshipm.com/pd/5417791.html)

[3、一文教你搞定所有前端鉴权与后端鉴权方案，让你不再迷惘](https://juejin.cn/post/7129298214959710244)

[4、图片风格变迁使用了此开源工具](https://github.com/reiinakano/arbitrary-image-stylization-tfjs)