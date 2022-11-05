import nbformat

with open("example.ipynb", "r") as f1:           # Open our source file
    nb = nbformat.read(f1, 4)

new_cell = nbformat.v4.new_markdown_cell(source='#HELLO WORLD!')

nb.cells.insert(0, new_cell)
with open("output.ipynb", "w") as f1:           # Open our source file
    nbformat.write(nb, f1, version = nbformat.current_nbformat)
