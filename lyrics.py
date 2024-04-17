import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Yeah", 0.1),
        ("My granny called, she said, Travvy, you work too hard", 0.06),
        ("I'm worried you forget about me", 0.03),
        ("I'm falling in and out of clouds, don't worry, I'ma get it, granny, uh", 0.09),
        ("What happened? Now my daddy happy, mama called me up", 0.06),
        ("That money coming and she love me, I done made it now", 0.08),
        ("I done found life's meaning now, all them her heart'd break", 0.08),
        ("Her heart not in pieces now", 0.03)

    ]

    delays = [0.3, 0.3, 0.3, 0.3, 0.4, 0.3, 0.1, 0.6, 0.07, 0.3, 0.5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()