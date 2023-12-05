using namespace std;

#include <vector>
#include <ostream>
#include <iostream>

int main(){
    int n, k;
    cin >> n >> k;
    vector<long long> a(n);
    for (int i=0; i<n; i++){
        cin >> a[i];
    }
    long long sum = 0;
    for (int i=0; i<n; i++){
        sum += a[i] * min(min(min(i+1, n-i),n-k+1),k);
    }
    cout << sum << endl;
}