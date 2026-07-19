class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> cols;
        unordered_map<int, unordered_set<char>> rows;
        unordered_map<int, unordered_set<char>> boxes;

        for (int r = 0; r < 9; r++){
            for (int c = 0; c < 9; c++){
                if (board[r][c] == '.') continue;

                int box = (r/3) * 3 + (c/3);

                if (rows[r].contains(board[r][c]) ||
                cols[c].contains(board[r][c]) ||
                boxes[box].contains(board[r][c])){
                    return false;
                }
                cols[c].insert(board[r][c]);
                rows[r].insert(board[r][c]);
                boxes[box].insert(board[r][c]);
            }
        }
        return true;

    }
};
