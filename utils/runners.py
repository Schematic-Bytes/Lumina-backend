import asyncio
from typing import Any, Callable, TypeVar

T = TypeVar('T')


def run_in_executor(func: Callable[..., T], *args: Any, **kwargs: Any) -> Callable[..., asyncio.Future[T]]:
    """
    Decorator function to run a normal runing function in an executor.
    """

    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        return await asyncio.get_event_loop().run_in_executor(None, func, *args, **kwargs)

    return wrapper
