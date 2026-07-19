class Solution {
public:
    int binary_search_(int l, int r, vector<int>& nums, int target){
        if (l > r) return -1;
        int m = l + (r - l) / 2;

        if (nums[m] == target) return m;

        if (target < nums[m]) {
            return binary_search_(l, m-1, nums, target);
        } else {
            return binary_search_(m+1, r, nums, target);
        }

    }

    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size()-1;
        return binary_search_(l, r, nums, target);
    }
};
