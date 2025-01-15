import java.util.concurrent.atomic.AtomicIntegerArray;

public class BakeryFor4 {
    /*
     * Usamos AtomicIntegerArray ya que nos permite hacer operaciones thread-safe sobre arreglos,
     * ofreciendo un comportamiento similar a una variable volatile.
     */
    private final AtomicIntegerArray flag;  
    private final AtomicIntegerArray label; 
    
    public BakeryFor4(int numThreads) {
        flag = new AtomicIntegerArray(numThreads);
        label = new AtomicIntegerArray(numThreads);
        
        for (int i = 0; i < numThreads; i++) {
            flag.set(i, 0);  // 0 significa que no queremos entrar a la seccion critica
            label.set(i, 0); // Sin label al principio
        }
    }

    public void lock(int threadID) {
        int n = flag.length();
        flag.set(threadID, 1);  // 1 representa que queremos entrar a la seccion critica
        int maxLabel = 0;
        
        
        for (int i = 0; i < n; i++) {
            int labelValue = label.get(i);
            maxLabel = Math.max(maxLabel, labelValue);
        }
        label.set(threadID, maxLabel + 1);
        flag.set(threadID, 2);  // 2 representa que tenemos un label y esperamos a entrar a la seccion critica
        
        // Esperamos nuestro turno
        for (int i = 0; i < n; i++) {
            while (i != threadID && flag.get(i) != 0 && (label.get(i) < label.get(threadID) || 
            (label.get(i) == label.get(threadID) && i < threadID))) {
            }
        }
    }

    public void unlock(int threadID) {
        flag.set(threadID, 0);  // Terminamos con la seccion critica
    }
}

