import threading
import time

def greet(name, delay):
    for i in range(3):
        print(f"Hello {name}, message {i+1}")
        time.sleep(delay)

# Create a thread with arguments
thread = threading.Thread(target=greet, args=("Omer", 1.5))
thread.start()

# Main program continues
print("Main program continues running while thread works...")

# Wait for the thread to finish
thread.join()

print("Thread has finished.")
