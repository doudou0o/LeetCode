#include <iostream>
#include <string>
#include <math.h>
using namespace std;


bool isPalindrome(int x) {
    if ( x<0 ) return 0;
    int length = 0;
    int temp = x;
    while(temp!=0){
        length++;
        temp = temp / 10;
    }
    int k = length / 2;
    int t1 = x,t2 = x;
    for (int i = 0; i < k; i++) {
        int w = pow(10,length-i-1);
        int a = t1%10;
        int b = t2/w;
        t1 = t1/10;
        t2 = t2%w;
        if ( a!=b ) {
            return 0;
        }
    }
    return 1;
}
int main(int argc, const char *argv[])
{
    int num;
    std::cin >> num;
    std::cout << isPalindrome(num) << std::endl;
    return 0;
}
