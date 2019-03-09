#include<iostream>
#include<iomanip>
#include<ctime>
#define e7 10000000
#define C 0.3728
using namespace std;

float recsum(float* tab, int start, int end);
float normal_sum();
float kahanSum(float* tab, int len) {
    float sum = tab[0];
    float compensate = 0.0;
    float tmp, buf;
    for(int i = 1; i < len; i++){
        tmp = tab[i] - compensate;
        buf = sum + tmp;
        compensate = (buf - sum) - tmp;
        sum = buf;
    }
    return sum;
}


float *tab;
int main(){
    cout << setprecision(12);
    clock_t start, end;

    tab = new float[e7];
    for(int i = 0; i < e7; i++) tab[i] = C;

    start = clock();
    float sum = normal_sum();
    end = clock();
    cout << "\nNormal adding time elapsed: " << (end-start)*1.0/CLOCKS_PER_SEC << " ===========";
    cout << "\nSUM/ERROR/RERROR  " <<sum<<" "<< (e7*C - sum) <<" " << (e7*C - sum)/(C*e7) <<  endl;


    start = clock();
    sum = recsum(tab,0, e7-1);
    end = clock();
    cout << "\nRecursive adding time elapsed: " << (end-start)*1.0/CLOCKS_PER_SEC << " ===========";
    cout << "\nSUM/ERROR/RERROR  " <<sum<<" "<< (e7*C - sum) <<" " << (e7*C - sum)/(C*e7) <<  endl;


    start = clock();
    sum = kahanSum(tab, e7);
    end = clock();
    cout << "\nKahan adding time elapsed: " << (end-start)*1.0/CLOCKS_PER_SEC << " ===========";
    cout << "\nSUM/ERROR/RERROR  " <<sum<<" "<< (e7*C - sum) <<" " << (e7*C - sum)/(C*e7) <<  endl;

}

float normal_sum(){
   
    float sum = 0;

    for(int i = 0; i < e7; i++){
        sum += tab[i];
        if(i % 25000 == 0){

           // cout << i<< ": " << (i*C - sum) << endl;
           cout <<sum<<" "<< (i*C - sum) <<" " << (i*C - sum)/(C*e7) <<  endl;
        }
    } 
    cout << "#DATA_END\n";
    return sum;
}

float recsum(float* tab, int start, int end){
    if(start == end) return tab[start];
    int mid = start + (end-start)/2;
    return recsum(tab, start, mid) + recsum(tab, mid+1, end);
}