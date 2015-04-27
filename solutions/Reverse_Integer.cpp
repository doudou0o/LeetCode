#include <iostream>
#include <string>
#include <climits>
using namespace std;

int reverse(int x)
{
    int ans=0;
    int tempx = x<0?-x:x;
    while(tempx != 0){
        int t = ans*10 + tempx%10;
        tempx = tempx / 10;
        if ( t < 0 || (t/10) < ans) {
            return 0;
        }
        ans = t;
    }
    return x<0?-ans:ans;
}
int main(int argc, const char *argv[])
{
    int num;
    std::cin >> num;
    std::cout << reverse(num) << std::endl;
    return 0;
}
