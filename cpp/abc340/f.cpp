#include <iostream>
using namespace std;

long long extGCD(long long a, long long b, long long &tmp_x, long long &tmp_y){
    // Reference: https://qiita.com/drken/items/b97ff231e43bce50199a
    // https://github.com/drken1215/algorithm/blob/54a71b363395c40ba9e394902296f56812f29cd0/MathNumberTheory/extended_GCD.cpp
    if (b == 0){
        tmp_x = 1;
        tmp_y = 0;
        return a;
    }
    long long d = extGCD(b, a%b, tmp_y, tmp_x);
    tmp_y -= a / b * tmp_x;
    return d;
}

int main() {
    long long int a;
    long long int b;
    cin >> a >> b;
    long long int x, y;
    long long int d = extGCD(b, a, x, y);
    if (2 % d != 0) {
        cout << -1 << endl;
        return 0;
    } else {
        long long int k = 2 / d;
        x *= k;
        y *= k;
        cout << x << " " << y << endl;
    }
}