using namespace std;
#include <string>
#include <vector>
#include <iostream>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string t;
    cin >> t;
    int n;
    cin >> n;
    vector<vector<string>> v(n);
    rep(i, n){
        int a;
        cin >> a;
        rep(j, a){
            string s;
            cin >> s;
            v[i].push_back(s);
        }
    }
    
    const int MAX = 1e9;
    vector<int> dp(t.size()+1, MAX);

    dp[0] = 0;

    rep(i, n){
        vector<int> before_dp(t.size()+1, MAX);
        rep(copy_i, t.size()+1) before_dp[copy_i] = dp[copy_i];
        rep(j, v[i].size()){
            rep(k, t.size()){
                if (dp[k]== MAX) continue;
                if (t.substr(k, v[i][j].size()) == v[i][j]){
                    int left_side = dp[k+v[i][j].size()];
                    int right_side = before_dp[k] + 1;
                    dp[k+v[i][j].size()] = min(left_side, right_side);
                }
            }
        }
        // print dp
        // rep(j, t.size()+1){
        //     cout << dp[j] << " ";
        // }
        // cout << endl;
    }
    if (dp[t.size()] == MAX) cout << -1 << endl;
    else
    cout << dp[t.size()] << endl;
}
