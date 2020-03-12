# 请求-应答 模式

![req-rep](req_rep.png)  

![req-mutrep](./req-mutrep.png)

---
* 必须严格交替 请求-应答 不可以连续发送或接收
* *Server 端 与 Client 端 运行不分先后
* 测试可多个 Client 连接同一个 Server,Server replay 对象为最后一个 request的 socket
* 抓包得知 建立连接时是会传输魔术字，协议类型等