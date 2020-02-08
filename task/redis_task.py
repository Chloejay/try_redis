from config.config import * 
from datetime import datetime 

start= time.time() 
def _cache_test(r: redis.Redis, 
                cache_key:str, 
                sql:str, 
                TTL:int, 
                host: str, 
                user:str, 
                _pswd:str, 
                db: str) -> str: 

    '''load first from cache layer, otherwise from database '''
    cache= r.get(cache_key)  

    with r.pipeline() as p:      
        if cache is None:
            logger.info('cache is not found')
            try:
                '''
                connect to mysql database that stores event stream data from kafka cluster 
                '''
                mysql_conn=pymysql.connect(host, user, _pswd, db) 
                cursor=mysql_conn.cursor()
                cursor.execute(kafka_query)
                data= cursor.fetchall() 

                #TODO 
                p.set(cache_key, json.dumps(str(data)))   
                p.expire(cache_key, TTL) 
                p.get(cache_key) 

                result=p.execute()
                pprint(f'execute pipe {result}')
                return result 

            except Exception as exc: 
                traceback.print_exc() 

        else:
            logger.info(f'catch cache {cache} at {datetime.now()}')
            return cache 
            
end = time.time() - start 
pprint(f'execute time is {end}')