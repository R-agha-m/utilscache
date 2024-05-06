from functools import wraps
from typing import Callable
from asyncio import iscoroutinefunction


def add(
        cache_dict: dict,
        cache_key_func: Callable = lambda args, kwargs, result: f"{args}-{kwargs}-{result}",
        cache_value_func: Callable = lambda args, kwargs, result: result,
        is_cache_active: bool = True,
):
    def decorator(function):
        if is_cache_active:
            if iscoroutinefunction(function):
                @wraps(function)
                async def wrapper(*args, **kwargs):
                    result = await function(*args, **kwargs)
                    key = cache_key_func(args, kwargs, result)
                    value = cache_value_func(args, kwargs, result)
                    cache_dict[key] = value
                    return value
            else:
                @wraps(function)
                def wrapper(*args, **kwargs):
                    result = function(*args, **kwargs)
                    key = cache_key_func(args, kwargs, result)
                    value = cache_value_func(args, kwargs, result)
                    cache_dict[key] = value
                    return value

        else:
            if iscoroutinefunction(function):
                @wraps(function)
                async def wrapper(*args, **kwargs):
                    return await function(*args, **kwargs)

            else:
                @wraps(function)
                def wrapper(*args, **kwargs):
                    return function(*args, **kwargs)

        return wrapper

    return decorator
