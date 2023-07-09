#include <bits/stdc++.h>

std::map<int, int> memo;

int calculateSalary(int i, const std::map<int, std::vector<int>>& dictionary) {
    if (memo.count(i) != 0) {
        // std::cout << "Memo is used at " << i << std::endl;
        return memo[i];
    }else if (dictionary.count(i) == 0 || dictionary.at(i).empty()) {
        // std::cout << "Solved " << i << std::endl;
        return 1;
    } else {
        const std::vector<int>& subordinates = dictionary.at(i);
        int min = calculateSalary(subordinates[0], dictionary);
        int max = min;
        
        for (size_t j = 1; j < subordinates.size(); j++) {
            int value = calculateSalary(subordinates[j], dictionary);
            if (min > value) {
                min = value;
            }
            if (max < value) {
                max = value;
            }
        }
        
        int result = max + min + 1;
        // std::cout << "Solved " << i << std::endl;
        memo[i] = result;
        return result;
    }
}

int main() {
    int n;
    std::cin >> n;
    std::map<int, std::vector<int>> dictionary;

    for (int i = 0; i < n; i++) {
        dictionary[i] = std::vector<int>();
    }

    for (int i = 1; i < n; i++) {
        int key;
        std::cin >> key;
        dictionary[key - 1].push_back(i);
    }
    
    std::cout << calculateSalary(0, dictionary) << std::endl;
}
