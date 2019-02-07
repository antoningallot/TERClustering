#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Instance {

    Instance::Instance(){
        
    }

    float min_compute (vector<vector<vector<float> > > d, int i, int I){
        float min = d[i][i][i+I];
        for (int k = i+1; k < i+I; k++){
            float tmp = d[i][k][i+I];
            if(tmp < min){
                min = tmp;
            }
        }
        return min;
    }

    vector<vector<float> > compute_matrix(int N){
        vector<vector<float> > c (N, vector<float>(N));
        for (int i = 0; i < N; i++){
            //c[i].resize(N);
            for (int j = i; j < N; i++){
                c[i][j] = 0;
            }
        }

        vector<vector<float> > tmp (N, vector<float>(N));
        vector<vector<vector<float> > > d (N, tmp);
        for (int i = 0; i < N; i++){
            //d[i].resize(N);
            for (int I = i; I < N; I++){
                //d[i][I].resize(N);
                for(int j = 0; j < N; j++){
                    d[i][I][j] = 0;
                }
            }
        }

        for (int I = 1; I < N; I++){
            for (int i = 0; i < N-I; i++){
                for (int k = i; k < i+I; k++){
                    d[i][k][i+I] = d[i][k][i-I] + abs(d[i][k][i-I]-d[i][k][i-I]);
                }
                c[i][i+I] = min_compute(d, i, I);
            }
        }
        return c;
    }

    float min_DP(vector<vector<float> > compute, vector<vector<float> > C, int i, int k){
        float min = C[0][k-1] + compute[1][i];
        for (int j = 2; j < i; j++){
            float tmp = C[j-1][k-1] + compute[j][i];
            if(tmp < min){
                min = tmp;
            }
        }
        return min;
    }

    float DP(vector<vector<float> > compute, int N, int K){
        vector<vector<float> > C (N, vector<float> (N));
        for (int i = 0; i < N; i++){
            C[i][1] = compute[1][i];
            for (int k = 2; k < K; k++){
                C[i][k] = min_DP(compute, C, i, k);
            }
        }
        return C[N][K];
    }

    float backtrack(vector<vector<float> > compute, vector<vector<float> > C, int N, int K){
        
    }
};