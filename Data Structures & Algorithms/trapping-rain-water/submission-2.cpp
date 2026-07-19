class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0) return 0;
        int l = 0;
        int r = height.size()-1;
        int res = 0;

        int max_L = height[l];
        int max_R = height[r];
        
        while (l < r){
            if (max_L <= max_R) {
                l++;
                max_L = max(max_L, height[l]);
                res += max_L - height[l];
            } else {
                r--;
                max_R = max(max_R, height[r]);
                res += max_R - height[r];
            }
        }
        return res;
    }
};
