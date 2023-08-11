#include <bits/stdc++.h>
using namespace std;

/*
I think we have to convert a_i to bit.
However, the number of combination is as large as 2^19 = 2^10^2 = 10^6.
Is it safe? => Yes.
But I use this: https://atcoder-companions.kakira.dev/ using https://atcoder.jp/contests/abc197/submissions/44438699
*/

int main() {
    int n;
    cin >> n;
    int a[20];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    // I may have to care ().
    int ans = numeric_limits<int>::max();
    for (int mask = 0; mask < (1 << n); mask++){
        // set unit element
        int res = 0;
        int tmp = 0;
        // mask decides whether you create ( or ) or just xor 
        for (int i = 0; i < n; i++) {
            // cout << (mask >> i) << "," << ((mask >> i )& 1) << endl;
            // cout << mask << "========" << i << endl;
            if ((mask >> i )& 1){
                // res = res xor (tmp) xor (new_tmp)
                res ^= tmp;
                tmp = a[i];
            } else {
                // tmp = tmp || a[i]
                tmp |= a[i];
            }
        }
        // cout << "*******" << endl;
        if (tmp != 0 || n == 1){
            // res = res xor new_tmp
            res ^= tmp;
        }
        ans = min(ans, res);
    }
    cout << ans << endl;
}
