/*
 * Paul Johnson
 * Solution to Change Return Program - The user enters a cost and then the
 amount of money given. The program will figure out the change and the number
 of quarters, dimes, nickels, pennies needed for the change.
 *
 *
 *
 */

package changereturn;


import java.util.Scanner;

public class ChangeReturn {
    private static Scanner scanner = new Scanner( System.in );

  
    public static void main(String[] args) {
        System.out.print( "What is the price of the item? " );
        String userIn = scanner.nextLine();
        float price = Float.parseFloat(userIn);
        price = price *100;
        System.out.print( "How much cash was tendered? " );
        userIn = scanner.nextLine();
        float cash = Float.parseFloat(userIn);
        cash = cash*100;
        int change = (int) cash - (int) price;
        //System.out.println(change);
        int dollars = change/100;
        change = change - dollars*100;
        int quarters = change/25;
        change = change%25;
        int dimes = change/10;
        change = change%10;
        int nickels = change/5;
        change = change%5;
        int pennies = change;
        System.out.println("Your change is:");
        if(dollars == 1) System.out.println("    " + dollars + " dollar");
        else System.out.println("    " + dollars + " dollars");
        if(quarters == 1) System.out.println("    " + quarters + " quarter");
        else System.out.println("    " + quarters + " quarters");
        if(dimes == 1) System.out.println("    " + dimes + " dime");
        else System.out.println("    " + dimes + " dimes");
        if(nickels == 1) System.out.println("    " + nickels + " nickel");
        else System.out.println("    " + nickels + " nickels");
        if(pennies == 1) System.out.println("    and " + pennies + " penny.");
        else System.out.println("    and " + pennies + " pennies.");


    }

}
