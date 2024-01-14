import 'dart:io';

void main() {
    final n = int.tryParse(stdin.readLineSync()!);

    if ( n == null ) {
        throw FormatException("You have to input numerical character.");
    }

    stdout.write("L");
    for (int i = 0; i < n; i++) {
        stdout.write("o");
    }
    stdout.write("ng");
}
