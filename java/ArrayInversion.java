public class ArrayInversion {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4, 5 };
        for (int number : a) {
            System.out.print(number + " ");
        }
    }

    /*
     * Escribir una función que tome de entrada un arreglo de enteros, y su
     * tamaño, y que invierta el orden
     * de los n´umeros contenidos en el arreglo, escribiendo el resultado en el
     * mismo arreglo, y sin usar arreglo
     */
    public static int[] invertArray(final int[] a) {
        if (a.length == 1) {
            return a;
        } else if (a.length % 2 == 0) {
            int tmp;
            for (int i = 0; i <= (a.length / 2) - 1; i++) {
                tmp = a[i];
                a[i] = a[(a.length - 1) - i];
                a[(a.length - 1) - i] = tmp;
            }
            return a;
        }
        return null;
    }
}