public class DeterminanteSecuencial {
    public static void main(String[] args) {
        int determinante;
        int n_prueba = 3;
        int matriz_prueba[][] = { { 1, 2, 2 }, { 1, 0, -2 }, { 3, -1, 1 }};
        long startTime = System.nanoTime();
        determinante = determinanteMatriz3x3(matriz_prueba, n_prueba);
        long endTime = System.nanoTime();
        System.out.println("Program took " +
                (endTime - startTime) + "ns, result: " + determinante) ;
    }

    public static int determinanteMatriz3x3(int matriz[][], int n_prueba) {
        int result = 0;
        result = matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[1][0] * matriz[2][1] * matriz[0][2] + matriz[2][0] * matriz[0][1] * matriz[1][2] - matriz[2][0] * matriz[1][1] * matriz[0][2] - matriz[1][0] * matriz[0][1] * matriz[2][2] - matriz[0][0] * matriz[2][1] * matriz[1][2];
        return result;
    }

}
