from time import sleep
from io import StringIO
import sys
import threading
import queue
def enqueue_output(out, queue):
    out.seek(0)
    for line in iter(out.readline, b''):
        if len(line) > 0:
            queue.put(line)
#        out.close()


old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()
#redirected statements
print("Hello wirl")
print("Hello again")

sys.stdout = old_stdout

sleep(3)
#print(len(mystdout.getvalue()))
mystdout.seek(0)
print(len(mystdout.readlines()))



q = queue.Queue()
t = threading.Thread(target=enqueue_output, args=(mystdout, q))
t.daemon = True  # thread dies with the program
t.start()

exit = False
while not exit:
    # read line without blocking
    try:
        line = q.get_nowait()  # or q.get(timeout=.1)
        sys.stdout = old_stdout
        print(line)
        sys.stdout = mystdout 

    except queue.Empty:
        #      print('no output yet')
        pass

mystdout.close()
