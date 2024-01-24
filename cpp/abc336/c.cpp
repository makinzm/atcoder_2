#include <iostream>
#include <vector>
// #include <cmath>

using namespace std;

long long int ipow(int base, int exp) {
    long long int result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result *= base;
        }
        base *= base;
        exp /= 2;
    }
    return result;
}

long long int create_quinary(long long int n) {
    long long int n5 = 0;
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
    long long int n;
    cin >> n;
    long long int n5 = create_quinary(n-1);
    cout << n5 * 2 << endl;
}
