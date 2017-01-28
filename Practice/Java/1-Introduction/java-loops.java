/* https://www.hackerrank.com/challenges/java-loops */
import java.util.*;
import java.io.*;
//import java.Math.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            for(int j=0;j<n;j++)
            {
                int d = 0;
                for(int k=0;k<=j;k++)
                {
                    d+=(int)Math.pow(2,k);    // to find summation of power of 2
                }
             int c = (a+b*d);
             System.out.printf("%d ",c);
            }
            System.out.printf("%n");
        }
        in.close();
    }
}
