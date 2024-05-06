from functools import wraps
from asyncio import iscoroutinefunction
from typing import Callable


def delete(
        cache_dict: dict,
        cache_key_func: Callable = lambda args, kwargs, result: f"{args}-{kwargs}-{result}",
        is_cache_active: bool = True,
):
    def decorator(function):
        if is_cache_active:
            if iscoroutinefunction(function):
                @wraps(function)
                async def wrapper(*args, **kwargs):
                    result = await function(*args, **kwargs)
                    key = cache_key_func(args, kwargs, result)
                    if key in cache_dict:
                        del cache_dict[key]
                    return result

            else:
                @wraps(function)
                def wrapper(*args, **kwargs):
                    result = function(*args, **kwargs)
                    key = cache_key_func(args, kwargs, result)
                    if key in cache_dict:
                        del cache_dict[key]
                    return result

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
