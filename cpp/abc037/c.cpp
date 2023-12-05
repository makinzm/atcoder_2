using namespace std;

#include <vector>
#include <ostream>
#include <iostream>

int main(){
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int i=0; i<n; i++){
        cin >> a[i];
    }
    // vector to store the sum of partial a[0:i]
    vector<long long> sum(n+1);
    sum[0] = 0;
    for (int i=0; i<n; i++){
        sum[i+1] = sum[i] + a[i];
    }
    // calculate the sum of partial a[i:i+k]
    long long ans = 0;
    for (int i=0; i<n-k+1; i++){
        ans += sum[i+k] - sum[i];
    }
    cout << ans << endl;
}