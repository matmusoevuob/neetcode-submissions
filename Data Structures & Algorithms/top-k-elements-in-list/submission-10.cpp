#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int num : nums) ++freq[num];

        vector<vector<int>> buckets(nums.size() + 1);
        for (auto& entry : freq) {
            buckets[entry.second].push_back(entry.first);
        }

        vector<int> result;
        result.reserve(k);
        for (int i = static_cast<int>(buckets.size()) - 1; i > 0 && static_cast<int>(result.size()) < k; --i) {
            for (int num : buckets[i]) {
                result.push_back(num);
                if (static_cast<int>(result.size()) == k) break;
            }
        }
        return result;
    }
};
