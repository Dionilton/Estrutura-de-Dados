#include <bits/stdc++.h>
using namespace std;

int main(){

    int x;
    cin >> x;
    for(int i = 0; i<x; i++){
        int n,m;
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

        float vec_f[n];
        for(int j=0; j <n; j++){
            vec_f[j] = (float((vec[j])))/(float((j+1)));
        }

        float sum = 0;
        for(int j=0; j<n; j++){
            for(int k=j; k<n; k++){
                sum += vec_f[k];
            }
        }

        if(sum == m){
            printf("YES\n");
        }
        else{
            printf("NO\n");
        }

        
    }

    return 0;
}