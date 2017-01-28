/* https://www.hackerrank.com/challenges/reduced-string */
// Referece Link: http://regexr.com/ 
//Regular expression: (.)\1
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        scan.close();
        
        while(true){
            int len = s.length();
            s = s.replaceAll("(.)\\1", ""); // providing regular expression of adjacent same letters
            if( s.length() == len ){
                break;
            }
        }

        System.out.println( (s.isEmpty()) ? "Empty String" : s);
    }
}