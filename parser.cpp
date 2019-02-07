#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
#include "Point.h"
using namespace std;

// Créer une instance dans laquelle tout stocker
// vector<point> + taille vector + taille données en attributs privés de cette instance
// matrices et données utilisées dans calculs intermédiaires en attributs privés aussi
vector<Point> parsing (int n, string filename) {
    vector<Point> res (n);
    float x, y;
    int taille, dimension;
    int cpt = 0;
    string filename;
    ifstream file (filename);
    file >> taille;
    file >> dimension;
    taille = min(n, taille);
    while (cpt <= taille){
        if(file.is_open()){
            file >> x;
            file >> y;
            Point p = Point(x, y);
            res.push_back(p);
            taille++;
        }
    }
    file.close();
    return res;
}

void display(vector<float,float> tab) {
    int i;
    for(i = 0; i < tab.size(); i++){
        cout << get<0>(tab[i]) << " " get<1>(tab[i]) << "\n";
    }
}

int main () {
    vector<float, float> tab = parsing(50, "dataAleaBox_5_60_100_ex0.txt");
    display(tab);
    
    return 0;
}