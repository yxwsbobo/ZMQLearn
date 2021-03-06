* ZMQ的消息是作为一个整体来收发的，你不会只收到消息的一部分；
* ZMQ不会立即发送消息，而是有一定的延迟；
* 你可以发送0字节长度的消息，作为一种信号；
* 消息必须能够在内存中保存，如果你想发送文件或超长的消息，就需要将他们切割成小块，在独立的消息中进行发送；
* 必须使用zmq_msg_close()函数来关闭消息，但在一些会在变量超出作用域时自动释放消息对象的语言中除外。

---
以下是合法的套接字连接-绑定对（一端绑定、一端连接即可）：

* PUB - SUB
* REQ - REP
* REQ - ROUTER
* DEALER - REP
* DEALER - ROUTER
* DEALER - DEALER
* ROUTER - ROUTER
* PUSH - PULL
* PAIR - PAIR

---
多线程中使用同一个Socket 需要注意
* 使用ZMQ进行多线程编程时，不需要考虑互斥、锁、或其他并发程序中要考虑的因素，你唯一要关心的仅仅是线程之间的消息。

* 不要在不同的线程之间访问同一份数据，如果要用到传统编程中的互斥机制，那就有违ZMQ的思想了。唯一的例外是ZMQ上下文对象，它是线程安全的。

* 必须为进程创建ZMQ上下文，并将其传递给所有你需要使用inproc协议进行通信的线程；

* 你可以将线程作为单独的任务来对待，使用自己的上下文，但是这些线程之间就不能使用inproc协议进行通信了。这样做的好处是可以在日后方便地将程序拆分为不同的进程来运行。

* 不要在不同的线程之间传递套接字对象，这些对象不是线程安全的。从技术上来说，你是可以这样做的，但是会用到互斥和锁的机制，这会让你的应用程序变得缓慢和脆弱。唯一合理的情形是，在某些语言的ZMQ类库内部，需要使用垃圾回收机制，这时可能会进行套接字对象的传递。

---
退出socket需要注意



```plantuml
digraph Test {
A -> B
}
```

```dot
digraph G {
  a->b
}
```

```mermaid
graph TD
A[Hard] -->|Text| B(Round)
B --> C{Decision}
C -->|One| D[Result 1]
C -->|Two| E[Result 2]
```

```puml
 @startuml
:Main Admin: as Admin
(Use the application) as (Use)

User -> (Start)
User --> (Use)

Admin ---> (Use)

note right of Admin : This is an example.

note right of (Use)
A note can also
be on several lines
end note

note "This note is connected\nto several objects." as N2
(Start) .. N2
N2 .. (Use)
@enduml
```