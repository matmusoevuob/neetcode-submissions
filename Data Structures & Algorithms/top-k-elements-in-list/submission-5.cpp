#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int num : nums) ++freq[num];

        vector<pair<int, int>> pairs(freq.begin(), freq.end());
        sort(pairs.begin(), pairs.end(), [](const auto& a, const auto& b) {
            return a.second > b.second;
        });

        vector<int> result;
        for (int i = 0; i < k && i < static_cast<int>(pairs.size()); ++i) {
            result.push_back(pairs[i].first);
        }
        return result;
    }
};