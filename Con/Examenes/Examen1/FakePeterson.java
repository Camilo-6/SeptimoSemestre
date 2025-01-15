public class FakePeterson {
    private volatile boolean victim = false;
    //private boolean victim = false;
    private boolean flag = false;
    //private volatile boolean flag = false;

    public void lock() {
        while(flag == true) {};
        flag = true;
        while(victim == true) {};
        victim = true;
    }

    public void unlock() {
        flag = false;
        victim = false;
    }
    
}
