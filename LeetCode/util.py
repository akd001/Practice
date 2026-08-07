import time
from functools import wraps
from typing import Callable, Any

def time_it(func: Callable[..., Any]) -> Callable[..., Any]:
    """A utility decorator that logs the execution time of a function."""
    @wraps(func)  # Keeps the original function's name and docstring
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"[INFO] '{func.__name__}' took {execution_time:.6f} seconds to execute.")
        
        return result
    return wrapper

def sort_array(arr: list[int]) -> list[int]:
    """Sorts an array in ascending order."""
    return sorted(arr)