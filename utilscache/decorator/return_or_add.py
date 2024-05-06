from asyncio import iscoroutinefunction
from typing import Callable
from functools import wraps


def return_or_add(
        cache_dict: dict,
        cache_key_func: Callable = lambda args, kwargs: f"{args}-{kwargs}",
        cache_value_func: Callable = lambda args, kwargs, result: result,
        return_value_from_cache_func: Callable = lambda value: value,
        is_cache_active: bool = True,
):
    def decorator(function):
        if is_cache_active:
            if iscoroutinefunction(function):
                @wraps(function)
                async def wrapper(*args, **kwargs):
                    key = cache_key_func(args, kwargs)
                    if key in cache_dict:
                        return return_value_from_cache_func(cache_dict[key])

                    result = await function(*args, **kwargs)

                    cache_dict[key] = cache_value_func(args, kwargs, result)
                    return result

            else:
                @wraps(function)
                def wrapper(*args, **kwargs):
                    key = cache_key_func(args, kwargs)
                    if key in cache_dict:
                        return return_value_from_cache_func(cache_dict[key])

                    result = function(*args, **kwargs)

                    cache_dict[key] = cache_value_func(args, kwargs, result)
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
