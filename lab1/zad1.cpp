#include<iostream>

using namespace std;


float epsilon(float curr){
    if(1.0f + curr/2 != 1.0f){
        return epsilon(curr/2);
    }
    else return curr;
}


double epsilon(double curr){
    if(1.0 + curr/2 != 1.0){
        return epsilon(curr/2);
    }
    else return curr;
}

int main(){
    cout << "epsilon dla floata: " << epsilon(1.0f) << endl;
    cout << "epsilon dla double'a: " << epsilon(1.0) << endl;

}