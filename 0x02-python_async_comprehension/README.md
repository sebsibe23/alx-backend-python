0x02. Python - Async Comprehension
This repository contains the solutions to the tasks for the "0x02. Python - Async Comprehension" project in the ALX Backend Python curriculum.

Learning Objectives
By the end of this project, you should be able to:

Explain how to write an asynchronous generator
Demonstrate the usage of async comprehensions
Understand how to type-annotate generators
Requirements
Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All files should end with a new line
The first line of all files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the project folder, is mandatory
Code should follow the pycodestyle style (version 2.5.x)
The length of your files will be tested using wc
All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All functions should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
Documentation should be meaningful and provide a clear explanation of the purpose of the module, class, or method (length will be verified)
All functions and coroutines must be type-annotated
Tasks
0. Async Generator
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait for 1 second, then yield a random number between 0 and 10 using the random module.

Example:

python
Copy
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
1. Async Comprehensions
Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehension over async_generator, and then return the 10 random numbers.

Example:

python
Copy
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())
2. Run time for four parallel comprehensions
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Example:

python
Copy
#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await measure_runtime()

print(
    asyncio.run(main())
)
Repository
GitHub repository: alx-backend-python
Directory: 0x02-python_async_comprehension
Files:
0-async_generator.py
1-async_comprehension.py
2-measure_runtime.py
Note: Replace "username" with your GitHub username in the repository URL.

Author
sebsibe solomon
GitHub: @sebsibe23
