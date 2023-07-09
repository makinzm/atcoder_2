#include <bits/stdc++.h>

int calculateSalary(int i, const std::map<int, std::vector<int>>& dictionary){
    if (dictionary.count(i) == 0 || dictionary.at(i).empty()) {
        return 1;
    } else {
        const std::vector<int>& subordinates = dictionary.at(i);
        int min = calculateSalary(subordinates[0], dictionary);
        int max = min;
        for (int i = 1; i < subordinates.size(); i++) {
            int value = calculateSalary(subordinates[i], dictionary);
            if (min > value) {
                min = value;
            }
            if (max < value){
                max = value;
            }
        }
        return max + min + 1;
    }
}


int main() {
    int n;
    std::cin >> n;
    std::map<int, std::vector<int>> dictionary;

    for(int i = 0; i < n; i++){
        dictionary[i] = std::vector<int>();
    }

    for(int i = 1; i < n; i++){
        int key;
        std::cin >> key;
        dictionary[key-1].push_back(i);
    }

    std::cout << calculateSalary(0, dictionary) << std::endl;
}
