import threading
import time

# Function using args (tuple)
def thread_with_args():
    def greet(name, delay):
        for i in range(3):
            print(f"[Args] Hello {name}, message {i+1}")
            time.sleep(delay)

    thread = threading.Thread(target=greet, args=("Omer", 1.5))
    thread.start()

    print("[Args] Main program continues running while thread works...")
    thread.join()
    print("[Args] Thread has finished.")

# Function using kwargs (dict)
def thread_with_kwargs():
    def greet(name, delay):
        for i in range(3):
            print(f"[Kwargs] Hello {name}, message {i+1}")
            time.sleep(delay)

    thread = threading.Thread(target=greet, kwargs={"name": "Alex", "delay": 1})
    thread.start()

    print("[Kwargs] Main program continues running while thread works...")
    thread.join()
    print("[Kwargs] Thread has finished.")

# Run both examples
if __name__ == "__main__":
    thread_with_args()
    print("\n---\n")
    thread_with_kwargs()
