#include <iostream>
#include <vector>
#include <bits/stdc++.h> 
#include <ctime>
#include <cstdlib>


using namespace std;

class Matrix{
public:
    vector<vector<float>> data;
    size_t dimX, dimY;

    void setVal(size_t x, size_t y, float val){
        data[x][y] = val;
    }

    float getVal(size_t x, size_t y){
        return data[x][y];
    }

    vector<float> operator *(vector<float> vec){
        if(dimY != vec.size()) return vector<float>();
        
        vector<float> res;
        res.resize(dimY);
        for(int i = 0; i < dimY; i++){
            for(int j = 0; j < dimX; j++){
                res[i] += data[i][j] * vec[j];
            }
        }
        return res;
    }

};


struct Coord{
    size_t x, y;
    float val;
};

Coord getCoord(size_t y, size_t x, float val){
    Coord tmp;
    tmp.x = x;
    tmp.y = y;
    tmp.val = val;
    return tmp;
}

bool operator < (const Coord &c1, const Coord &c2) {
    if(c1.y < c2.y) return true;
    else return (c1.y == c2.y && c1.x < c2.x);
}

bool operator > (const Coord &c1, const Coord &c2) {
    if(c1.y > c2.y) return true;
    else return (c1.y == c2.y && c1.x > c2.x);
}


class COOMatrix{
public:

    size_t dimX, dimY;
    vector<Coord> data;

    COOMatrix (size_t x, size_t y){
        dimX = x;
        dimY = y;
    }

    COOMatrix (){
        dimX = 0;
        dimY = 0;
    }

    bool setVal(size_t x, size_t y, float val){
        if(x > dimX || y > dimY) return false;

        for (auto i = data.begin(); i != data.end(); ++i){
            if( i->x == x && i->y == y){
                if(val == 0){
                    data.erase(i);
                }
                else{
                    i->val = val;
                }
                return true;
            }
        }
        Coord tmp;
        tmp.x = x;
        tmp.y = y;
        tmp.val = val;
        data.push_back(tmp);
        sort(data.begin(), data.end());
    }


    vector<float> operator * (vector<float> &vec){
        
        if(this->dimY != vec.size()) return vector<float>();

        vector<float> result;
        result.resize(vec.size());


        for(Coord c : data){
            result[c.y] += c.val * vec[c.x];
        }

        return result;
    } 

    // void print (){
    //     for(int i = 0; i < dimY; i++){
    //         for(int j = 0; j< dimX; j++){
    //             if(data)
    //         }
    //     }
    // }


};

struct CSRCoord{
    float val;
    size_t col;
};

CSRCoord getCrec(size_t col, float val){
    CSRCoord tmp;
    tmp.col = col;
    tmp.val = val;

    return tmp;
}

class CSRMatrix{
    public:

    size_t dimX, dimY;
    vector<CSRCoord> colTable;
    vector<size_t> offset; 




    vector<float> operator * (vector<float> &vec){
        
        if(this->dimY != vec.size()) return vector<float>();

        vector<float> result;
        result.resize(vec.size());


        for(size_t i = 0; i < vec.size(); i++){
            for(size_t j = offset[i]; j < offset[i+1]; j++){
                result[i] += colTable[j].val * vec[colTable[j].col]; 
            }
            
        }



        return result;
    } 

};

class ELLMatrix{
public:
    int MAX_ELEM_ROW;
    size_t dimX, dimY;

    vector<vector<float>> values;
    vector<vector<int>> columns;

    vector<float> operator * (vector<float> &vec){
        
        if(this->dimY != vec.size()) return vector<float>();

        vector<float> result;
        result.resize(vec.size());


        for(size_t i = 0; i < dimY; i++){
            for(size_t j = 0; j < MAX_ELEM_ROW; j++){
                if(columns[i][j] == -1) continue;
                result[i] += vec[columns[i][j]] * values[i][j]; 
            }
        }

        return result;
    } 
};

void print_vec(vector<float> v){
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
    cout << endl;
}

