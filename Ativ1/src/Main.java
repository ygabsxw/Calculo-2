import java.util.*;

public class Main {
    private static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        Numbers numbers = read();
        Calculation calculation = new Calculation();
        double[] subrange = calculation.calculateLimit(numbers);
        printSubrange(subrange);
    }

    private static Numbers read() {
        Numbers numbers = new Numbers();
        System.out.println("This is a program to calculate the limit of a function in an interval.");
        System.out.println();
        System.out.println("Enter the first number: ");
        numbers.setA(sc.nextInt());
        sc.nextLine();
        System.out.println("Enter the second number: ");
        numbers.setB(sc.nextInt());
        sc.nextLine();
        System.out.println("Enter how many equal parts you want to divide the range into: ");
        numbers.setN(sc.nextInt());
        sc.nextLine();
        return numbers;
    }

    private static void printSubrange(double[] subrange) {
        System.out.println("The subrange is: ");
        for (int i = 0; i < subrange.length; i++) {
            System.out.printf("%.2f - ", subrange[i]);
        }
    }
}

