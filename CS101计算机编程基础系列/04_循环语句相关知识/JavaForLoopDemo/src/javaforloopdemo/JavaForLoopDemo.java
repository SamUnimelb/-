package javaforloopdemo;

/**
 *
 * @author Sam_Yan
 */
public class JavaForLoopDemo {
    
    public static <T> void printArr(T[] arr){
        System.out.print("{ ");
        for(T each : arr)
            System.out.print(each + " ");
        System.out.println("}");
    }
    
    public static void main(String[] args) {
        String actions[] = {"��ע", "����", "ת��", "�ղ�", "����"};

        for(String action : actions) {
            System.out.println(action);
        }
        System.out.println("");
        printArr(actions);

        for (String action : actions) {
            action = "����";
        }

        System.out.println("");
        printArr(actions);

        for (int i = 0; i < 5; i++) {
            actions[i] = "���γɹ���";
        }
        System.out.println("");
        printArr(actions);
        
    }

}
