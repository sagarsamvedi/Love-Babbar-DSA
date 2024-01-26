// QUESTION LINK
// https://bit.ly/3E55FvF 

#include <bits/stdc++.h>
#include<string.h>
using namespace std;

bool checkPalindrome(string s) {
    string temp = "";
    // remove extra characters
    int s_len = s.size();
    for(int i = 0; i < s_len; i++) {
        if((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= '0' && s[i] <= '9')) {
            temp.push_back(s[i]);
        }
    }
    // convert each character to lower case
    int temp_len = temp.size();
    for(int i = 0; i < temp_len; i++) {
        if(temp[i] >= 'A' && temp[i] <= 'Z') {
            temp[i] = temp[i] - 'A' + 'a';
        }
    }

    // check if palindrome
    int i = 0;
    int j = temp_len - 1;
    while (i <= j) {
        if (temp[i] != temp[j]) {
            return false; 
        }
        i++;
        j--;  
    }
    return true;
}
