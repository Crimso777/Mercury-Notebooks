import nbformat
import IPython
import sys
from io import StringIO
from IPython.utils import io
from bisect import bisect
class notebook:
   def __init__(self, path, version = 4):
      self.runtime = IPython.InteractiveShell()

      with open(path+".ipynb", "r") as f1:           # Open our source file
         self.json = nbformat.read(f1, 4)
      self.total = len(self.json.cells)
      self.text_count = 0
      self.code_count = 0
      self.code_cells = []
      self.text_cells = []
      i = 0
      while i < self.total:
         if self.json.cells[i].cell_type == "markdown":
            self.text_cells.append(i)
            self.text_count = self.text_count + 1
         if self.json.cells[i].cell_type == "code":
            self.code_cells.append(i)
            self.code_count = self.code_count + 1
         i = i + 1
      

   def read_code_cell(self, i):
      if abs(i) >= self.code_count:
         return "Index out of range"
  
      return self.json.cells[self.code_cells[i]].source 
   def read_text_cell(self, i):
      if abs(i) >= self.text_count:
         return "Index out of range"
      return self.json.cells[self.text_cells[i]].source

   def read_cell(self, i):
      if abs(i) >= self.total:
         return "Index out of range"
      return self.json.cells[i].source

   def insert_code_cell(self, source, i):
      i1 = i
      if i < 0:
         i1 = self.total + i
      if i1 > self.total:
         i1 = self.total
      if i1 < 0:
         i1 = 0
      new_cell = nbformat.v4.new_code_cell(source = source)
      self.json.cells.insert(i1, new_cell)
      self.total = self.total + 1
      i2 = bisect(self.code_cells, i1)
      self.code_cells.insert(i2, i1)
      self.code_count = self.code_count + 1
      while i2 < self.code_count:
         self.code_cells[i2] = self.code_cells[i2] + 1
         i2 = i2 + 1

      i2 = bisect(self.text_cells, i1)
      while i2 < self.text_count:
         self.text_cells[i2] = self.text_cells[i2] + 1
         i2 = i2 + 1

   
   def insert_text_cell(self, source, i):
      i1 = i
      if i < 0:
         i1 = self.total + i
      if i1 > self.total:
         i1 = self.total
      if i1 < 0:
         i1 = 0
      new_cell = nbformat.v4.new_markdown_cell(source = source)
      self.json.cells.insert(i1, new_cell)
      self.total = self.total + 1
      i2 = bisect(self.code_cells, i1)
      while i2 < self.code_count:
         self.code_cells[i2] = self.code_cells[i2] + 1
         i2 = i2 + 1

      i2 = bisect(self.text_cells, i1)
      self.text_cells.insert(i2, i1)
      self.text_count = self.text_count + 1
      while i2 < self.text_count:
         self.text_cells[i2] = self.text_cells[i2] + 1
         i2 = i2 + 1

   def delete_cell(self, i):
      i1 = i
      if i < 0:
         i1 = self.total + i
      popped = self.json.cells.pop(i1)
      self.total = self.total - 1
      i2 = bisect(self.code_cells, i1)
      if popped.cell_type == "code":
         self.code_cells.pop(i2)
         self.code_count = self.code_count - 1
      while i2 < self.code_count:
         self.code_cells[i2] = self.code_cells[i2] - 1
         i2 = i2 + 1

      i2 = bisect(self.text_cells, i1)
      if popped.cell_type == "markdown":
         self.text_cells.pop(i2)
         self.text_count = self.text_count - 1
      while i2 < self.text_count:
         self.text_cells[i2] = self.text_cells[i2] - 1
         i2 = i2 + 1

   def run_cell(self, i, relative = False):
      i1 = i
      if relative:
         i1 = self.code_cells[i]
      if self.json.cells[i1].cell_type == "code":
         with io.capture_output() as captured:
            self.runtime.run_cell(self.json.cells[i1].source)
         return captured
      else:
         return "Error: Cannot run a markdown cell"

   def save_to_file (self, path):
      with open(path+".ipynb", "w") as f1:           # Open our source file
         nbformat.write(self.json, f1, version = nbformat.current_nbformat)
