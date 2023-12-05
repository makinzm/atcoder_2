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
    long long sum = 0;
    for (int i=0; i<n; i++){
        // n-k+1 is the maximum number of times that a[i] is added to the sum.
        // k is also the maximum number of times that a[i] is added to the sum.
        sum += a[i] * min(min(min(i+1, n-i),n-k+1),k);
    }
    cout << sum << endl;
}