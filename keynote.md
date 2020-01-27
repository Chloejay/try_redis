## launch redis server 

```bash 
$ redis-server /etc/redis/6379.conf 

$ redis-cli  
$ pkill redis-server
$ redis-cli shutdown
```

#### redis for cache, linked with distributed (HS) system design pattern. <br/>

#### concept 
Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker.<br/> 
The simpfiled system strucyure: 
The client side which sends request to the server and server sends back the response to the client by sending query request to database system and get the response. 
<img src='https://dzone.com/storage/temp/9300395-architecturediagram.png'> 

#### why use redis? 
It provides the benefits about reducing the network calls, recomputation as a gloabl cache layer, which can reponse faster(improve the APP speed and performance) and reduce the database load. It provides better data scale and data resilence. The cache policy, the most appropriate one is the Least Recently Used<a href='http://www.mathcs.emory.edu/~cheung/Courses/355/Syllabus/9-virtual-mem/LRU-replace.html'> LRU</a>. 

- Loading balance is used in this distributed system to decides which worker instance handle a request based on the policy. 
- Data consitency between the cache and database, the write through policy is applied mostly. 
<img src='https://camo.githubusercontent.com/7acedde6aa7853baf2eb4a53f88e2595ebe43756/687474703a2f2f692e696d6775722e636f6d2f51367a32344c612e706e67'> 