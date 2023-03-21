# Profiliing_Guide
Profilers help to identify performance problems. These are tools designed to give the metrics to find the slowest parts of the code so that we can optimize what really matters. Profilers can gather a wide variety of metrics: wall time, CPU time, network or memory consumption, I/O operations, etc.
<br>
Profilers can answer questions like,
- How many times is each method in my code called? 
- How long does each of these methods take?
- How much memory does the method consume?

<br>
There are different types of profilers

- **Deterministic Profiling:** Deterministic profilers execute trace functions at various points of interest (function call, function return) and record precise timings of these events. It means the code runs slower under profiling. Its use in production systems is often impractical.


- **Statistical profiling:**  Instead of tracking every event (call to every function), statistical profilers interrupt applications periodically and collect samples of the execution state (call stack snapshots). The call stacks are then analyzed to determine the execution time of different parts of the application. This method is less accurate, but it also reduces the overhead.

<br>

We will begin profiling with a Starter Kit:
- **Scikit-Learn Intelligent Indexing for Incoming Correspondence – [LINK](https://github.com/oneapi-src/intelligent-indexing)**

![image.png](attachment:53b30e68-ce2d-4739-8be5-46951d87ad19.png)

Follow the steps mentioned in the [github link](https://github.com/oneapi-src/intelligent-indexing) to setup the environment.
The process involves
- Setting up a virtual environment for stock/Intel®-accelerated ML
- Preprocessing data using Pandas/Intel® oneAPI Modin and NLTK
- Training an NLP model for text classification using scikit-learn/Intel® oneAPI scikit-learn extension
- Predicting from the trained model on new data using scikit-learn/Intel® oneAPI scikit-learn extension.

Here we'll discuss profiling Tools Available for Python
- [Vtune](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html)
- [Cprofile (function profiler)](https://docs.python.org/3/library/profile.html) 
- [Profile (function profiler)](https://docs.python.org/3/library/profile.html)
- [line_profiler (line profiler)](https://github.com/pyutils/line_profiler)
- [memory_profiler (line)](https://github.com/pythonprofilers/memory_profiler)
- [Scalene (both line and function profiler)](https://github.com/plasma-umass/scalene)
- [Function-Trace (function profiler)](https://functiontrace.com/)

%lprun: Run code with the line-by-line profiler <br>
%memit: Measure the memory use of a single statement <br>
%mprun: Run code with the line-by-line memory profiler <br>
