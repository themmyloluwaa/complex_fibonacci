import redis
import os

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

redisClient = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0,)


def fib(index):
    if(index < 2):
        return 1
    return fib(index - 1) + fib(index - 2)


def sub(name: 'str'):
    pubsub = redisClient.pubsub()
    pubsub.subscribe('insert')
    for message in pubsub.listen():
        if message.get('type') == 'message':
            redisClient.hset('values', fib(message.get('value')))
