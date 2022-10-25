
# Take in text from STT
#assuming input is .txt
from sentence_transformers import SentenceTransformer, util
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
import re

command_file = 'CommandList.txt'

pc = re.compile(r'[a-zA-Z0-9 \.]*$')
commands = []
with open(command_file) as fo:
    tokens = sent_tokenize(fo.read())
    for line in tokens:
        # line = line.replace('\n', ' ')
        line = re.sub(r' \s+', ' ', line)
        commands.append(line)
commands = re.split("\n", commands[0])
print('sentences =\n{}'.format(commands))

input_file = 'testinput.txt'
input_sentences = []
with open(input_file) as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        input_sentences.append(line)

''' 
doing text cleaning because testinput is funky
'''
input_sentences = re.split("\n", input_sentences[0])
input_sentences = [i for i in input_sentences if i != '']


print('input_sentence =\n{}'.format(input_sentences))



model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(commands)

print('\nResults:')
for sentence in input_sentences:
    emb = model.encode(sentence)
    cos_sim = util.cos_sim(embeddings, [emb])

    sentence_combinations = []
    for i in range(0, len(cos_sim)):
        sentence_combinations.append([i, cos_sim[i]])
    sorted_sentence_combinations = sorted(sentence_combinations, key=lambda x: x[1], reverse=True)
    # show
    print('> {}'.format(sentence))
    for i, sc in enumerate(sorted_sentence_combinations[0:3]):
        print('  {:.4f} {}'.format(sc[1][0], commands[sc[0]]))


# Find closest command
# Execute command
