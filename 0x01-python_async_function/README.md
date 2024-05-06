Asynchronous Python Project
This project is designed to help you learn and practice asynchronous programming in Python 3. It includes several tasks that cover different aspects of working with asynchronous code. By completing these tasks, you will gain a solid understanding of asynchronous programming concepts and how to apply them in Python.

Task 0: The Basics of Async
In the file 0-basic_async_syntax.py, you will find an asynchronous coroutine called wait_random. This coroutine takes an integer argument max_delay (default value: 10) and waits for a random delay between 0 and max_delay seconds (inclusive). Eventually, it returns the delay. Make sure to use the random module to generate random values.

Task 1: Executing Multiple Coroutines Concurrently
In the file 1-concurrent_coroutines.py, you need to import the wait_random coroutine from the previous file. Your task is to write an async function called wait_n that takes two integer arguments: n and max_delay. Inside this function, you should spawn wait_random coroutine n times with the specified max_delay. The function should return a list of all the delays (float values) in ascending order, without using the sort() method due to concurrency.

Task 2: Measuring the Runtime
In the file 2-measure_runtime.py, you should import the wait_n function from the previous file. Your goal is to create a function called measure_time that takes two integer arguments: n and max_delay. This function measures the total execution time for wait_n(n, max_delay) and returns the average time per task (total_time / n) as a float. To measure the elapsed time, use the time module.

Task 3: Creating an asyncio.Task
In the file 3-tasks.py, import the wait_random coroutine from 0-basic_async_syntax.py. Write a regular function (not an async function) called task_wait_random that takes an integer argument max_delay. This function should return an asyncio.Task object that represents the execution of the wait_random(max_delay) coroutine.

Task 4: Creating a Task-Based Version of wait_n
In the file 4-tasks.py, take the code from the wait_n function in 1-concurrent_coroutines.py and modify it to create a new function called task_wait_n. This function should be almost identical to wait_n, but instead of calling the wait_random coroutine directly, it should call the task_wait_random function from Task 3.
