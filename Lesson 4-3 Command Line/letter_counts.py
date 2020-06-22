import sys

def process_data(f):
    txt = f.read()
    letter_counts = {} 
    for c in txt:
        letter_counts[c] = letter_counts.get(c, 0) + 1

    for c in sorted(letter_counts.keys()):
        print(c + ": " + str(letter_counts[c]) + " occurrences")
        


if len(sys.argv) == 2:
    filename = sys.argv[1]
    try:
        with open(filename) as f:
            process_data(f)
    except FileNotFoundError:
        print('No such file: ', filename)
else:
    process_data(sys.stdin)


