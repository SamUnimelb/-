#include<iostream>
#include<cctype>
#include <time.h>

using namespace std;

int main(){
    srand(time(NULL));
    cout << (rand() % 100) / 100.0 << endl;
    /*int grade{0};
    cout << "Input your grade: ";
    cin >> grade;
    //string output = (grade >= 60? "passed":"failed");
    int output = (grade >= 60? 1:0);
    cout << output << endl;*/

    /*cout << "Input your ladder grade: ";
    string ladderGrade;
    cin >> ladderGrade;

    switch (toupper(ladderGrade[0]))
    {
    case 'A':
        cout << "�����㣬һֱ��������ɼ����к���ϣ��ѽ��" << endl;
        switch(toupper(ladderGrade[1])){
            case '+':
                cout << "GPA = 4.3��δ�����׵��ⷽ��ר��Ŷ��" << endl; break;
            case '-':
                cout << "GPA = 3.7���߼�ҵ�����ԱŶ��" << endl; break;
            default:
                cout << "GPA = 4.0��δ�����׵��ⷽ��ר��Ŷ��" << endl; break;
        }
    case 'B':
        if(toupper(ladderGrade[0]) != 'A'){
            cout << "���ſ�ҵ�����Ա�������ⷽ�濼�еĻ�����Ŭ��Ŷ��" << endl;
            switch(toupper(ladderGrade[1])){
                case '+':
                    cout << "GPA = 3.3���߼�ҵ�����ԱŶ��" << endl; break;
                case '-':
                    cout << "GPA = 2.7�����ˮƽ�Ѿ���ҵ���ˣ�" << endl; break;
                default:
                    cout << "GPA = 3.0��һ��ҵ�����ԱŶ��" << endl; break;
            }
        }
    case 'C':
        if(toupper(ladderGrade[0]) != 'A' && toupper(ladderGrade[0]) != 'B'){
            cout << "������ε�ˮƽ��ҵ���ˣ����鿼�б����ⷽ����Ŷ��" << endl;
            switch(toupper(ladderGrade[1])){
                case '+':
                    cout << "GPA = 2.3���������ν���ҵ���Ե�һ���ɼ���" << endl; break;
                default:
                    cout << "GPA = 2.0���������ν���ҵ���Ի���ñȽ϶��һ���ɼ���" << endl; break;
            }
        }
    case 'P':
        //C-�ǹ��˵ġ�
        if(toupper(ladderGrade[1]) != 'C' && toupper(ladderGrade[1]) != '-')
            cout << "��ϲ�����ſι��ˣ�" << endl;     
        break;
    default:
        cout << "�ܲ������ſ�����ˣ�" << endl;
        break;
    }*/

    system("pause");
    return 0;
}
