public class DoublePeterson {

    private Peterson lock1;
    private Peterson lock2;
    private Peterson lock3;

    public DoublePeterson() {
        lock1 = new Peterson();
        lock2 = new Peterson();
        lock3 = new Peterson();
    }

    public void lock() {
        Thread currentThread = Thread.currentThread();
        long id = currentThread.getId();
        int valor = (int) (id % 4);
        if (valor == 0 || valor == 1) {
            lock1.lock();
        }
        if (valor == 2 || valor == 3) {
            lock2.lock();
        }
        lock3.lock();
    }

    public void unlock() {
        Thread currentThread = Thread.currentThread();
        long id = currentThread.getId();
        int valor = (int) (id % 4);
        lock3.unlock();
        if (valor == 0 || valor == 1) {
            lock1.unlock();
        }
        if (valor == 2 || valor == 3) {
            lock2.unlock();
        }
    }
    
}
