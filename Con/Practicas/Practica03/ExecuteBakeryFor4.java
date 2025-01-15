import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.CountDownLatch;


public class ExecuteBakeryFor4 {
    
    // Diccionario concurrente para contar el numero de veces que un thread incrementa el contador.
    private static ConcurrentHashMap<Integer, Integer> threadIncrements = new ConcurrentHashMap<>();

    public static void take(BakeryFor4 lock, CounterNaive counter, int threadID) {
        //System.out.println("Before lock thread " + threadID);
        lock.lock(threadID);
        //System.out.println("After lock thread" + threadID);
        try {
            Thread.sleep(200); // Simulamos una tarea
            counter.increment();

            
            System.out.println("Hilo " + threadID + " incremento el contador. Valor actual: " + counter.getValue());

            // Update the increment count for the current thread
            threadIncrements.merge(threadID, 1, Integer::sum);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock(threadID);
        }
    }

    public static void main(String[] args) {
        BakeryFor4 lock = new BakeryFor4(4);
        CounterNaive counter = new CounterNaive();
        // Para saber cuando todas las tareas han terminado de correr
        CountDownLatch latch = new CountDownLatch(400); // Porque tenemos 400 tareas
        ExecutorService executor = Executors.newFixedThreadPool(4);
        for (int i = 0; i < 400; i++) {
            final int threadID = i % 4; // Distribuimos las tareas entre 4 hilos
            executor.execute(() -> {
                try{
                    take(lock, counter, threadID);
                }finally{
                    latch.countDown();
                }
            });
        }
        try {
            // Esperamos a que terminen todos los threads
            latch.await();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally{
            executor.shutdown();
        }
        
        System.out.println("Valor final del contador: " + counter.getValue());

        System.out.println("Conteo de incrementos por thread: " + threadIncrements);
    }
}

