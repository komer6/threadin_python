import threading
import time

def background_task():
    while True:
        print("Background task running...")
        time.sleep(2)

def main_task():
    for i in range(5):
        print(f"Main task iteration {i+1}")
        time.sleep(1)

# Create a background thread
daemon_thread = threading.Thread(target=background_task)
daemon_thread.daemon = True  # Mark it as a daemon thread
daemon_thread.start()

# Run main task
main_task()

print("Main task finished. Daemon thread will be killed automatically.")
