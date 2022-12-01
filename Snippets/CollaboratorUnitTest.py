from Collaborator.colab import notebook

nb = notebook("example")
print(nb.read_code_cell(3))
print(nb.read_text_cell(-1))
print(nb.read_code_cell(-100))

input()
nb.insert_text_cell("Hello Increment!", 0)
print(nb.read_cell(0))
print(nb.read_text_cell(0))
nb.insert_text_cell("Hello Again!", 0)
print(nb.read_text_cell(1))
input()
print(nb.read_cell(0))
nb.delete_cell(0)
print(nb.read_cell(0))
nb.delete_cell(0)
print(nb.read_cell(0))

nb.save_to_file("output")
input()
nb.insert_code_cell("""print("Hello Coding!")""", 0)
print(nb.run_cell(0))