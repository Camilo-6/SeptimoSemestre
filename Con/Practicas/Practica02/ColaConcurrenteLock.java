import java.util.List;
import java.util.ArrayList;
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

public class ColaConcurrenteLock {
    
    private Nodo head;
    private Nodo tail;
    private ExecutorService executor;
    private List<Future<String>> futures;

    public ExecutorService getExecutor() {
        return executor;
    }

    public ColaConcurrenteLock() {
        this.head = new Nodo("hnull");
        this.tail = new Nodo("tnull");
        this.head.next = this.tail;
        futures = new ArrayList<Future<String>>();
        this.executor = Executors.newFixedThreadPool(4);
    }

    public Boolean enq(String x) {
        futures.add(executor.submit(() -> enqS(x)));
        return true;
    }

    private synchronized String enqS(String x) {
        Nodo newnode = new Nodo(x);
        if (this.head.next == this.tail) {
            newnode.next = this.tail;
            this.head.next = newnode;
        } else {
            Nodo last = this.tail.next;
            newnode.next = tail;
            last.next = newnode;
        }
        tail.next = newnode;
        return "enqueued de " + x + " lista";
    }

    public String deq() {
        futures.add(executor.submit(() -> deqS()));
        return "done";
    }

    private synchronized String deqS() {
        if (this.head.next == this.tail) {
            return "empty";
        }
        Nodo first = this.head.next;
        this.head.next = first.next;
        String result = first.item;
        return result;
    }

    public void print() {
        System.out.println("Orden de operaciones");
        try {
            for (int i = 0; i < futures.size(); i++) {
                while (!futures.get(i).isDone()) {
                    System.out.print("aun no termina");
                }
                String result = futures.get(i).get();
                System.out.printf("Result: " + result + "\n");
            }
        } catch (InterruptedException e) {
            System.out.println(e);
        } catch (ExecutionException e) {
            System.out.println(e);
        }
        System.out.println("Elementos de la cola");
        Nodo pred = this.head;
        Nodo curr = pred.next;
        System.out.println(pred.item);
        while (curr.item != "tnull") {
            pred = curr;
            curr = curr.next;
            System.out.println(pred.item);
        }
    }

    public static void main(String[] args) {
        ColaConcurrenteLock queue = new ColaConcurrenteLock();
        queue.deq();
        queue.enq("1");
        queue.enq("2");
        queue.deq();
        queue.enq("3");
        queue.enq("4");
        queue.deq();
        queue.deq();
        queue.enq("5");
        queue.enq("6");
        queue.deq();
        queue.deq();
        queue.deq();
        queue.enq("7");
        queue.enq("8");
        queue.deq();
        queue.print();
        queue.getExecutor().shutdown();
    }

}