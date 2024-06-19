#!/usr/bin/env python3
"""
Web cache and tracker using Redis.
"""

import redis
import requests
from typing import Callable


class Cache:
    def __init__(self):
        """Initialize the Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count the number of calls to a method.

        Args:
            method (Callable): The method to be decorated.

        Returns:
            Callable: The wrapped method.
        """
        def wrapper(self, *args, **kwargs):
            """Wrapper function to count calls and call the original method."""
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper


def get_page(url: str) -> str:
    """
    Obtain the HTML content of a URL and cache it with an expiration time.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    cache = redis.Redis()
    cache_key = f"cache:{url}"
    count_key = f"count:{url}"

    # Increment the access count for the URL
    cache.incr(count_key)

    # Try to get the cached content
    cached_content = cache.get(cache_key)
    if cached_content:
        return cached_content.decode('utf-8')

    # Fetch the content from the URL
    response = requests.get(url)
    content = response.text

    # Cache the content with an expiration time of 10 seconds
    cache.setex(cache_key, 10, content)

    return content


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(get_page(url))
