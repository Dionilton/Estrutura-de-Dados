#include <bits/stdc++.h>
using namespace std;

int main(){

    int total = 0;
    int min;
    int ind;
    int n;
    cin >> n;
    int vec[n][2];
    for(int i=0; i<n; i++){
        cin >> vec[i][0] >> vec[i][1];
    }

    min = vec[0][1];

    for(int i=0; i<n; i++){
        if(vec[i][1] < min){
            min = vec[i][1];
        }
        total += vec[i][0] * min;

    }

    cout << total << endl;

    return 0;
}
