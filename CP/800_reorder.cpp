#include <bits/stdc++.h>
using namespace std;

int main(){

    int x;
    cin >> x;
    int n,m;
    for(int i = 0; i<x; i++){
        cin >> n >> m;
        int vec[n];
        for(int j = 0; j<n; j++){
            cin >> vec[j];
        }
        int temp;

        //bubble sort:
        for(int j = n-1; j>0; j--){
            for(int k=0; k<=j; k++){
                if(vec[k] > vec[k + 1]){
                    temp = vec[k];
                    vec[k] = vec[k + 1];
                    vec[k +1] = temp;
                }
            } 
        }
        cout << "sai do sort" << endl;
        float vec_f[n];
        for(int j=0; j<n; j++){
            cout << "to no primeiro for" << endl;
            vec_f[j] = vec[j]/j+1;
        }

        for(int j=0; j<n; j++){
            cout << "to no ultimo for" << endl;
            cout << vec_f[j] << " ";
        }


        /*
        for(int j=0; j<n; j++){
            cout << vec[j] << " ";
        }
        */
    }

    return 0;
}