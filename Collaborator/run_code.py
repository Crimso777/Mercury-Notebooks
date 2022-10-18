import IPython
import nbformat

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

test.run_cell(nb.cells[n].source)
test.run_cell("i = 1")
test1.run_cell("i = 2")
test.run_cell("print(i)")
