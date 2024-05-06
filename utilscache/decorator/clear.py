from functools import wraps
from asyncio import iscoroutinefunction


def clear(
        cache_dict: dict,
        is_cache_active: bool = True,
):
    def decorator(function):
        if is_cache_active:
            if iscoroutinefunction(function):
                @wraps(function)
                async def wrapper(*args, **kwargs):
                    result = await function(*args, **kwargs)
                    cache_dict.clear()
                    return result

            else:
                @wraps(function)
                def wrapper(*args, **kwargs):
                    result = function(*args, **kwargs)
                    cache_dict.clear()
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
