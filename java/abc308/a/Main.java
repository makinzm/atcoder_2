import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] s = new int[8];
        for (int i = 0; i < 8; i++) {
            s[i] = Integer.parseInt(scanner.next());
        }
        scanner.close();

        Boolean flag = true;
        int last = 0;
        for (int i = 0; i < 8; i++) {
            if (s[i] < 100 || s[i] > 675 || s[i] % 25 !=0 || last > s[i]) {
                flag = false;
                break;
            }
            last = s[i];
        }
        String result = flag ? "Yes" : "No";
        System.out.println(result);
    }
}
