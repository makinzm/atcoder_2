import subprocess
import sys

command = ["uv", "run", "python3", "a.py"]

try:
    with open("input.txt") as file:
        input_data = file.read()
except FileNotFoundError:
    print("Error: input.txt file not found.", file=sys.stderr)
    sys.exit(1)
except OSError:
    print("Error: Could not read input.txt file.", file=sys.stderr)
    sys.exit(1)

process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

stdout, stderr = process.communicate(input_data)

try:
    with open("output.txt", "w") as file:
        file.write(stdout)
    print("Output has been written to output.txt")
except OSError:
    print("Error: Could not write to output.txt file.", file=sys.stderr)
    sys.exit(1)

if stderr:
    print("Errors occurred:", file=sys.stderr)
    print(stderr, file=sys.stderr)
