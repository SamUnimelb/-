#include<iostream>
#include<cmath>

using namespace std;

int main(){
    cout << "������뾶: ";
    double radius = 0.0;
    cin >> radius;

    double area = M_PI * pow(radius, 2);
    cout << "Բ�����Ϊ��" << area << endl;

    system("pause");
    return 0;
}
