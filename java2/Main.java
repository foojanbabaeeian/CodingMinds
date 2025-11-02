package java2;

public class Main {
    public static int mystery(int x, int y)
        {
            if (y == 1) {
                return x;
            }
            else {
                return x + mystery(x, y-1);
            }
        }
    public static void main(String[] args) {
        mystery(0, 0);

    }
}
