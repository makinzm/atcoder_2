#include <iostream>
#include <vector>
// #include <cmath>

using namespace std;

long int ipow(int base, int exp) {
    long int result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result *= base;
        }
        base *= base;
        exp /= 2;
    }
    return result;
}

long int create_quinary(long int n) {
    long int n5 = 0;
    int i = 0;
    while (n > 0) {
        n5 += (n % 5) * ipow(10, i);
        n /= 5;
        i++;
    }
    return n5;
}

vector<int> Vec = {0, 2, 4, 6, 8};

int main() {
    long int n;
    cin >> n;
    long int n5 = create_quinary(n-1);
    int n5_len = 0;
    long int tmp = n5;
    while (tmp > 0) {
        n5_len++;
        tmp /= 10;
    }
    cout << n5 * 2 << endl;
}
