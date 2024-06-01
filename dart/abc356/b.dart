import 'dart:io';

void main() {
    final input = stdin.readLineSync()!.split(' ');
    int n = int.parse(input[0]);
    int m = int.parse(input[1]);

    final aim =stdin.readLineSync()!.split(' ').map(int.parse).toList();
    final xList = <List<int>>[];
    for (int i = 0; i < n; i++) {
        xList.add(stdin.readLineSync()!.split(' ').map(int.parse).toList());
    }

    final ateResult = List<int>.generate(m, (i) => 0);
    for (final x in xList) {
        for (final (i, a) in x.indexed) {
            ateResult[i] += a;
        }
    }

    bool isFailed = false;
    for (final (i, a) in aim.indexed) {
        if (ateResult[i] < a) {
            isFailed = true;
            break;
        }
    }

    print(isFailed ? "No" : "Yes");
}

