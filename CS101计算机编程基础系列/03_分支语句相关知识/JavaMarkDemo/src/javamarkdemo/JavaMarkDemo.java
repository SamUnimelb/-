package javamarkdemo;

import java.util.Scanner;

/**
 *
 * @author Sam_Yan
 */
public class JavaMarkDemo {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.print("������߿�������");
        Scanner input = new Scanner(System.in);
        int mark = input.nextInt();
        
        if(mark >= 594){
            System.out.println("���Ϻܺõ�ѧУ");
            System.out.println("��΢ѧϰһ��");
        }else{
            System.out.println("����һ���ѧУ");
            System.out.println("ͨ������Ŭ����ѧϰ����������ʵϰ����Ŀ");
            System.out.println("׼������������������Ŭ��ӦƸ");
        }
        
        System.out.println("��Ϊ�󳧼�����ţ");
        System.out.println("ӭȢ�׸���");
        System.out.println("���������۷�");
        
    }
    
}
