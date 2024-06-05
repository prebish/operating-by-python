import time
import threading

# SYSCALL.H: Syscall numbers and prototypes
SYSCALL_PRINT = 0
SYSCALL_TIME = 1

# USYS.S: Low-level syscall interface (simulated in Python)
def low_level_syscall(syscall_number, *args):
    # This function would actually use assembly in a real OS
    return syscall(syscall_number, *args)

# SYSPROC.C: Kernel functions
def kernel_print(message):
    print(f"Kernel: {message}")

def kernel_time():
    return time.time()

# SYSPROC.C: Syscall table
syscall_table = {
    SYSCALL_PRINT: kernel_print,
    SYSCALL_TIME: kernel_time
}

# SYSCALL.C: Syscall interface
def syscall(syscall_number, *args):
    # Transition to Kernel Mode
    print(f"Transition: Switching to Kernel Mode for syscall {syscall_number}")
    
    # Simulate the kernel's handling of the syscall
    if syscall_number in syscall_table:
        result = syscall_table[syscall_number](*args)
        
        # Return to User Mode
        print("Return: Switching back to User Mode")
        return result
    else:
        raise ValueError("Invalid syscall number")

# USER.H: User program interface
def user_program():
    print("User program starting...")
    
    # Request syscall to print a message
    low_level_syscall(SYSCALL_PRINT, "Hello from user program")
    
    # Request syscall to get current time
    current_time = low_level_syscall(SYSCALL_TIME)
    print(f"User program received time: {current_time}")

# MAIN.C: Main execution
def main():
    user_program()

if __name__ == "__main__": 
    main()
