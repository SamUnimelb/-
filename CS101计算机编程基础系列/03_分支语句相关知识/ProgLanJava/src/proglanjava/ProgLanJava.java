package proglanjava;

import java.util.Scanner;

/**
 *
 * @author Sam_Yan
 */
public class ProgLanJava {

    public static void main(String[] args) {
        System.out.print("�������һѧ�ı�����ԣ�");
        Scanner input = new Scanner(System.in);
        String progLan =  input.next();
        
        if(progLan.equals("C") || progLan.equals("C++"))
            System.out.println("ϵͳ�ܹ�ר��");
        else if(progLan.equals("Java"))
            System.out.println("����ܹ�ר�ң����߶��ն˳���Ա");
        else if(progLan.equals("Python"))
            System.out.println("AI�����ݷ�����ʦ");
        else
            System.out.println("����ǰ�ˣ�");
        
    }
    
}
