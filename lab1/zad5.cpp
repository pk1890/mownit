#include <iostream>
#include <vector>
#include <cmath>
#include <list>
#include <ctime>

#define MAXVAL 1.0f
#define MINVAL 0.0f

using namespace std;



float max(const list<float> tab){
    float buff = tab.front();
    for(auto i = tab.begin(); i != tab.end(); ++i){
        if(*i > buff) buff = *i;
    }
    return buff;
}


float min(const list<float> tab){
    float buff = tab.front();
    for(auto i = tab.begin(); i != tab.end(); ++i){
        if(*i < buff) buff = *i;
    }
    return buff;
}

float max(float a, float b){
    return a>b ? a : b;
}

list<float> k_mins( const list<float> workingTab, int k, int n_buck){
    list<float> result;
    if(k == 0) return result;
    //cout << 'D' << flush;
    
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


    //cout << "=========== POTRZEBUJE JESZCZE " << k <<" liczb ================\n";
    for(int i = 0; i < buckets.size(); i++){
     //   cout << "W kubelku nr " << i << " jest " << buckets[i].size() << "liczb" << endl; 
        if(result.size() + buckets[i].size() <= k){
            result.merge(buckets[i]);
        }
        else{
            result.merge(k_mins(buckets[i], k - result.size(), n_buck));
            break;
        }
    }
    return result;
}

list<float> classic_k_mins(list<float> workingTab, int k){
    workingTab.sort();
    list<float> res;
    int it = 0;
    for(auto i = workingTab.begin(); i != workingTab.end() && it < k; ++i){
        res.push_back(*i);
        it++;
    }
    return res;
}


int main(){
    srand(time(NULL));
    list<float> test = {2.5, 34, 5.3, 34.5, .43, 5.4, 2, 123094, 542, 0.0432423, 0.0432434};
    list<float> test2;
    const float LIM = 3;
    const int K = 10;



    clock_t start, end;
    list<float> res;

    for(int N = 100; N <= 10000000; N*=10){
        test2.clear();
        cout << "\n\nTesting 10 min of " << N << " numbers\n";

        for(int i = 0; i < N; i++){
            test2.push_back(static_cast <float> (rand()) / (static_cast <float> (RAND_MAX/LIM)));
        }

        start = clock();
        res = k_mins(test2, K, 256);
        end = clock();
        res.sort();

        cout << "\nExercise version time elapsed: " << (end-start)*1.0/CLOCKS_PER_SEC << " ===========\n";
        for(auto i = res.begin(); i != res.end(); ++i) cout << *i << " ";

        start = clock();
        res = classic_k_mins(test2, K);
        end = clock();
        cout << "\nNormal version time elapsed: " << (end-start)*1.0/CLOCKS_PER_SEC << " ===========\n";
        res.sort();
        for(auto i = res.begin(); i != res.end(); ++i) cout << *i << " ";
        cout << endl;
    }
    return 0;
}