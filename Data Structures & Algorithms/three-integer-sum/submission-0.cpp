class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int l = 0;
        int r = 0;

        set<vector<int>> result;
        sort(nums.begin(), nums.end());
        for (int i=0; i < nums.size(); i++){
            for (l = i+1; l < nums.size(); l++){
                for (r = l+1; r < nums.size(); r++){
                    if (nums[i] + nums[l] + nums[r] == 0){
                        result.insert({nums[i], nums[l], nums[r]});
                    }
                }
            }
        }

        return vector<vector<int>>(result.begin(), result.end());
    }
};
