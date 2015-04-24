#include <iostream>
#include <string>
#include <vector>
using namespace std;


string longestPalindrome(string s)
{
    string news;
    for (int i = 0; i < s.size(); i++) {
        news.push_back('#');
        news.push_back(s.at(i));
    }
    news.push_back('#');
    std::vector<int> p (news.size());


}
int main(int argc, const char *argv[])
{
    string str="jabccbagg";
    std::cin >> str;
    std::cout << longestPalindrome(str) << std::endl;
    return 0;
}
