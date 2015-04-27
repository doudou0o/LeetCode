#include <iostream>
#include <string>
#include <climits>
using namespace std;

int myAtoi(string str){;
    if(str.size() == 0)return 0;
    int start = 0;
    while (str.at(start)==' ')
        start++;
    if(start == str.size())return 0;
    if ( (str.at(start)<'0'||str.at(start)>'9')&&
            str.at(start)!='+'&&str.at(start)!='-') {
        return 0;
    }
    int sign = 1;
    if ( str.at(start) == '-' ){
        sign = -1;
        start++;
        if ( str.at(start) == '+' ||  str.at(start) == '-' )
            return 0;
    }
    if ( str.at(start) == '+' ) {
        start++;
        if ( str.at(start) == '+' ||  str.at(start) == '-' )
            return 0;
    }
    int ans=0;
    for (int i = start; i < str.size(); i++) {
        if ( str.at(i)<'0'||str.at(i)>'9' )break ;
        int t = str.at(i) - '0';
        int temp = ans*10 + t;
        if ( temp<0 || (temp/10)<ans ) {
            return sign==1 ? INT_MAX:INT_MIN;
        }
        ans = temp;
    }
    return ans*sign;
}
int main(int argc, const char *argv[])
{
    string str;
    std::cin >> str;
    std::cout << myAtoi(str) << std::endl;
    return 0;
}
