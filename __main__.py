from redis_task import _cache_test 
from config.config import * 


def main():
    logging.basicConfig(level=logging.INFO) 
    conn= redis.Redis(host=HOST, port=PORT, password='') 

    _cache_test(conn,'kafkaTest', kafka_query, CACHE_TTL, HOST, USER, PSWD, DB)

    
if __name__=="__main__":
    main() 