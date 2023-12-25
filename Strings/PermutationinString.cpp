//QUESTION LINK
// https://leetcode.com/problems/permutation-in-string/
// include<std.h>
#include <bits/stdc++.h>
using namespace std;

class Solution{
private:
    bool checkEqual(int a[26], int b[26]){
        for (int i = 0; i < 26; i++){
            if (a[i] != b[i]){
                return false;
            }
        }
        return true;
    }
    
public:
    bool checkInclusion(string s1, string s2) {
        //character count array
        int count[26] = {0};
        int window_size = s1.length();        
        for (int i = 0; i < window_size; i++){
            int index = s1[i] - 'a';
            count[index]++;
        }
        
        //traverse s2 inwindow size of s1
        int i = 0;
        int count2[26] = {0};
        while (i < window_size && i < s2.length()){
            int index = s2[i] - 'a';
            count2[index]++;
            i++;
        }
        if (checkEqual(count,count2)){
            return 1;
        }
        //running for other windows
        while (i < s2.length()){
            //adding next element count
            int index = s2[i] - 'a';
            count2[index]++;
            //removing first character of window
            int oldchar_index = s2[i-window_size] - 'a';
            count2[oldchar_index]--;
            if (checkEqual(count,count2)){
                return 1;
            }
            i++;
        }
        return 0;
    }
};