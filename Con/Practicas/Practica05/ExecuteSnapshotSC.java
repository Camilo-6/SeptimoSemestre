import java.util.Random;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ExecuteSnapshotSC {

	public static void main(String[] args) {
		int capacity = 4;
		String init = null;
		ConcurrentLinkedQueue<Integer> queue = new ConcurrentLinkedQueue<>();// Implementacion linealizable de una cola no acotada
		SimpleSnapshotHC<String> snapshotI = new SimpleSnapshotHC<String>(capacity,init);
		SimpleSnapshotHC<String> snapshotR = new SimpleSnapshotHC<String>(capacity,init);
			ExecutorService executor = Executors.newFixedThreadPool(4);
			
			Random rand = new Random(); //Para crear num randoms
			for(int i = 0; i < 10; i++) {
				int numRand = rand.nextInt(2);//Si es 0 se ejecuta un enq(), si es 1 un deq()
				final int ntask=i;//Los items integers que se agregan a la cola
				executor.execute(new RunnableSC(ntask, queue,numRand,snapshotI,snapshotR)); 
			}
			executor.shutdown();
			
			while(!executor.isTerminated()) {};
			
			// Imprimir los snaps guardados en el update()
			
			/*System.out.println("Snapshot Final in Invs");
			StampedSnapH<String>[] copy = (StampedSnapH<String>[]) new StampedSnapH[capacity];
			copyI = snapshotI.collect();
			for (int j = 0; j < capacity; j++) {
				System.out.println("\n Thread Owner: " + copy[j].owner + " Last Value: " + copy[j].value +  
						" Last Stamp: " + copy[j].stamp + " Number of Snaps: " + copy[j].snap.size());
				
				  for (int i = 0; i < copy[j].snap.size(); i++) { 
					  System.out.println("The " + i + " snap has: " ); 
					  for (int k = 0; k < capacity; k++) {
						  System.out.println("Thread " + k + " has value: " + copy[j].getSnap(k,i)); }
				  }
				 
			}*/
			
			StampedValueH<String>[] copy = (StampedValueH<String>[]) new StampedValueH[capacity];
			copy = snapshotR.collect();
			System.out.println("Ejecutanto el SimpleSnapshotHC");
			System.out.println("Snapshot Final --- Values");
			for (int j = 0; j < capacity; j++) {
				System.out.println("\n Thread Owner: " + copy[j].owner +  
						" Last Stamp: " + copy[j].stamp + " Number of Snaps: ");// + copy[j].snap.size());
				System.out.println("The values are: "); 
				for (int i = 0; i < copy[j].values.size(); i++) { 
					  
					  System.out.println(copy[j].values.get(i)); }
				  
			}
		}
}
