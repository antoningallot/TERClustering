#include "Point.h"
#include <iostream>
using namespace std;
   
Point::Point() : x(0), y(0) { }
Point::Point(float abs, float ord) : x(abs), y(ord) { }

void Point::display(){
    cout << "x :" << x << ", y : " << y;
}
