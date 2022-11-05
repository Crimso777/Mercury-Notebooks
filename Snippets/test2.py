from time import sleep
from io import StringIO
import sys
import threading
import queue
import nbformat
import IPython
import os
from stop_thread import stop_thread
def run_command():
#    test.run_cell(nb.cells[n].source)
    test.run_cell("""from time import sleep
for i in range(60):
    print(i)
    sleep(1)
""")
    print("end")

    mystdout.seek(0)



def enqueue_output(out, queue):
    out.seek(0)
    for line in iter(out.readline, b''):
        if len(line) > 0:
            queue.put(line)
#        out.close()

with open("example.ipynb", "r") as f1:           # Open our source file
    nb = nbformat.read(f1, 4)


n = 0

while n < len(nb.cells):
    if nb.cells[n].cell_type == "code":
        break
    else:
        n = n + 1


old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()
#redirected statements
print("Hello wirl")
print("Hello again")


sleep(3)
#print(len(mystdout.getvalue()))
mystdout.seek(0)
print(len(mystdout.readlines()))
test = IPython.InteractiveShell()

t1 = threading.Thread(target=run_command, args=())
t1.daemon = True  # thread dies with the program
t1.start()
stop_thread(t1.ident)
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
    else:
        if len(line) > 2 and line[:3] == 'end':
            exit = True

sys.stdout = old_stdout
test.run_cell("""print("Finished the damn thing.")""")
