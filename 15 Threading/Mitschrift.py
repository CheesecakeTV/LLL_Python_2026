import time
import threading

mein_lock = threading.Semaphore(2)
#meine_barrier = threading.Barrier(4)

def print_schlecht(text: str):

    # meine_barrier.wait()
    # meine_barrier.reset()

    with mein_lock:
        for i in text:
            print(i, end="")
            time.sleep(0.01)

        print()

def print_cyclic(text: str = "Hallo"):
    for i in range(3):
        print_schlecht(text)
        time.sleep(1)

thread1 = threading.Thread(target=print_cyclic, args=("Thread1", ))#, daemon=True)
thread2 = threading.Thread(target=print_cyclic, kwargs={"text":"Thread2"})#, daemon=True)
threading.Thread(target=print_cyclic).start()
threading.Thread(target=print_cyclic).start()
threading.Thread(target=print_cyclic).start()
threading.Thread(target=print_cyclic).start()

thread1.start()
thread2.start()

#print(thread1.is_alive())
#thread1.join()

print_schlecht("Ende")
