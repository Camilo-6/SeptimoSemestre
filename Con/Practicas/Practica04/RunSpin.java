import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
public class RunSpin {
	static int counter = 0;
	public static int increment() {
		return counter++;
	}
	private static int task(Lock lock) {
		try {
			lock.lock();
			// sleep de 2000ms
			/* 
			try {
				Thread.sleep(2000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			*/
			increment();
		}finally {
			lock.unlock();		
		}
		return counter;
	}
	public static void main(String[] args) {
		List<Future<Integer>> futures = new ArrayList<Future<Integer>>();
		int numberThreads = 4;
		ExecutorService executor = Executors.newFixedThreadPool(numberThreads);
		CounterAtomic counter = new CounterAtomic(); // Descomentar para probar el contador atomico
		//Lock lock = new TASLock();
		//Lock lock = new TTASLock();
		//Lock lock = new BackoffLock();
		//Lock lock = new MCSLock();
		//Lock lock = new ALock(numberThreads);
		//Lock lock = new CLHLock();
		//Lock lock = new ReentrantLock();
		long startTime = System.nanoTime();//Start time
		for(int i = 0; i < 1000; i++) {
			//futures.add(executor.submit(() -> task(lock))); 
			futures.add(executor.submit(() -> counter.increment())); // Descomentar para probar el contador atomico
		}
		executor.shutdown();
		for (int i = 0; i < futures.size(); i++) {
            while(!futures.get(i).isDone()){}; // Comprobar que todas las tareas terminen
		}
		long endTime = System.nanoTime();//Finish time
        System.out.println("Program took " +
                (endTime - startTime)*0.000001 + "ms, Count result: " + counter) ; //En milisegundos
	}
}
