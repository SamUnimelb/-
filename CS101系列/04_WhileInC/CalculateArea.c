#include <stdio.h>
#include "math.h"
#include <stdbool.h>

int main()
{
    /*bool wantToContinue = true;
    while (wantToContinue)
    {
        printf_s("%s", "������Բ�İ뾶������������˳���");
        double radius = 0.0;
        scanf("%lf", &radius);

        if (radius > 0)
        {
            double area = M_PI * powl(radius, 2.0);
            printf_s("Բ�����Ϊ��%.2lf\n", area);
        }
        else
            wantToContinue = false;
    }*/

    do    
    {
        printf_s("%s", "������Բ�İ뾶������������˳���");
        double radius = 0.0;
        scanf("%lf", &radius);

        if (radius > 0)
        {
            double area = M_PI * powl(radius, 2);
            printf_s("Բ�����Ϊ��%.2lf\n", area);
        }
        else break; //continue; 
    }while(true);

    system("pause");
    return 0;
}