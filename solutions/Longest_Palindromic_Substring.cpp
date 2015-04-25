#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


string longestPalindrome(string s)
{
    string news;
    for (int i = 0; i < s.size(); i++) {
        news.push_back('#');
        news.push_back(s.at(i));
    }
    news.push_back('#');
    std::vector<int> p (news.size(),0);

    int cur = 0, right = 0;
    for (int i = 0; i < news.size()-1; i++) {
        int mirror = 2*cur - i;
        p[i] = right > i ? std::min( right-i , p[mirror] ):0;

        while ((i+1+p[i]<news.size())&&(i-1-p[i]>=0)&&news.at(i+1+p[i]) == news.at(i-1-p[i]))
            p[i]++;

        if (i+p[i]>right) {
            cur = i;
            right = i +p[i];
        }
    }

//    for (int i = 0; i < p.size(); i++) {
//        std::cout << p[i] << " ";
//    }
    int maxlen=1,pos=0;
    for (int i = 1; i < news.size()-1; i++) {
        if (maxlen < p[i]) {
            maxlen = p[i];
            pos = i;
        }
    }
    p.clear();
//    std::cout << std::endl << pos <<" "<< maxlen << std::endl;
    return s.substr((pos + 1 - maxlen)/2 , maxlen);
}
int main(int argc, const char *argv[])
{
    string str="jabccbagg";
    std::cin >> str;
    std::cout << longestPalindrome(str) << std::endl;
    return 0;
}
