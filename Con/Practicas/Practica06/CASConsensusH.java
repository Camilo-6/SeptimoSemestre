import java.util.concurrent.atomic.AtomicInteger;

public class CASConsensusH<T> implements ConsensusProtocol<T>{
    private T[] propose;
    private final int capacity;
    private final int FIRST=-1;
    private AtomicInteger r = new AtomicInteger(FIRST);

    public CASConsensusH(int c, T init){
        capacity = c;
        propose =  (T[]) new Object[capacity];
        for (int i = 0; i < capacity; i++) {
            propose[i] = init;
        }
    }

    public T decide(T value, int me){
        propose[me]=value;
        if (r.compareAndSet(FIRST, me)) {
            //System.err.println("WIN " + me);
            return propose[me];
        } else {
            //System.err.println("LOSE " + me);
            return propose[r.get()];
        }
    }

    public T dedice2(T value, int me){
        return propose[r.get()];
    }

}
