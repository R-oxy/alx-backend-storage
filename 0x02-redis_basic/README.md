# 0x02. Redis Basic

## Back-end | Redis

## Resources
Read or watch:
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)
- [Redis commands](https://redis.io/commands)
- [Redis python client](https://pypi.org/project/redis/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)

## Learning Objectives
- Learn how to use Redis for basic operations
- Learn how to use Redis as a simple cache

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should use the pycodestyle style (version 2.5)
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions and methods should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method
- All functions and coroutines must be type-annotated

## Install Redis on Ubuntu 18.04
```sh
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Use Redis in a Container
Redis server is stopped by default. When starting a container, start it with:
```sh
service redis-server start
```

## Tasks

### 0. Writing Strings to Redis
Create a `Cache` class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.

Create a `store` method that takes a `data` argument and returns a string. The method should generate a random key (e.g., using `uuid`), store the input data in Redis using the random key, and return the key.

Type-annotate `store` correctly. Remember that `data` can be a `str`, `bytes`, `int`, or `float`.

**File:** `exercise.py`
```python
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
```

### 1. Reading from Redis and Recovering Original Type
Create a `get` method that takes a key string argument and an optional `Callable` argument named `fn`. This callable will be used to convert the data back to the desired format.

Remember to conserve the original `Redis.get` behavior if the key does not exist.

Also, implement 2 new methods: `get_str` and `get_int` that will automatically parameterize `Cache.get` with the correct conversion function.

**File:** `exercise.py`

### 2. Incrementing Values
Familiarize yourself with the `INCR` command and its Python equivalent.

Implement a system to count how many times methods of the `Cache` class are called.

Above `Cache`, define a `count_calls` decorator that takes a single method `Callable` argument and returns a `Callable`.

As a key, use the qualified name of the method using the `__qualname__` dunder method.

Create and return a function that increments the count for that key every time the method is called and returns the value returned by the original method.

Decorate `Cache.store` with `count_calls`.

**File:** `exercise.py`
```python
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
```

### 3. Storing Lists
Familiarize yourself with Redis commands `RPUSH`, `LPUSH`, `LRANGE`, etc.

Define a `call_history` decorator to store the history of inputs and outputs for a particular function.

Every time the original function is called, add its input parameters to one list in Redis and store its output in another list.

In `call_history`, use the decorated function’s qualified name and append `":inputs"` and `":outputs"` to create input and output list keys, respectively.

`call_history` has a single parameter named `method` that is a `Callable` and returns a `Callable`.

In the new function that the decorator will return, use `rpush` to append the input arguments. Redis can only store strings, bytes, and numbers, so use `str(args)` to normalize. Ignore potential kwargs for now.

Execute the wrapped function to retrieve the output. Store the output using `rpush` in the "...:outputs" list, then return the output.

Decorate `Cache.store` with `call_history`.

**File:** `exercise.py`
```python
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))
```

### 4. Retrieving Lists
Implement a `replay` function to display the history of calls of a particular function.

Use keys generated in previous tasks to generate the following output:
```python
>>> cache = Cache()
>>> cache.store("foo")
>>> cache.store("bar")
>>> cache.store(42)
>>> replay(cache.store)
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
```
Tip: use `lrange` and `zip` to loop over inputs and outputs.

**File:** `exercise.py`

### 5. Implementing an Expiring Web Cache and Tracker
Implement a `get_page` function (prototype: `def get_page(url: str) -> str:`). The core of the function is very simple. It uses the `requests` module to obtain the HTML content of a particular URL and returns it.

Start in a new file named `web.py` and do not reuse the code written in `exercise.py`.

Inside `get_page`, track how many times a particular URL was accessed in the key `count:{url}` and cache the result with an expiration time of 10 seconds.

Tip: Use `http://slowwly.robertomurray.co.uk` to simulate a slow response and test your caching.

Bonus: implement this use case with decorators.

**File:** `web.py`