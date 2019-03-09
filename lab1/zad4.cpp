#include <iostream>

using namespace std;

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
