import time
import numpy as np
import cProfile

def very_slow_random_generator():   ##Function to generate random number
    time.sleep(5)                   ##Added 5secs sleep to simulate very slow generator
    arr1 = np.random.randint(1,100, size=(1000,1000))
    avg = arr1.mean()
    return avg


def slow_random_generator():       ##Function to generate random number
    time.sleep(2)                  ##Added 2secs sleep to simulate very slow generator
    arr1 = np.random.randint(1,100, size=(1000,1000))
    avg = arr1.mean()
    return avg

prof = cProfile.Profile()

def main_func():
    prof.enable()
    avg1 = slow_random_generator()
    avg2 = very_slow_random_generator()
    prof.disable()
    print("Averages: {:.3f}, {:.3f}".format(avg1,avg2))

if __name__ == '__main__':
    main_func()
    prof.print_stats()