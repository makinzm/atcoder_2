#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> events;

    for (int i = 0; i < n; i ++) {
        int l, r;
        cin >> l >> r;
        events.emplace_back(l, 1);
        events.emplace_back(r, -1);
    }

    sort(events.begin(), events.end(), [](pair<int, int> a, pair<int, int> b) {
        if (a.first == b.first) {
            return a.second > b.second;
        }
        return a.first < b.first;
    });

    // for (const auto &event:events) {
    //     cout << event.first << " " << event.second << endl;
    // }

    long long int count = 0;
    long long int num_active_interval = 0;

    for (const auto& event : events) {
        assert( num_active_interval >= 0 );
        if (event.second == 1) {
            count += num_active_interval;
            num_active_interval++;
        } else {
            num_active_interval--;
        }
    }

    cout << count << endl;

    return 0;
}

