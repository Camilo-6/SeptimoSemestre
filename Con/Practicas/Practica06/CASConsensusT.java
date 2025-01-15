import java.util.concurrent.atomic.AtomicInteger;

public class CASConsensusT<T> implements ConsensusProtocol<T>{
    private T[] propose;
    private final int capacity;
    private final int FIRST=-1;
    private AtomicInteger r = new AtomicInteger(FIRST);

    public CASConsensusT(int c, T init){
        capacity = c;
        propose =  (T[]) new Object[capacity];
        for (int i = 0; i < capacity; i++) {
            propose[i] = init;
        }
    }

    public T decide(T value, int me){
        propose[me]=value;
        // Usamos ahora un getAndSet en vez de un compareAndSet
        if (FIRST == r.getAndSet(me)) {
        //if (r.compareAndSet(FIRST, me)) {
            //System.err.println("WIN " + me);
            return propose[me];
        } else {
            //System.err.println("LOSE " + me);
            return propose[r.get()];
        }
    }

}
