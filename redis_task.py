import redis 
import logging 
import time 
from pprint import pprint 
import traceback 
import pymysql 


CACHE_TTL= 60 *10
HOST='localhost'
USER='root'
PSWD='password'
DB='kafka_test'


logging.basicConfig(level=logging.INFO) 
conn= redis.Redis(host='localhost', port=6379) 
start= time.time() 

sql= '''select favorite_color from kafkav1 where id=1'''

def get_test(r: redis.Redis, sql, TTL, host, user, pswd, db): 
    with r.pipeline() as p: 

        try:
            # p.lpush("name", 'chloe')
            # p.lpush("name", 'emma')
            # p.lpop("name") 
            mysql_conn=pymysql.connect(host, user, pswd, db) 
            cursor=mysql_conn.cursor()
            cursor.execute(sql)
            data= cursor.fetchall() 
            #TODO 
            p.set('key', str(data))
            p.expire('key', TTL) 
            p.get('key') 
            result=p.execute() 

            logging.info(f'execute pipe {result}')
            return result 

        except Exception as exc: 
            traceback.print_exc() 
            
end = time.time() - start 
pprint(f'execute time is {end}')  

pprint(get_test(conn, sql, CACHE_TTL, HOST,USER, PSWD, DB )) 