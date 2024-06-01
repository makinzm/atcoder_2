Env:
- Ref: https://note.com/fuuuuusha/n/n9c16247c49bc
    - I add this step: ` ls /usr/local/bin/ | grep gcc`
    - and then I change the part of `g++` to the previous result.
        - `g++-13 <>.cpp`
- alias `alias atcoder='g++ -std=c++17 -I../ac-library/'`
