import unittest
from TTC import ClosestCommand

class ClosestCommandTest(unittest.TestCase):
    ttc = ClosestCommand.TextToCommands()

    input_sentences = [
        "create code cell",
        "create text cell",
        "insert code cell",
        "move code cell up",
        "delete cell ",
        "delete cell 2",
        "run cell",
        "run all cells",
        "run cells",
        "read cell",
        "zip my files"]
    
    matched_sentences = [
        "Create new [type] Cell",
        "Create new [type] Cell",
        "Insert [type] Cell to {num/current_above}",
        "Move cell [up/down]",
        "delete cell {num/current cell}",
        "delete cell {num/current cell}",
        "run cell",
        "run all cells",
        "run cell",
        "read cell",
        None]

    for i, sentence in enumerate(input_sentences):
        my_match = ttc.findMatch(sentence)
        unittest.TestCase.assertEqual(my_match, matched_sentences[i])   # TODO: FIX THIS IT BREAKS SOMETIMES???
        