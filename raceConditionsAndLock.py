import threading

# Race Condition Example (BAD)
def race_condition_example():
    counter = 0

    def increment():
        nonlocal counter
        for _ in range(100000):
            counter += 1

    thread1 = threading.Thread(target=increment)
    thread2 = threading.Thread(target=increment)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"[Race Condition] Final counter value (should be 200000): {counter}")

# Lock Example (GOOD)
def lock_example():
    counter = 0
    lock = threading.Lock()

    def safe_increment():
        nonlocal counter
        for _ in range(100000):
            with lock:
                counter += 1

    thread1 = threading.Thread(target=safe_increment)
    thread2 = threading.Thread(target=safe_increment)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"[Lock Used] Final counter value: {counter}")

# Run both examples separately
if __name__ == "__main__":
    race_condition_example()
    lock_example()
