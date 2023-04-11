import time
import random
from line_profiler import LineProfiler


def very_slow_random_generator():
    time.sleep(5)
    arr = [random.randint(1,100) for i in range(100000)]
    return sum(arr) / len(arr)

def slow_random_generator():
    time.sleep(2)
    arr = [random.randint(1,100) for i in range(100000)]
    return sum(arr) / len(arr)
    
def main_func():
    result = slow_random_generator()
    print(result)

    result = very_slow_random_generator()
    print(result)



lprofiler = LineProfiler()
lprofiler.add_function(very_slow_random_generator)
lprofiler.add_function(slow_random_generator)
lp_wrapper = lprofiler(main_func)
lp_wrapper()
lprofiler.print_stats()