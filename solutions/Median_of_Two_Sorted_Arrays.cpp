#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int findKth(vector<int> A,vector<int> B,int k)
{
    int l1 = A.size();
    int l2 = B.size();
    if ( l1 > l2 )
        return findKth(B,A,k);
    if ( k == 1 )
        return std::min( A.at(0) , B.at(0));
    if ( m == 0 )
        return B.at(k-1);
    int pa = std::min(k/2,m);

}
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2){
    int length1 = nums1.size();
    int length2 = nums2.size();
    int toral = length1 + length2;
    if ( toral & 0x1 )
        return findKth(nums1,nums2,toral/2 + 1);
    else
        return (findKth(nums1,nums2,toral/2)
                +findKth(nums1,nums2,toral/2+1))/2;
        }
    int main(int argc, const char *argv[])
    {
        std::vector<int> n1;
        std::vector<int> n2;
        n1.push_back(1);
        n1.push_back(2);
        n1.push_back(3);
        n1.push_back(4);
        n1.push_back(5);

        n2.push_back(3);
        n2.push_back(4);
        n2.push_back(5);
        n2.push_back(6);
        n2.push_back(7);
        n2.push_back(8);
        double ans = findMedianSortedArrays(n1,n2);
        std::cout << ans << std::endl;
        return 0;
    }
