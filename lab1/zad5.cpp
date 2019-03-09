#include <iostream>
#include <vector>
#include <cmath>
#include <list>


#define MAXVAL 1.0f
#define MINVAL 0.0f

using namespace std;



float max(list<float> tab){
    float buff = tab.front();
    for(auto i = tab.begin(); i != tab.end(); ++i){
        if(*i > buff) buff = *i;
    }
    return buff;
}


float min(list<float> tab){
    float buff = tab.front();
    for(auto i = tab.begin(); i != tab.end(); ++i){
        if(*i < buff) buff = *i;
    }
    return buff;
}

float max(float a, float b){
    return a>b ? a : b;
}

list<float> k_mins( list<float> workingTab, int k, int n_buck){
    list<float> result;
    if(k == 0) return result;
    cout << 'D' << flush;
    
    float minim = min(workingTab);
    float maxim = max(workingTab);

    float min1 = 0;
    float max1= maxim - minim;

    vector<list<float>> buckets;
    buckets.resize(n_buck);


    for(auto tabElem = workingTab.begin(); tabElem != workingTab.end(); ++tabElem){
        buckets[floor(
            min((float)(n_buck-1), //min dlatego żeby maksymalna wartość nie trafiła do kubełka o numerze n_buck  
                max(n_buck+log2(*tabElem-minim), //wszystkie watrości mniejsze niż 2^(n_buck) do zerowego
                0.0f)))].push_back(*tabElem);
    }


    cout << "=========== POTRZEBUJE JESZCZE " << k <<" liczb ================\n";
    for(int i = 0; i < buckets.size(); i++){
        cout << "W kubelku nr " << i << " jest " << buckets[i].size() << "liczb" << endl; 
        if(buckets[i].size() <= k){
            result.merge(buckets[i]);
        }
        else{
            result.merge(k_mins(buckets[i], k - result.size(), n_buck));
            break;
        }
    }
    return result;
}


int main(){
    list<float> test = {2.5, 34, 5.3, 34.5, .43, 5.4, 2, 123094, 542, 0.0432423, 0.0432434};
    list<float> res = k_mins(test, 4, 256);

    for(auto i = res.begin(); i != res.end(); ++i) cout << *i << " ";
    cout << endl;
    return 0;
}