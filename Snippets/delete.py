import nbformat

with open("example.ipynb", "r") as f1:           # Open our source file
    nb = nbformat.read(f1, 4)

popped = nb.cells.pop(0)
#print(popped)

with open("output.ipynb", "w") as f1:           # Open our source file
    nbformat.write(nb, f1)
