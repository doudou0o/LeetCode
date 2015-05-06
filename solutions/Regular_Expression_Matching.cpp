#include <iostream>
#include <string>
using namespace std;

bool isMatch(string a,string b)
{
    int lena = a.length();
    int lenb = b.length();
    int dp[lena+1][lenb+1];

    dp[0][0] = 1;
    for (int i = 1; i < lena+1; i++)
        dp[i][0] = 0;
    for (int j = 1; j < lenb+1; j++)
        dp[0][j] = b[j-1]=='*' && dp[0][j-2] == 1;

    for (int i = 1; i < lena+1; i++) {
        for (int j = 1; j < lenb+1; j++) {
            if (b[j-1] != '*') {
                dp[i][j] = dp[i-1][j-1] == 1 && (b[j-1] == a[i-1] || b[j-1] == '.');
            }
            else {
                dp[i][j] = dp[i][j-1] == 1 || dp[i][j-2] == 1 || (dp[i-1][j] == 1 && (b[j-2]==a[i-1] || b[j-2] == '.'));                                                                                                                    ;
            }
        }
    }
    for (int i = 0; i < lena+1; i++) {
        for (int j = 0; j < lenb+1; j++) {
            std::cout << dp[i][j] << " ";
        }
        std::cout << std::endl;
    }
    return dp[lena][lenb]==1;
}
int main(int argc, const char *argv[])
{
    string a = "a";
    string b = "ab*a";
    std::cout << isMatch(a,b) << std::endl;
    return 0;
}
