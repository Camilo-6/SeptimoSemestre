import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Tarea implements Runnable {
    
    int task;
    Semaphore semaphore;
    static Lock lock = new ReentrantLock();

    public Tarea(int i, Semaphore semaphore){
        this.task = i;
        this.semaphore = semaphore;
    }

    @Override
    public void run() {
        Thread currentThread = Thread.currentThread();
        long id = currentThread.getId();

        // Con el lock nos aseguramos que solo una tarea por persona es aceptada
        lock.lock();
        try{
            System.out.println("Tarea " + task + " enviada por :" + id);
        }finally{
            lock.unlock();
        }

        // Despues de que la tarea haya sido enviada, podemos ejecutar a lo mas 3 tareas al mismo tiempo
        try{
            semaphore.acquire();
            try {
                // Simulamos cuanto tiempo tarda la ejecucion de cada tareas
                int value = (int) (id % 6);
                int tiempoTarea = switch(value) {
                    case 0, 2 -> 500;
                    case 1 -> 2000;
                    default -> 3000;
                };

                System.out.println("Ejecutando tarea " + task + " por hilo " + id + " durante " + tiempoTarea + " ms");
                Thread.sleep(tiempoTarea); // Inicia la tarea

                System.out.println("Tarea " + task + " completada por el hilo " + id);
            } finally {
                // Termina la tarea
                semaphore.release();
            }
        } catch (InterruptedException e) {
            System.out.println("Tarae interrumpida: " + e.getMessage());
        }       
    }
}
