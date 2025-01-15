import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class SimpleSnapshotHC<T> implements Snapshot<T> {
  private StampedValueH<T>[] a_table;  // array of atomic MRSW registers
  public SimpleSnapshotHC(int capacity, T init) {
    a_table = (StampedValueH<T>[]) new StampedValueH[capacity];
    for (int i = 0; i < capacity; i++) {
      a_table[i] = new StampedValueH<T>(init);
    }
  }
  public void update(T value) {
    int me = ThreadID.get();
    StampedValueH<T> oldValue = a_table[me];
    oldValue.values.add(value);
    StampedValueH<T> newValue =
        new StampedValueH<T>((oldValue.stamp)+1, value, oldValue.values);
    a_table[me] = newValue;
  }
  public StampedValueH<T>[] collect() {
    StampedValueH<T>[] copy = (StampedValueH<T>[]) new StampedValueH[a_table.length];
    for (int j = 0; j < a_table.length; j++)
      copy[j] = a_table[j];
    return copy;
  }
  public T[] scan() {
    StampedValueH<T>[] oldCopy;
    oldCopy = collect();
    T[] result = (T[]) new Object[a_table.length];
      for (int j = 0; j < a_table.length; j++)
        result[j] = (T) oldCopy[j].values;
      return result;
  }
}



