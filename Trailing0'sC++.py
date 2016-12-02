## C++ program to count trailing 0s in n!
#include <iostream>
using namespace std;
 
// Function to return trailing 0s in  of n
int findTrailingZeros(int  n)
{
    // Initialize result
    int count = 0;
 
    // Keep dividing n by powers of 5 and update count
    for (int i=5; n/i>=1; i *= 5)
          count += n/i;
 
    return count;
}
 
//  Test above function
int main()
{
    int n = 20;
    cout << "Count of trailing 0s in " << 20
         << "! is " << findTrailingZeros(n);
    return 0;
}
