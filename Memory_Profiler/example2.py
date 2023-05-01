from memory_profiler import profile
import random
fp = open("example_report.log", "w+")
@profile(precision=4,stream=fp)
def random_number_generator():
    arr1 = [random.randint(1,10) for i in range(100000)]
    arr2 = [random.randint(1,10) for i in range(100000)]
    arr3 = [arr1[i]+arr2[i] for i in range(100000)]
    del arr1
    del arr2
    tot = sum(arr3)
    del arr3
    print(tot)

if __name__ == "__main__":
    random_number_generator()