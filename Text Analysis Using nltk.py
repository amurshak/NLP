import nltk
from nltk.tokenize import word_tokenize
from nltk.text import Text
nltk.download()

my_string  = """Two plus two is four, minus one that's three — quick maths.
Every day man's on the block. Smoke trees.
See your girl in the park, that girl is an uckers.
When the thing went quack quack quack, your men were ducking!
Hold tight Asznee, my brother. He's got a pumpy.
Hold tight my man, my guy. He's got a frisbee.
I trap, trap, trap on the phone. Moving that cornflakes, rice crispies.
Hold tight my girl Whitney."""


tokens = word_tokenize(my_string)
tokens = [word.lower() for word in tokens]
token[:5]

t = Text(tokens)
t

