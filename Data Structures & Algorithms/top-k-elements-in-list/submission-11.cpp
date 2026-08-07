#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> freq;
        freq.reserve(n);
        for (int num : nums) ++freq[num];

        vector<vector<int>> buckets(n + 1);
        for (auto& entry : freq) {
            buckets[entry.second].push_back(entry.first);
        }

        vector<int> result;
        result.reserve(k);
        for (int i = n; i > 0 && static_cast<int>(result.size()) < k; --i) {
            for (int num : buckets[i]) {
                result.push_back(num);
                if (static_cast<int>(result.size()) == k) return result;
            }
        }
        return result;
    }
};
