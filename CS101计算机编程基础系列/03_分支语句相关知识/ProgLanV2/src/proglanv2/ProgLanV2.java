package proglanv2;

import java.util.Scanner;

/**
 *
 * @author Sam_Yan
 */
public class ProgLanV2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.print("�������һѧ�ı�����ԣ�");
        Scanner input = new Scanner(System.in);
        String progLan =  input.next();
        
        switch(progLan){
            case "C":
            case "C++":
                System.out.println("ϵͳ�ܹ�ר��");
            break;
            
            case "Java":
                System.out.println("\"����ܹ�ר�ң����߶��ն˳���Ա\"");
            break;
            
            case  "Python":
                System.out.println("AI�����ݷ�����ʦ");
            break;
            
            default:
                System.out.println("����ǰ�ˣ�");
        }
        
    }
    
}
