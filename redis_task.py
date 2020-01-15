import redis 
import logging 
import time 
from pprint import pprint 
import traceback 


# TODO
# CACHE_TTL= 60 *10 
# implement the pipeline, transaction, cache

logging.basicConfig(level=logging.INFO) 
conn= redis.Redis(host='localhost', port=6379) 
start= time.time() 

def get_test(r: redis.Redis): 
    with r.pipeline() as p: 

        try:
            p.lpush("name", 'chloe')
            p.lpush("name", 'emma')
            p.lpop("name") 
            result=p.execute() 
            logging.info(f'execute pipe {result}')
            return result 

        except Exception as exc:
            traceback.print_exc(exc) 
            
end = time.time() - start 
pprint(f'execute time is {end}')  

pprint(get_test(conn)) 