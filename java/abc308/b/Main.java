//package b;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        int m = Integer.parseInt(scanner.next());
        scanner.nextLine();
        String[] c = scanner.nextLine().split(" ");
        String[] d = scanner.nextLine().split(" ");
        int[] p = Arrays.stream(
                scanner.nextLine().split(" ")
                ).mapToInt(
                        Integer::parseInt
                ).toArray();
        scanner.close();

        Map<String, Integer> platesPrice = new HashMap<>();
        for (int i = 0; i < m; i++) platesPrice.put(d[i], p[i+1]);
        int res = 0;
        for (int i = 0; i < n; i++){
            if (platesPrice.containsKey(c[i])){
                res += platesPrice.get(c[i]);
            } else {
                res += p[0];
            }
        }
        System.out.println(res);
    }
}
