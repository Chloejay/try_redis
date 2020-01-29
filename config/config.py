import redis 
import logging 
import time 
from pprint import pprint 
import traceback 
import pymysql 
import json 


CACHE_TTL= 60 *10
HOST='localhost'
USER='root'
PSWD='password'
DB='kafka_test'
PORT= 6379 
kafka_query= '''select favorite_color from kafkav1'''

