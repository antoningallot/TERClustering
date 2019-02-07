#include "Point.h"
#include <iostream>
using namespace std;

class Point {
   
    Point::Point(float abs, float ord) : x(abs), y(ord) { }

    void Point::display(){
        cout << "x :" << x << ", y : " << y;
    }
};