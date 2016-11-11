/*Paul Johnson
 * Solution to Mortgage Calculator - Calculate the monthly payments of a fixed
 term mortgage over given Nth terms at a given interest rate. Also figure out
 how long it will take the user to pay back the loan.
 */

package mortgagecalculator;


import java.util.Scanner;
public class MortgageCalc {
    private static Scanner scanner = new Scanner( System.in );

    public static void main(String[] args) {
         System.out.print( "What is your loan amount? " );
         String userIn = scanner.nextLine();
         float loanAmt = Float.parseFloat(userIn);
         System.out.print( "What is your interest rate? " );
         userIn = scanner.nextLine();
         float interest = Float.parseFloat(userIn);
         System.out.print( "How many years is your loan? " );
         userIn = scanner.nextLine();
         int payments = Integer.parseInt(userIn);
         interest = interest/1200;
         payments = payments * 12;
         double top;
         top = interest*Math.pow((1+interest), payments);
         double bottom;
         bottom = Math.pow((1+interest),payments)-1;
         double monthly = loanAmt*top/bottom;
         System.out.format("Your monthly payment is %.2f\n", monthly);
         System.out.format("And your total amount paid is %.2f\n", monthly*payments);
    
    }

}
