/*Paul Johnson
 * Solution to Collatz Conjecture - Start with a number n > 1. Find the number
 of steps it takes to reach one using the following process: If n is even,
 divide it by 2. If n is odd, multiply it by 3 and add 1.
 */

package collatz;


import java.util.Scanner;
public class Main {
    private static Scanner scanner = new Scanner( System.in );
  
    public static void main(String[] args) {
         System.out.print( "What number would you like analyzed? " );
         String userIn = scanner.nextLine();
         int input = Integer.parseInt(userIn);
         int n = input;
         int counter = 0;
         while (n != 1){
             if (n%2 == 0) n = n/2;
             else n = n*3+1;
             counter++;
         }
         System.out.println(counter + " steps.");
    }

}
