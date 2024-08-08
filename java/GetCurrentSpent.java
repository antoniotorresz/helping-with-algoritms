import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class GetCurrentSpent {
    public static void main(String[] args) {

    }

    static int getMoneySpent(int[] keyboards, int[] drives, int b) {
        int spent = -1;
        for (int i = 0; i < keyboards.length; i++) {
            for (int j = 0; j < drives.length; j++) {
                int currentCost = keyboards[i] + drives[j];
                if (currentCost > b) {
                    continue;
                }
                if (currentCost > spent) {
                    spent = currentCost;
                }
            }
        }
        return spent;
    }

    public static int minimumDistances(final List<Integer> a) {
        List<Integer> distances = new ArrayList<Integer>();
        for (int i = 0; i < a.size(); i++) {
            for (int j = 0; j < a.size(); j++) {
                if (a.get(i) == a.get(j) && j > i) {
                    distances.add(j - i);
                }
            }
        }

        Collections.sort(distances);
        if (distances.size() == 0) {
            return -1;
        }
        return distances.get(0);
    }
}