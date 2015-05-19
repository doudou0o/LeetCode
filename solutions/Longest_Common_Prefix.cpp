#include <iostream>
#include <string>
#include <vector>
using namespace std;
string longestCommonPrefix(vector<string>& strs) {
    int count = strs.size();
    string result;
    if ( strs.size() == 0)return result;

    bool hasnext = true;
    int num = 0;
    while (hasnext) {
        for (int i = 0; i < count; i++) {
            if(strs[i].length()==num||strs[i].at(num)!=strs[0].at(num)){
                hasnext = false;
                break;
            }
        }
        if ( hasnext ) result.push_back(strs[0].at(num));
        num++;
    }
    return result;
}
int main(int argc, const char *argv[])
{
    std::vector<string> strs;
    strs.push_back("");
    strs.push_back("abcfffss");
    strs.push_back("abcdddd2");
    std::cout << longestCommonPrefix(strs) << std::endl;
    return 0;
}
