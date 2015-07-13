#include <iostream>
#include <string>
#include <stack>
using namespace std;
bool isValid(string s)
{
    std::stack<char> S;
    for (int i = 0; i < s.length(); i++) {
        char c = s[i];
        if ( c =='[' || c =='(' || c=='{' ) 
            S.push(c);
        else {
            if(S.empty()) return 0;
            switch ( c ) {
                case '}':
                    if( S.top() != '{' ) return 0;
                    else S.pop();
                    break;
                case ']':
                    if ( S.top() != '[' ) return 0;
                    else S.pop();
                    break;
                case ')':
                    if ( S.top() != '(' ) return 0;
                    else S.pop();
                    break;
                default:
                    return 0;
            }
        }
    }
    if(!S.empty())return 0;
    return 1;
}
int main(int argc, const char *argv[])
{
    string a = "{[{([[])}}]}";
    std::cout << isValid(a) << std::endl;
    return 0;
}
