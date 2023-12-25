//question link
//https://leetcode.com/problems/spiral-matrix/

#include<vector.h>
using namespace std;
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int count = 0;
        int total_elements = rows*cols;
        
        int startingRow = 0;
        int startingCol = 0;
        int endingRow = rows - 1;
        int endingCol = cols -1;
        vector<int> ans;
        
        
        while (count < total_elements){
            //printing starting row
            for (int col = startingCol; count < total_elements && col <= endingCol; col++){
                ans.push_back(matrix[startingRow][col]);
                count++;
            }
            startingRow++;
            //printing ending column
            for (int row = startingRow; count < total_elements && row <= endingRow; row++){
                ans.push_back(matrix[row][endingCol]);
                count++;
            }
            endingCol--;
            //printing ending row
            for (int col = endingCol; count < total_elements && col >= startingCol; col--){
                ans.push_back(matrix[endingRow][col]);
                count++;
            }
            endingRow--;
            //printing staring column
            for (int row = endingRow; count < total_elements && row >= startingRow; row--){
                ans.push_back(matrix[row][startingCol]);
                count++;
            }
            startingCol++;
            
        }
        return ans;
    }
};