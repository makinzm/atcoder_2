#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <vector>

using namespace std;

// 回文かどうかをチェックする関数
bool isPalindrome(const string& s) {
    int left = 0;
    int right = s.size() - 1;
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

// k文字の回文を含むかどうかをチェックする関数
bool containsKLengthPalindrome(const string& s, int k) {
    for (int i = 0; i <= s.size() - k; ++i) {
        if (isPalindrome(s.substr(i, k))) {
            return true;
        }
    }
    return false;
}

int main() {
    int num, kaibun_length;
    cin >> num >> kaibun_length;
    string base_string;
    cin >> base_string;

    int count = 0;

    sort(base_string.begin(), base_string.end());

    do {
        if (!containsKLengthPalindrome(base_string, kaibun_length)) {
            count++;
        }
    } while (next_permutation(base_string.begin(), base_string.end()));

    cout << count << endl;

    return 0;
}
