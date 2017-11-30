/*  Problem link "http://www.codechef.com/JULY14/problems/SGARDEN".

    Please note that some of the constraints have been changed from the original problem statement.

    Please feel free to improve on the code

    Contributor: Ambar De (001.amby@gmail.com)
*/

#include <iostream>

using namespace std;

int nWhistle[11];

int hcf (int a, int b){
    for (;;){
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

int lcm (int a, int b){
    int temp = hcf (a, b);
    return a/ temp* b;
}

void gardenGame (int T){
    int N=0, temp=1;
    int A[11], turn[11];

    cin>> N;
    for (int i=1; i<=N; i++) cin>> A[i];

    for (int i=1; i<=N; i++){
        temp= 1;
        int l= A[i];
        while (l!=i) {l= A[l]; temp++;}
        turn[i]= temp;
    }
    nWhistle[T]= 1;
    for (int i=1; i<=N; i++) nWhistle[T]= lcm(nWhistle[T], turn[i]);
}

int main()
{
    int T=0;
    cin>> T;
    for (int i=1; i<=T; i++) gardenGame (i);
    cout<< "Results:\n";
    for (int i=1; i<=T; i++) cout<< nWhistle[i]<< "\n";
    return 0;
}
