/* https://www.hackerrank.com/challenges/java-string-compare */
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        String str = scan.next();
        int n = scan.nextInt();
        SortedSet<String> sets = new TreeSet<String>();
        for(int i = 0 ; i<=str.length()-n ; i++){
            //System.out.println(str.substring(i,i+n)); // Generate all substring of n length
            sets.add(str.substring(i,i+n));    
        }       
        System.out.println(sets.first());
        System.out.println(sets.last());
    }
    
    
    
}