int main(){

    vector <float> v {1,2,5};
    Matrix m;
    m.dimX = 3;
    m.dimY = 3;
    m.data.push_back(vector<float>{3,0,2});
    m.data.push_back(vector<float>{0,1,2});
    m.data.push_back(vector<float>{2,0,1});


    print_vec(m * v);

    COOMatrix mo;
    mo.dimX = 3;
    mo.dimY = 3;
    mo.data.push_back(getCoord(0, 0, 3));
    mo.data.push_back(getCoord(0, 2, 2));
    mo.data.push_back(getCoord(1, 1, 1));
    mo.data.push_back(getCoord(1, 2, 2));
    mo.data.push_back(getCoord(2, 0, 2));
    mo.data.push_back(getCoord(2, 2, 1));

    print_vec(mo * v);

    CSRMatrix mc;
    mc.dimX = 3;
    mc.dimY = 3;
    mc.colTable.push_back(getCrec(0,3));
    mc.colTable.push_back(getCrec(2,2));
    mc.colTable.push_back(getCrec(1,1));
    mc.colTable.push_back(getCrec(2,2));
    mc.colTable.push_back(getCrec(0,2));
    mc.colTable.push_back(getCrec(2,1));

    mc.offset.push_back(0);
    mc.offset.push_back(2);
    mc.offset.push_back(4);
    mc.offset.push_back(6);
    print_vec(mc * v);

    ELLMatrix ml;
    ml.dimY = 3;
    ml.dimX = 3;

    ml.MAX_ELEM_ROW= 2;
    ml.columns.push_back(vector<int>{0,2});
    ml.columns.push_back(vector<int>{1,2});
    ml.columns.push_back(vector<int>{0,2});

    ml.values.push_back(vector<float>{3,2});
    ml.values.push_back(vector<float>{1,2});
    ml.values.push_back(vector<float>{2,1});

    print_vec(ml * v);

    srand(time(NULL));

    const size_t DIMX = 6000;
    const size_t DIMY = 6000;
    const int  ZEROPROB = 80;
    
    const float LO = 0;
    const float HI = 1000;

    Matrix testm;
    testm.dimX = DIMX;
    testm.dimY = DIMY;

    testm.data.resize(DIMY);

    float tmpV;

    for(int i = 0; i < DIMX; i++){
        for(int j = 0; j < DIMY; j++){
            if(rand() % 100 < ZEROPROB){
                tmpV = 0;
            }
            else
            {
                tmpV = LO + static_cast <float> (rand()) /( static_cast <float> (RAND_MAX/(HI-LO)));
            }
            testm.data[i].push_back(tmpV);
        }
    }

    vector<float> vec;
    vec.resize(DIMY);
    for(int i = 0; i <  DIMY; i ++){
        vec[i] = LO + static_cast <float> (rand()) /( static_cast <float> (RAND_MAX/(HI-LO)));
    }

    clock_t start, end;

    start = clock();
    auto a = testm * vec;
    end = clock();
    a = a;
    
    cout << "\nNormal version time elapsed: " << (end-start)*1.0/CLOCKS_PER_SEC << " ===========\n";

    COOMatrix testo;
    testo.dimX = DIMX;
    testo.dimY = DIMY;
     for(int i = 0; i < DIMX; i++){
        for(int j = 0; j < DIMY; j++){
            if(rand() % 100 < ZEROPROB) continue;
            testo.data.push_back(getCoord(i, j, LO + static_cast <float> (rand()) /( static_cast <float> (RAND_MAX/(HI-LO)))));
        }
     }
    start = clock();
    auto ao = testo * vec;
    end = clock();
    ao= ao;
    
    cout << "\nNormal version time elapsed: " << (end-start)*1.0/CLOCKS_PER_SEC << " ===========\n";

    CSRMatrix testc;
    testc.dimX = DIMX;
    testc.dimY = DIMY;
    int cntr = 0;
    testc.offset.push_back(cntr);
     for(int i = 0; i < DIMY; i++){
        for(int j = 0; j < DIMX; j++){
            if(rand() % 100 < ZEROPROB) continue;
            testc.colTable.push_back(getCrec(j, LO + static_cast <float> (rand()) /( static_cast <float> (RAND_MAX/(HI-LO)))));
            cntr++;
        }
        testc.offset.push_back(cntr);
     }

     start = clock();
    auto ac = testc * vec;
    end = clock();
    ac= ac;
    
    cout << "\nNormal version time elapsed: " << (end-start)*1.0/CLOCKS_PER_SEC << " ===========\n";

    ELLMatrix teste;
    teste.dimX = DIMX;
    teste.dimY = DIMY;
    vector<int> tmpcol;
    vector<float> tmpVal;
    teste.MAX_ELEM_ROW = static_cast<int>(DIMX*ZEROPROB/100);
     for(int i = 0; i < DIMY; i++){
        for(int j = 0; j < teste.MAX_ELEM_ROW; j++){
            tmpVal.push_back(LO + static_cast <float> (rand()) /( static_cast <float> (RAND_MAX/(HI-LO))));
            tmpcol.push_back(rand() % DIMX);
        }
        teste.columns.push_back(tmpcol);
        teste.values.push_back(tmpVal);
        tmpcol.clear();
        tmpVal.clear();
     }

    start = clock();
    auto ae = teste * vec;
    end = clock();
    ae= ae;
    
    cout << "\nELL    version time elapsed: " << (end-start)*1.0/CLOCKS_PER_SEC << " ===========\n";



    

}