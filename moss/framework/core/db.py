#! /usr/bin/env python

import redis
import json

def log_operation_to_redis_database(key, value):
    redis_connection = redis.StrictRedis()
    redis_connection.execute_command('JSON.SET', str(key), '.', json.dumps(value))
