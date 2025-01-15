import java.util.ArrayList;
import java.util.List;

public class StampedValueH<T> extends StampedValue<T> {
  public List<T> values = new ArrayList<T>();
  /**
   * Constructor.
   */
  public StampedValueH(long stamp, T value) {
    super(stamp, value);
  }
  /**
   * Constructor.
   */
  public StampedValueH(T value) {
    super(value);
  }
  /**
   * Constructor.
   */
  public StampedValueH(long stamp, T value, List<T> v) {
    super(stamp, value);
    values = v;
  }
  public static StampedValue max(StampedValue x, StampedValue y) {
    if (x.stamp > y.stamp) {
      return x;
    } else if (x.owner > y.owner){
      return x;
    } else {
      return y;
    }
  }
}
