/*  Problem link "http://www.codechef.com/JULY14/problems/CSUB". 
    
    Please note that unlike the constraints stated in the link, this code has been written under the following constraints:
    # of test cases T = 10
    # of elements in each test case = 10
    # sum of N over all test cases = 100
    
    Please feel free to improve on the code
    
    Contributor: Ambar De (001.amby@gmail.com)
*/

#include <iostream>

using namespace std;

int N[11], arrT[11][10];

void countSubstrings (int Ni){
    cin>>N[Ni];
    int temp= 0;
    for (int i=0; i<N[Ni]; i++) cin>> arrT[Ni][i];
    for (int i=0; i<N[Ni]; i++){
        if (arrT[Ni][i]== 1)
            for (int j=i; j<N[Ni]; j++)
                if (arrT[Ni][j]== 1)
                    temp++;
    }
    N[Ni]= temp;
}

int main(){
    int T= 0;
    cin>> T;
    for (int i=1; i<=T; i++){
        countSubstrings(i);
    }
    for (int i=1; i<=T; i++)    cout<< N[i]<< "\n";
    return 0;
}
