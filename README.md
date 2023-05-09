# Profiling_Guide
Profilers help to identify performance problems. These are tools designed to give the metrics to find the slowest parts of the code so that we can optimize what really matters. Profilers can gather a wide variety of metrics: wall time, CPU time, network or memory consumption, I/O operations, etc.
<br>
Profilers can answer questions like,
- How many times is each method in my code called? 
- How long does each of these methods take?
- How much memory does the method consume?

<br>
**is this relevant to this github? confusing since this isn't mentioned in the actual profiler descriptions**
There are different types of profilers

- **Deterministic Profiling:** Deterministic profilers execute trace functions at various points of interest (function call, function return) and record precise timings of these events. It means the code runs slower under profiling. Its use in production systems is often impractical.


- **Statistical profiling:**  Instead of tracking every event (call to every function), statistical profilers interrupt applications periodically and collect samples of the execution state (call stack snapshots). The call stacks are then analyzed to determine the execution time of different parts of the application. This method is less accurate, but it also reduces the overhead.

<br>

**add information on the purpose of this GitHub**
**please go into detail about each of the different profilers - what are they? what is the difference between them? would be good to have a table describing this - need this to guide users to correct part of GitHub**
**example table**

| Performance Profiler Type      | Description of Profiler |
| ----------- | ----------- |
| Line Profiler      | Description of Line Profiler including benefits and differences to other profilers described     |
| Memory Profiler  | memory profiler description.... do same with other profilers        |

**add call to action - something like try out the profilers you are interested in accordingly....**

<br>
We will also use the following Intel AI Reference Kit in our profiling examples:
- **Scikit-Learn Intelligent Indexing for Incoming Correspondence – [Ref Kit](https://github.com/oneapi-src/intelligent-indexing)**

![image](https://user-images.githubusercontent.com/113541458/226619059-f5ea3ec5-a297-43d4-a6d4-c173265379e2.png)

**Follow the steps mentioned in the [Ref Kit GitHub ReadMe](https://github.com/oneapi-src/intelligent-indexing) to setup the environments accordingly.** <br>
The process involves
- Setting up a virtual environment for stock/Intel®-accelerated ML
- Preprocessing data using Pandas/Intel® Distribution of Modin and NLTK
- Training an NLP model for text classification using scikit-learn/Intel® Extension for Scikit-Learn*
- Predicting from the trained model on new data using scikit-learn/Intel® Extension for Scikit-Learn*.

This guide utilizes the following profiling tools available for Python:
- **[Vtune (both line and function profiler)](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html)**
- **[Cprofile (function profiler)](https://docs.python.org/3/library/profile.html)** 
- **[Profile (function profiler)](https://docs.python.org/3/library/profile.html)**
- **[line_profiler (line profiler)](https://github.com/pyutils/line_profiler)**
- **[memory_profiler (line)](https://github.com/pythonprofilers/memory_profiler)**
- **[Scalene (both line and function profiler)](https://github.com/plasma-umass/scalene)**
- **[FunctionTrace (function profiler)](https://functiontrace.com/)**

