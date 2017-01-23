/*Paul Johnson
 * Solution to Fibonacci Sequence - Enter a number and have the program
 generate the Fibonacci sequence to that number or to the Nth number.
 */

package fibonacci;


import java.util.Scanner;
public class Main {
    private static Scanner scanner = new Scanner( System.in );
   
    public static void main(String[] args) {
         System.out.print( "How places of Fibonnaci would you like displayed? " );
         String userIn = scanner.nextLine();
         int input = Integer.parseInt(userIn);
         int[] fib = new int[input];
         fib[0] = 0;
         fib[1] = 1;
         for(int x = 2; x < input; x++){
             fib[x] = fib[x-1]+fib[x-2];

         }
         for(int x = 0; x < input; x++){
             System.out.println(fib[x]);
             if (fib[x] == input) break;
         }
    }

}
