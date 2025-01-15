import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;

public class Scheduler {
    // Para solo dar acceso a lo mas a 3 personas
    static Semaphore semaphore = new Semaphore(3, true);  

    public static void main(String[] args){
        // Corresponde a las 6 personas enviando sus tareas
        ExecutorService executorTarea = Executors.newFixedThreadPool(6);

        for(int i = 0; i < 6; i++) {
            executorTarea.execute(new Tarea(i, semaphore));
        }

        
        executorTarea.shutdown();
    }
}
