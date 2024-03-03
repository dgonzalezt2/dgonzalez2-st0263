# entrypoint.py

import threading
import main
import grpc

def run_script1():
    main.main()

def run_script2():
    grpc.main()

thread1 = threading.Thread(target=run_script1)
thread2 = threading.Thread(target=run_script2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
