#include <iostream>
#include <vector>
using namespace std;

int maxArea(vector<int>& height)
{
    int i = 0;
    int j = height.size()-1;
    int max = 0;
    while(i!=j){
        int water;
        if (height.at(i) < height.at(j)) {
            water = height.at(i) * (j-i);
            i++;
        }
        else {
            water = height.at(j) * (j-i);
            j--;
        }
        max = water > max ? water : max;
    }
    return max;
}
int main(int argc, const char *argv[])
{
    std::vector<int> h;
    h.push_back(2);
    h.push_back(7);
    h.push_back(6);
    h.push_back(5);
    std::cout << maxArea(h) << std::endl;
    return 0;
}
