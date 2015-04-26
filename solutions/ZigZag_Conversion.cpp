#include <iostream>
#include <string>
#include <vector>
using namespace std;

string convert(string s, int numRows)
{
    if( numRows == 1)return s;
    int length = s.size();
    std::vector<int> p(length,0);
    int D = 1;
    int T = 1;
    for (int i = 0; i < length; i++) {
        p[i] = D;
        D += T;
        if ( D == numRows)
            T = -1;
        if ( D == 1)
            T = 1;
    }
    string ans;
    for (int i = 1; i <= numRows; i++) {
        for (int j = 0; j < length; j++) {
            if (p[j] == i)
                ans.push_back(s.at(j));
        }
    }
    return ans;
}
int main(int argc, const char *argv[])
{
    string str;
    int n;
    std::cin >> str >> n;
    std::cout << convert(str,n) << std::endl;
    return 0;
}
