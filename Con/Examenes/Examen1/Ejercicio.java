import java.util.List;
import java.util.ArrayList;
import java.util.concurrent.Future;
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.ExecutionException;

public class Ejercicio {

    private static int[] task(FakePeterson lock, CounterNaive counter) {
        int[] valores = new int[2];
        valores[0] = 0;
        valores[1] = 0;
        long id = Thread.currentThread().getId();
        valores[0] = (int) id;
        int i = 0;
        try {
            lock.lock();
            i = counter.increment();
            // System.out.println(counter.getValue());
        } finally {
            lock.unlock();
        }
        valores[1] = i;
        return valores;
    }

    public static void main(String[] args) {
        FakePeterson lock = new FakePeterson();
        CounterNaive counter = new CounterNaive();
        List<Future<int[]>> futures = new ArrayList<Future<int[]>>();
        List<int[]> resultados = new ArrayList<int[]>();
        ExecutorService executor = Executors.newFixedThreadPool(2);
        for (int i = 0; i < 400; i++) {
            futures.add(executor.submit(() -> task(lock, counter)));
        }
        try {
            Thread.sleep(1000);
            executor.shutdown();
            for (int i = 0; i < futures.size(); i++) {
                while (!futures.get(i).isDone());
                int[] resultado = futures.get(i).get();
                resultados.add(resultado);
                System.out.println("El hilo " + resultado[0] + " aumento el contador a " + resultado[1]);
            }
            // Buscar el id de los hilos, buscan en resultado[0] cuatro valores
            int idHilo1 = 0;
            int idHilo2 = 0;
            int[] resultado1 = resultados.get(0);
            idHilo1 = resultado1[0];
            for (int i = 1; i < resultados.size(); i++) {
                int[] resultado = resultados.get(i);
                if (resultado[0] != idHilo1) {
                    idHilo2 = resultado[0];
                    break;
                }
            }
            int contadorHilo1 = 0;
            int contadorHilo2 = 0;
            for (int i = 0; i < resultados.size(); i++) {
                int[] resultado = resultados.get(i);
                if (resultado[0] == idHilo1) {
                    contadorHilo1++;
                } else {
                    contadorHilo2++;
                }
            }
            System.out.println("El hilo " + idHilo1 + " aumento el contador " + contadorHilo1 + " veces");
            System.out.println("El hilo " + idHilo2 + " aumento el contador " + contadorHilo2 + " veces");
            for (int i = 0; i < resultados.size(); i++) {
                int[] resultado = resultados.get(i);
                for (int j = 0; j < resultados.size(); j++) {
                    if (i != j) {
                        int[] resultado2 = resultados.get(j);
                        if (resultado[1] == resultado2[1]) {
                            System.out.println("El hilo " + resultado[0] + " y el hilo " + resultado2[0] + " aumentaron el contador a " + resultado[1]);
                        }
                    }
                }
            }
            System.out.println(counter.getValue());
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }
    
}
