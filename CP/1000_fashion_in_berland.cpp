#include <bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cin >> n;
    int vec[n];
    for(int i =0; i<n; i++){
        cin >> vec[i];
    }

    int controle = 0;
    if(n == 1){
        if(vec[0] == 1){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
    }
    else if(n > 1){
        for(int i=0; i<n; i++){
            if(vec[i] == 0){
                controle++;
            }
            if(controle > 1){
                cout << "NO" << endl;
                break;
            }
        }
        if(controle == 1){
            cout << "YES" << endl;
        }
        else if(controle == 0){
            cout << "NO" << endl;
        }
    }
}