import nbformat

with open("example.ipynb","r") as f1:           # Open our source file
#    print(nbformat.read(f1, 4).cells[0]["source"])
    print(nbformat.read(f1, 4).metadata)
