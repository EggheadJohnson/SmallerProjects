/*Paul Johnson
 */

package anybase;

import java.util.Scanner;

public class AnyBase {
    private static Scanner scanner = new Scanner( System.in );

    public static String reverser(String s){
        String output = "";
        for (int x = 0; x < s.length(); x++){
            output = output + s.charAt(s.length()-x-1);
            
        }
        return output;
    }
    public static void main(String[] args) {
        int number;

        System.out.print( "What is the number you want converted? " );
        while(!scanner.hasNextInt()){
            System.out.print("That's not a number.\n");
            System.out.print("What is the number you want converted? ");
            scanner.next();
        }
        number = scanner.nextInt();


        
        System.out.print( "What is the base you want it in? " );
        int base;
        do{
            while(!scanner.hasNextInt()){
                System.out.print("That's not a number.");
                scanner.next();
            }
            base = scanner.nextInt();
        }while(base <= 0);
/*        double maxLength = Math.log(number)/Math.log(base);
        int ML = (int) maxLength;
        String answer = "";
        int power = ML;
        int conNum = number;
        int curr;
        double toThe;
        int toTheInt;
        while (power >= 0){
            toThe = Math.pow(base,power);
            toTheInt = (int) toThe;
            curr = conNum / toTheInt;
            answer = answer+curr;
            conNum = conNum%toTheInt;
            if (base > 10) answer = answer + " ";

            power--;
        }*/
        String answer = "";
        int conNum = number;
        while (conNum > 0){
            answer = answer+conNum%2;
            conNum = conNum/2;
        }
        answer = reverser(answer);
        System.out.println("The answer in base " + base + " is " + answer);
        
    }

}
