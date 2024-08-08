import java.util.ArrayList;
import java.util.List;

public static void main(String args[]) {
    applesAndOranges(7, 11, 5, 15, new int[]{-2, 2, 1}, new int[]{5, -6});
}

public static void applesAndOranges(int s, int t, int a, int b, int[] apples, int[] oranges) {
    List<Integer> houseRange = new ArrayList<Integer>();
    Integer fallenApples = 0;
    Integer fallenOranges = 0;

    for (Integer i = s; i <= t; i++) {
        houseRange.add(i);
    }
    for (Integer apple : apples) {
        Integer fallPos = a + apple;
        if (houseRange.contains(fallPos)) {
            fallenApples += 1;
        }
    }
    for (Integer orange : oranges) {
        Integer fallPos = b + orange;
        if (houseRange.contains(fallPos)) {
            fallenOranges += 1;
        }
    }
}