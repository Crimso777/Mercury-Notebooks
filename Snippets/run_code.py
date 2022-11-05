from io import StringIO 
from IPython.utils.capture import CapturedIO
import sys
import IPython
import nbformat
import subprocess
import threading
import queue
import multiprocessing as mp
from time import sleep

with open("example.ipynb", "r") as f1:           # Open our source file
    nb = nbformat.read(f1, 4)


n = 0

while n < len(nb.cells):
    if nb.cells[n].cell_type == "code":
        break
    else:
        n = n + 1
test = IPython.InteractiveShell()
test1 = IPython.InteractiveShell()

from IPython.utils import io
with io.capture_output() as captured:
    print(1)
    sleep(10)
    print(2)
    sleep(1)
#    test.run_cell(nb.cells[n].source)
    #   test.run_cell("print(i)")
print(captured)

class Tee(StringIO):
    def __init__(self, initial_value='', newline='\n', stream=None):
        self.stream = stream
        super().__init__(initial_value, newline)
    
    def write(self, data):
        if self.stream is not None:
            self.stream.write(data)
        
        super().write(data)

class capture_and_print_output(object):
    stdout = True
    stderr = True
    display = True
    
    def __init__(self, stdout=True, stderr=True, display=True):
        self.stdout = stdout
        self.stderr = stderr
        self.display = display
        self.shell = None
    
    def __enter__(self):
        from IPython.core.getipython import get_ipython
        from IPython.core.displaypub import CapturingDisplayPublisher
        from IPython.core.displayhook import CapturingDisplayHook
        
        self.sys_stdout = sys.stdout
        self.sys_stderr = sys.stderr
        
        if self.display:
            self.shell = get_ipython()
            if self.shell is None:
                self.save_display_pub = None
                self.display = False
        
        stdout = stderr = outputs = None
        if self.stdout:
            stdout = sys.stdout = Tee(stream=sys.stdout)
        if self.stderr:
            stderr = sys.stderr = Tee(stream=sys.stderr)
        if self.display:
            self.save_display_pub = self.shell.display_pub
            self.shell.display_pub = CapturingDisplayPublisher()
            outputs = self.shell.display_pub.outputs
            self.save_display_hook = sys.displayhook
            sys.displayhook = CapturingDisplayHook(shell=self.shell,
                                                   outputs=outputs)
        
        return CapturedIO(stdout, stderr, outputs)
    
    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.sys_stdout
        sys.stderr = self.sys_stderr
        if self.display and self.shell:
            self.shell.display_pub = self.save_display_pub
            sys.displayhook = self.save_display_hook

with capture_and_print_output() as captured:
    print(1)
    sleep(10)
    print(2)
    sleep(1)
