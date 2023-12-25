//Question link
//https://leetcode.com/problems/string-compression/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int compress(vector<char>& chars) {
        int index = 0;
        int ans_index = 0;
        int size = chars.size();
        while (index < size){
            int j = index + 1;
            while ( j < size && chars[index] == chars[j]){
                j++;
            }
            chars[ans_index++] = chars[index];
            int count = j-index;
            
            if (count > 1){
                string cnt = to_string(count);
                for(char ch: cnt){
                    chars[ans_index++] = ch;
                }
            }
            index = j;
        }
        return ans_index;
    }
};