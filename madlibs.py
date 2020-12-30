""" 
According to Wikipedia, Madlibs is...
a phrasal template word game which consists of one player prompting others 
for a list of words to substitute for blanks in a story before reading aloud. 
The game is frequently played as a party game or as a pastime.
"""

from template import cooking, night_circus, programmer
import random

if __name__ == "__main__":
    m = random.choice([cooking, night_circus, programmer])
    m.madlib()
