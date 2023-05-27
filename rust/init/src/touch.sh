#!/bin/bash

for (( i = 97; i <= 103; i++ )); do
    current_char=$(printf \\$(printf '%03o' $i))
    filename=""$current_char".rs"
    touch $filename
    echo "// Here is "$current_char"'s problem\n\nfn main() {\n\tprintln!(\"Here is "$current_char"!\");\n}" > $filename
done
