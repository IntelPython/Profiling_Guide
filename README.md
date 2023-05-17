# Profiling_Guide
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

All the profilers we are going to discuss here are **Deterministic Profilers** because they capture precise timings of events. Please note that the **Memory Profiler** package also has the **mprof** module that does **statistical profiling**. It is discussed briefly in Memory Profiler notebook. 

This GitHub aims to show different profilers for Python and explain in detail the procedure to profile different workloads with different profilers. Below is the list of all the profilers we will be discussing. Each profiler has a separate folder with a Jupyter Notebook to guide you.  

| Performance Profiler | Lines or Function | Description of Profiler |
| ----------- | ----------- | ----------- |
| **[Memory Profiler](https://github.com/pythonprofilers/memory_profiler)** | lines | <ul><li> It provides memory consumption of each individual line inside the function. </li> <li> Minimal code modification is required.</li><li> It is generally used after identifying **hotspot functions** from a function profiler.</li><li>It does not profile GPU workloads.</li><li>It cannot profile individual threads.</li><li> It does not provide execution time information.</li></ul>|
| **[Line Profiler](https://github.com/pyutils/line_profiler)** | lines | <ul><li> It times the execution of each individual line inside the function. </li> <li> No code modification is required.</li><li> It is generally used after identifying **hotspot functions** from a function profiler.</li><li>It does not profile GPU workloads.</li><li>It cannot profile individual threads.</li><li> It does not provide memory consumption information.</li></ul>|
| **[cProfile](https://docs.python.org/3/library/profile.html)** | function | <ul><li> It times the execution of different functions. </li> <li> No code modification is required.</li><li> It provides a call stack graph and execution time of functions that help identify hotspots.</li><li>It does not profile GPU workloads.</li><li>It cannot profile individual threads.</li><li> It does not provide memory consumption information.</li></ul>|
| **[Profile](https://docs.python.org/3/library/profile.html)** | function | <ul><li> It times the execution of different functions. </li> <li> No code modification is required.</li><li> It provides a call stack graph and execution time of functions that help identify hotspots.</li><li>It does not profile GPU workloads.</li><li>Unlike cProfile, it can profile individual threads but has more overhead compared to cProfile.</li><li> It does not provide memory consumption information</li></ul>|
| **[FunctionTrace](https://functiontrace.com/)** | function | <ul><li> It times the execution of different functions but only supports Python>3.5. </li> <li> No code modification is required.</li><li> It provides stack charts, flame graphs, and call trees that help identify hotspots.</li><li>It does not profile GPU workloads.</li><li>It can profile individual threads.</li><li> It does not provide memory consumption information.</li><li>Profiling results can be shared very easily through browser.</li></ul>|
| **[Scalene](https://github.com/plasma-umass/scalene)** | function and line | <ul><li> It times the execution of different functions and lines but only supports Python>3.7. </li> <li> No code modification is required.</li><li> It does not provide call stack information.</li><li>It can profile GPU workloads.</li><li>It can profile individual threads.</li><li> It provides memory consumption information.</li><li>Profiling results can be shared very easily through browser.</li><li>It has integration to GPT3, when activated it can suggest changes to optimize code</li></ul>|
| **[VTune](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html)** | function and line | <ul><li> It times the execution of different functions and lines and supports other languages like C, Java, etc. </li> <li> Minimal code modification is required. It also provides a GUI that is easy to use.</li><li> It provides call stack information, flame graph, and hardware utilization.</li><li>It can profile GPU workloads.</li><li>It can profile individual threads.</li><li> It provides memory consumption information.</li><li>Profiling results can be shared very easily through web browser interface.</li><li>It also gives low-level C, C++ functions that can be potential hotspots.</li><li> The profiling overhead is high as compared to other profilers.</li></ul>|



We will also use the following Intel AI Reference Kit in our profiling examples:
- **Scikit-Learn Intelligent Indexing for Incoming Correspondence – [Ref Kit](https://github.com/oneapi-src/intelligent-indexing)**

![image](https://user-images.githubusercontent.com/113541458/226619059-f5ea3ec5-a297-43d4-a6d4-c173265379e2.png)

**Follow the steps mentioned in the [intelligent-Indexing Ref Kit GitHub ReadMe](https://github.com/oneapi-src/intelligent-indexing) to setup the environments accordingly.** <br>
The process involves
- Setting up a virtual environment for both stock and Intel®-accelerated machine learning packages
- Preprocessing data using Pandas*/Intel® Distribution of Modin and NLTK
- Training an NLP model for text classification using Scikit-Learn*/Intel® Extension for Scikit-Learn*