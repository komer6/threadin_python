import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1.5)

# Create threads
number_thread = threading.Thread(target=print_numbers)
letter_thread = threading.Thread(target=print_letters)

# Start threads
number_thread.start()
letter_thread.start()

# Wait for both threads to finish
number_thread.join()
letter_thread.join()

print("Both threads have finished.")
