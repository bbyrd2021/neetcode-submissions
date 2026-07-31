class Solution {
public:
    bool binary_search(int l, int r, vector<int>& line, int &target){
        if (l > r) return false;
        int m = l + (r - l) / 2;

        if (target == line[m]) return true;
        else if (target < line[m]) return binary_search(l, m-1, line, target);
        else if (target > line[m]) return binary_search(m+1, r, line, target);
    }
    
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int top = 0;
        int btm = matrix.size() - 1;

        int mid; 

        while (top <= btm) {
            mid = top + (btm - top) / 2;
            if (target >= matrix[mid][0] && target <= matrix[mid][matrix[mid].size()-1]) {
                return binary_search(0, matrix[mid].size()-1, matrix[mid], target);
            }
            else if (target < matrix[mid][0]) {
                btm = mid - 1;
            }
            else if (target > matrix[mid][0]){
                top = mid + 1;
            } 
        }

        return false;
    }
};
