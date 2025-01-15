public class DeterminanteConcurrenteRunnable implements Runnable{
    static int determinante;
    static int n_prueba = 3;
    static int matriz_prueba[][] = { { 1, 2, 2 }, { 1, 0, -2 }, { 3, -1, 1 }};
    int num1, num2, num3, partial;
    
    public DeterminanteConcurrenteRunnable(int num1, int num2, int num3) {
        this.num1 = num1;
        this.num2 = num2;
        this.num3 = num3;
    }
    
    public static int determinanteMatriz3x3(int matriz[][], int n_prueba) {
        int result = 0;
        DeterminanteConcurrenteRunnable thr1 = new DeterminanteConcurrenteRunnable(matriz[0][0], matriz[1][1], matriz[2][2]);
        DeterminanteConcurrenteRunnable thr2 = new DeterminanteConcurrenteRunnable(matriz[1][0], matriz[2][1], matriz[0][2]);
        DeterminanteConcurrenteRunnable thr3 = new DeterminanteConcurrenteRunnable(matriz[2][0], matriz[0][1], matriz[1][2]);
        DeterminanteConcurrenteRunnable thr4 = new DeterminanteConcurrenteRunnable(matriz[2][0], matriz[1][1], matriz[0][2]);
        DeterminanteConcurrenteRunnable thr5 = new DeterminanteConcurrenteRunnable(matriz[1][0], matriz[0][1], matriz[2][2]);
        DeterminanteConcurrenteRunnable thr6 = new DeterminanteConcurrenteRunnable(matriz[0][0], matriz[2][1], matriz[1][2]);
        Thread t1 = new Thread(thr1);
        Thread t2 = new Thread(thr2);
        Thread t3 = new Thread(thr3);
        Thread t4 = new Thread(thr4);
        Thread t5 = new Thread(thr5);
        Thread t6 = new Thread(thr6);
        t1.start();
        t2.start();
        t3.start();
        t4.start();
        t5.start();
        t6.start();
        try{
            t1.join();
            t2.join();
            t3.join();
            t4.join();
            t5.join();
            t6.join();
        }catch(InterruptedException e) {}
        result = thr1.partial + thr2.partial + thr3.partial - thr4.partial - thr5.partial - thr6.partial;
        return result;
    }
    
    @Override
    public void run(){
        this.partial = this.num1 * this.num2 * this.num3;
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        long startTime = System.nanoTime();
        determinante = determinanteMatriz3x3(matriz_prueba, n_prueba);
        long endTime = System.nanoTime();
        System.out.println("Program took " +
                (endTime - startTime) + "ns, result: " + determinante) ;

    }
    
}