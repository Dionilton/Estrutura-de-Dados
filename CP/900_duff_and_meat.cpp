#include <bits/stdc++.h>
using namespace std;

int main(){

    int total = 0;
    int min = 101;
    int ind;
    int n;
    cin >> n;
    int vec[n][2];
    for(int i=0; i<n; i++){
        cin >> vec[i][0] >> vec[i][1];
        if(vec[i][1] < min){
            min = vec[i][1];
            ind = i;
        }
    }

    for(int i=0; i<n; i++){
        if(i <= ind){
            total += vec[i][0] * vec[i][1];
        }
        else{
            total += vec[i][0] * vec[ind][1];
        }
    }

    cout << total << endl;

    return 0;
}