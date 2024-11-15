from time import sleep
import sys

def print_lirik():
    lines = [
        ("jika aku bukan jalan mu", 0.14),
        ("ku berhenti mengharapkan mu", 0.17),
        ("jika aku memang tercipta untukmu", 0.17),
        ("ku kan memilikimu", 0.14),   
    ]
    delays = [3, 1.2, 3, 0]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            sleep(char_delay)
        sleep(delays[i])
        print('')

print_lirik()