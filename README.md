# mp_wrapper
A simple wrapper for python multiprocessing functions
------------------------------------------------------

The mp_wrapper function receives a function and a list, and runs this function in parallel on every member of the list.

To use, just add to your script:  

```from mp_wrapper import *   
results = mp_wrapper(function_to_run, list_to_iterate)```
