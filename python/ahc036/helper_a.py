import subprocess
import sys

command = ["rye", "run", "python3", "a.py"]

input_data = """7 9 3 7 4
0 1
0 2
0 3
1 2
2 3
3 4
4 5
5 6
6 0
4 1 5
100 0
200 0
200 100
100 100
0 200
0 100
0 0"""

process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

stdout, stderr = process.communicate(input_data)

print(stdout)

if stderr:
    print(stderr, file=sys.stderr)
