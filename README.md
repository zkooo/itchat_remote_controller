# itchat_remote_controller
基于微信的远程控制

### 功能
+ 获取帮助信息
+ 执行系统命令
+ 在后台打开交互式shell，可以向此shell发送命令（能用，但是shell会返回终端转移序列，不知道怎么去除，在想办法）
+ 退出
+ ...

### 安装
  下载项目后，安装python库 [requirements.txt](https://github.com/featherL/itchat_remote_controller/blob/master/requirements.txt)
  运行命令
  ```
  $ pip install -r requirements.txt
  ```
  
  或者手动安装 itchat 
  ```
  $ pip install itchat
  ```
  
  要交互式shell功能的还需安装ptyprocess库，只在Linux下可用
  ```
  $ pip install ptyprocess
  ```
  然后去掉文件cmd.py中的代码注释，具体看文件
 
