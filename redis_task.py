from config.config import * 


start= time.time() 
def _cache_test(r: redis.Redis, cache_key, sql, TTL, host, user, pswd, db): 

    '''load first from cache layer, otherwise from database '''
    cache= r.get(cache_key)  

    with r.pipeline() as p:      
        if cache is None:
            try:
                '''
                connect to mysql database that store the event stream data from kafka cluster 
                '''
                mysql_conn=pymysql.connect(host, user, pswd, db) 
                cursor=mysql_conn.cursor()
                cursor.execute(kafka_query)
                data= cursor.fetchall() 
                #TODO 
                p.set(cache_key, json.dumps(str(data)))   
                p.expire(cache_key, TTL) 
                p.get(cache_key) 

                result=p.execute()  
                logging.info(f'execute pipe {result}')
                return result 

            except Exception as exc: 
                traceback.print_exc() 
        else:
            return cache 
            
end = time.time() - start 
pprint(f'execute time is {end}') 
