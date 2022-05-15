import os
import memcache


CACHE_HOST = os.environ.get('CACHE_HOST', None)

if CACHE_HOST:
    client = memcache.Client([(CACHE_HOST, 11211)], debug=0)


def get_by_key(key):
    return client.get(key)


def set_entry(key, value):
    client.set(key, value, time=60)
    return True
