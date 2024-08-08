import java.util.HashMap;

public class EncryptAlgorithm {
    public static void main(String[] args) {
        System.out.println(encryption("chillout"));
        System.out.println(encryption("have a nice day"));
        System.out.println(encryption("feed the dog"));
    }

    public static String encryption(final String s) {
        HashMap<String, Object> res = buildInitialMatrix(s.replace(" ", ""));
        String[][] sMatrix = (String[][]) res.get("matrix");
        int rows = (int) res.get("rows");
        int columns = (int) res.get("columns");
        String encryptedString = "";
        //traverse the matrix has encrypt algorithm
        for (int column = 0; column < columns; column++) {
            String word = "";
            for (int row = 0; row < rows; row++) {
                word += sMatrix[row][column];
            }
            encryptedString += word + " ";
        }
        return encryptedString.replaceFirst(".$", "");
    }

    public static HashMap<String, Object> buildInitialMatrix(final String s) {
        int columns = (int) Math.ceil(Math.sqrt(s.length()));
        int rows = columns - 1;
        char[] letters = s.replace(" ", "").toCharArray();
        String[][] initialMatrix;
        int sIdx = 0;
        HashMap<String, Object> data = new HashMap<>();

        while (rows * columns < s.length()) {
            rows++;
        }

        initialMatrix = new String[rows][columns];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                initialMatrix[i][j] = "";
            }
        }

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (sIdx < letters.length) {
                    initialMatrix[i][j] = String.valueOf(letters[sIdx]);
                    sIdx++;
                } else {
                    break;
                }
            }
        }

        data.put("matrix", initialMatrix);
        data.put("rows", rows);
        data.put("columns", columns);
        return data;
    }
}