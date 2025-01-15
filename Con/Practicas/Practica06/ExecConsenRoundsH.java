import java.util.Arrays;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;



public class ExecConsenRoundsH {
    public static int[] winners;
    // Arreglo announce
    public volatile static int[] announce;
    // Arreglo para ver cuantas veces cada hilo realizo decide en cada ronda
    public volatile static int[] count;
    public static void task(CountDownLatch latch, CASConsensusH<Integer> cas, int c, int round){
        Thread thread = Thread.currentThread();
        long me = thread.getId();
        int id = (int) (me % c);
        // Veamos el valor preferido
        int prefer = round % c;
        // Revisamos si el hilo preferido no ha ganado
        // En caso de que no haya ganado usamos su id y si no, usamos el id del hilo actual
        prefer = announce[prefer] == -1 ? prefer : id;
        // Ejecutamos decide con el valor preferido
        //int winner = cas.decide(prefer, prefer); // version donde se hace pasar por el hilo que ayuda
        // Revisamos si el hilo ya realizo decide en esta ronda
        int winner;
        if (count[id] > 0) {
            winner = cas.dedice2(prefer, id);
        } else {
            winner = cas.decide(prefer, id);
            count[id] = count[id] + 1;
        }
        //System.out.println("Thread: "+ id + " hizo decide con prefer: " + prefer + " y id: " + id + " y regreso: " + winner);
        winners[round] = winner;// se guarda al ganador en el arreglo
        // Si ganamos actualizamos el arreglo announce
        if (winner == id) {
            announce[id] = id;
        }
        System.out.println("Thread: "+ id + " says WIN: " + winner);
        latch.countDown(); // Una vez que terminas, disminuyes el contador de "latch"
    }
    public static void main(String[] args) {
        int c = 4, rounds = 10; // c es el no. de hilos, rounds es el no. de rondas
        winners = new int[rounds];
        ExecutorService executor = Executors.newFixedThreadPool(c);//El candado solo funciona para dos hilos
		// Inicializamos el arreglo announce
        announce = new int[c];
        // Llenamos el arreglo announce con -1, lo que significa que no han ganado
        for (int i = 0; i < c; i++) {
            announce[i] = -1;
        }
        // Inicializamos el arreglo count
        count = new int[c];
        for (int j = 0; j < rounds; j++) {//Iteras en el no. de rondas
            // Inicializamos el arreglo count con 0
            for (int i = 0; i < c; i++) {
                count[i] = 0;
            }
            CountDownLatch latch =  new CountDownLatch(c);
            CASConsensusH<Integer> protocolCAS = new CASConsensusH<Integer>(c, -1);
            int currRound = j;
            System.out.println("Round: " + j);
            for (int i = 0; i < c; i++) { //creas "c" tareas, una por cada hilo
                executor.execute(() -> task(latch, protocolCAS, c, currRound)); 
            }
            try {
                latch.await(); // El hilo main espera a que los "c" hilos terminen
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            
        }

        System.out.println("\n Winners: " + Arrays.toString(winners)); 

        executor.shutdown();
		
		//while(!executor.isTerminated()) {};
        
    }
}