public class DeterminanteConcurrente2 extends Thread{
    static int determinante;
    static int n_prueba = 3;
    static int matriz_prueba[][] = { { 1, 2, 2 }, { 1, 0, -2 }, { 3, -1, 1 }};
    int num1, num2, num3, partial;
    int num4, num5, num6, partial2;
    int num7, num8, num9, partial3;
    
    public DeterminanteConcurrente2(int num1, int num2, int num3, int num4, int num5, int num6, int num7, int num8, int num9) {
		this.num1 = num1;
		this.num2 = num2;
		this.num3 = num3;
        this.num4 = num4;
		this.num5 = num5;
		this.num6 = num6;
        this.num7 = num7;
		this.num8 = num8;
		this.num9 = num9;
	}
    
    public static int determinanteMatriz3x3(int matriz[][], int n_prueba) {
        int result = 0;
        DeterminanteConcurrente2 thr1 = new DeterminanteConcurrente2(matriz[0][0], matriz[1][1], matriz[2][2], matriz[2][0], matriz[0][1], matriz[1][2], matriz[1][0], matriz[0][1], matriz[2][2]);
        DeterminanteConcurrente2 thr2 = new DeterminanteConcurrente2(matriz[1][0], matriz[2][1], matriz[0][2], matriz[2][0], matriz[1][1], matriz[0][2], matriz[0][0], matriz[2][1], matriz[1][2]);
        thr1.start();
		thr2.start();
        try{
			thr1.join();
			thr2.join();
		}catch(InterruptedException e) {}
        result = thr1.partial + thr2.partial + thr1.partial2 - thr2.partial2 - thr1.partial3 - thr2.partial3;
       
        return result;
    }
    
    public void run(){
    	this.partial = this.num1 * this.num2 * this.num3;
        this.partial2 = this.num4 * this.num5 * this.num6;
        this.partial3 = this.num8 * this.num7 * this.num9;
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
