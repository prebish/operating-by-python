import time
import threading

def START():
    return time.perf_counter()

def END(start_time):
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    return elapsed

def sep():
    print(f"-----------------------------")

counter_lock = threading.Lock()  # Define the lock globally to synchronize access to shared resources

def increment():
    """
    Function to demonstrate a simple non-atomic counter increment.
    """
    print("Function: increment()")
    start = START(); time.sleep(1)  # Start timing and include a delay to simulate work
    c = 0
    print(f"c: {c}")  # Show initial count
    c += 1
    print(f"c after increment: {c}")  # Increment value

    elapsed = END(start) - 1  # Calculate elapsed time minus the initial sleep
    print(f"\033[92mTime: {elapsed:.4f}s\033[0m\n")  # Print elapsed time in green

def increment_atomic():
    """
    Function to demonstrate an atomic counter increment using a lock.
    
    The lock ensures that only one thread can execute the critical section
    at a time, preventing race conditions and ensuring data consistency.
    """
    print("Function: increment_atomic()")
    start = START()
    
    global counter_lock  # Declare the global lock to use it within this function
    
    # Acquire the lock before entering the critical section
    counter_lock.acquire()  # This call blocks if the lock is already held by another thread
    try:
        c = 0
        print(f"c: {c}")  # Show initial count
        c += 1
        print(f"c after increment: {c}")  # Increment value
    finally:
        # Release the lock after exiting the critical section
        counter_lock.release()  # This allows other threads to acquire the lock and proceed
        # Ensuring the lock is always released, even if an error occurs, is crucial for avoiding deadlocks

    elapsed = END(start)  # Calculate elapsed time
    print(f"\033[92mTime taken: {elapsed:.4f}s\033[0m\n")  # Print elapsed time in green

def main():
    sep()
    increment()  # Call the non-atomic increment function
    sep()
    increment_atomic()  # Call the atomic increment function
    sep()

if __name__ == "__main__": 
    main()
