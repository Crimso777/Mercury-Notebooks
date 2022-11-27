# Take in text from STT
#assuming input is .txt

# imports
from sentence_transformers import SentenceTransformer, util
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
import re

class TextToCommands:
  command_file = 'CommandList.txt'
  commands = []
  with open(command_file) as fo:
    tokens = sent_tokenize(fo.read())
    for line in tokens:
        # line = line.replace('\n', ' ')
        line = re.sub(r' \s+', ' ', line)
        commands.append(line)
  commands = re.split("\n", commands[0])
  print('Commands loaded...\n{}'.format(commands))
  
  model = SentenceTransformer('all-MiniLM-L6-v2')
  embeddings = model.encode(commands)
  
  def findMatch(self, input_string):
    emb = self.model.encode(input_string)
    cos_sim = util.cos_sim(self.embeddings, [emb])
    
    sentence_combinations = []
    for i in range(0, len(cos_sim)):
        sentence_combinations.append([i, cos_sim[i]])

    sorted_sentence_combinations = sorted(sentence_combinations, key=lambda x: x[1], reverse=True)

    for i, sc in enumerate(sorted_sentence_combinations[0:1]):
      if sc[1][0] > .5:
        return self.commands[sc[0]]
      else:
        return None
  
  def findVariables(self, solid_match, matched_command):
    var = None
    if "[type]" in matched_command:
        if "code" in solid_match:
          var = "code"
        elif "text" in solid_match:
          var = "text"
        else:
          var = "Unkown"
          # TODO: REPLACE ABOVE WITH 
          # 1. Ask user to provide a correct input for this command
          # 2. Call Speech to Text command
          # 3. Preprocess text for passing to executing that command
    elif "[up/down]" in matched_command:
      if "up" in solid_match:
        var = "up"
      elif "down" in solid_match:
        var = "down"
      else:
        var = "Unknown"
        # TODO: REPLACE ABOVE WITH 
          # 1. Ask user to provide a correct input for this command
          # 2. Call Speech to Text command
          # 3. Preprocess text for passing to executing that command
    # TODO: get optional{} vars from commands, this will depend on most likely command, and can be extrapolated to more simple function calls.
    print(f"current command: {solid_match}\n intepreted as: {matched_command}\n has var: {var}")
    # TODO: run that command.