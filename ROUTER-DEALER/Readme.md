# ROUTER-DEALER 模式

![router-dealer](./router-dealer.png)  

---

* 内置代理 zmq_device (ZMQ_QUEUE, frontend, backend)
* 主要用于扩容REQ-REP模式
* Client 和 Server 都无需知道对方，只需要知道 Broder即可，由Broker进行分发请求和应答，内部会负载均衡