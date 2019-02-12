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
    ifstream file (filename);
    file >> taille;
    file >> dimension;
    taille = min(n, taille);
    while (cpt <= taille){
        if(file.is_open()){
            file >> x;
            file >> y;
            Point p(x, y);
            res.push_back(p);
            taille++;
        }
    }
    file.close();
    return res;
}

void display(vector<Point> tab) {
    int i;
    for(i = 0; i < tab.size(); i++){
        tab[i].display();
    }
}

int main () {
    vector<Point> tab = parsing(50, "data.txt");
    display(tab);
    
    return 0;
}