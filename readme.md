# 用于简单快速共享文件(带简易的密码验证)
## 1.启动
在项目根目录下，直接按照默认配置启动服务：python3 main.py
## 2.自主配置
```
settings.py
    BASE_FOLDER：要共享的目录，默认是项目下的file目录
    SECURITY_USER：安全员的名称(username)
```
## 3.日志(app.log)
上传成功的日志：筛选状态码为201的日志<br>
下载成功的日志：筛选带有username的日志

## 4.下载文件和上传文件
|操作|请求方式|参数|用例|
|--|--|--|--|
|上传文件|POST|file和username|curl -X POST -H "Content-Type: multipart/form-data" -F "file=@filepath" -F "username=XXXX"|
|下载文件|GET|file和username|curl -o wanted_file_name "http://XXX.XXX.XX.XXX:5000/download/?file=wanted_file_name&username=XXXX"|
