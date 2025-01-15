import java.util.List;
import java.util.ArrayList;
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

public class ColaConcurrente {
    
    private Nodo head;
    private Nodo tail;
    private ExecutorService executor;
    private List<Future<String>> futures;

    public ExecutorService getExecutor() {
        return executor;
    }

    public ColaConcurrente() {
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

    private String enqS(String x) {
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
        return "done"; // revisar esto
    }

    private String deqS() {
        if (this.head.next == this.tail) {
            return "empty";
        }
        Nodo first = this.head.next;
        this.head.next = first.next;
        return first.item;
    }

    public void print() {
        System.out.println("Orden de operaciones");
        try {
            for (int i = 0; i < futures.size(); i++) {
                while (!futures.get(i).isDone());
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
        ColaConcurrente queue = new ColaConcurrente();
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

/* 
Inconsitencias
Orden de operaciones
Result: empty
Result: enqueued de 1 lista
Result: enqueued de 2 lista
Result: 1
Result: enqueued de 3 lista
Result: enqueued de 4 lista
Result: 2
Result: 2
Result: enqueued de 5 lista
Result: enqueued de 6 lista
Result: 3
Result: 4
Result: 5
Result: enqueued de 7 lista
Result: enqueued de 8 lista
Result: 6
Elementos de la cola
hnull
7
8
*/