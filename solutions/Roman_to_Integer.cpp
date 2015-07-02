#include <iostream>
#include <string>
using namespace std;
string intToRoman(int num)
{
    int val[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
    string Roman[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
    string ans;
    while (num!=0) {
        for (int i = 0; i < 13; i++) {
            if ( num>=val[i] ){
                ans.append(Roman[i]);
                num = num - val[i];
                break;
            }
        }
    }
    return ans;
}
int romanToInt(string s)
{
    int val[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
    string Roman[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
    int ans = 0;
    while(s.size()!=0){
        string twoStr = s.substr(0,2);
        bool finded = 0 ;
        for (int i = 1; i < 13; i=i+2) {
            if ( twoStr.compare(Roman[i])==0 ) {
                ans += val[i];
                s = s.substr(2);
                finded = 1;
                break;
            }
        }
        if ( finded ) continue;
        string oneStr = s.substr(0,1);
        for (int i = 0; i < 13; i=i+2) {
            if ( oneStr.compare(Roman[i])==0 ) {
                ans += val[i];
                s = s.substr(1);
                break;
            }
        }
    }
    return ans;
}
int main(int argc, const char *argv[])
{
    int a;
    std::cin >> a;
    std::cout << intToRoman(a) << std::endl;
    std::cout << romanToInt(intToRoman(a)) << std::endl;
    return 0;
}
