import multiprocessing as mp
from time import sleep


# Define an output queue
OUTPUT_QUEUE = mp.Queue()


def mp_wrapper(func, list_name, sleep_between_jobs=0, output=OUTPUT_QUEUE):
    """A wrapper function for using the multiprocessing package.
    The function receives a function and a running each member of the list in parallel.
    returns a list of results."""
    processes = [mp.Process(target=func, args=(x, output)) for x in list_name]
    # Run processes
    for p in processes:
        p.start()
        sleep(sleep_between_jobs)
    # Exit the completed processes
    for p in processes:
        p.join()
    return [output.get() for p in processes]
