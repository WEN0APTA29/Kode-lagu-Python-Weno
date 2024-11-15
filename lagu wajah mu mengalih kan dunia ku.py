from time import sleep
import sys

def print_lirik():
    lines = [
        ("tujuh hari dalam seminngu", 0.08),
        ("hidup penuh warna", 0.10),
        ("ku selalu mendekatimu", 0.11),
        ("memberi tanda cinta", 0.13),
        ("engkau wanita tercantikku!!", 0.10),
        ("yang pernah kutemukan", 0.09),
        ("wajah mu mengalihkan", 0.18),
        ("duniakuuuuuuuu", 0.11),
    ]
    delays = [0.9, 0.9, 0.20, 0.30, 0.50, 0.11, 0.50, 0.20]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            sleep(char_delay)
        sleep(delays[i])
        print('')

print_lirik()