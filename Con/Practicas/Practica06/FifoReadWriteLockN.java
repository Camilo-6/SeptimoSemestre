import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * First-in First-out readers/writers lock.
 */
public class FifoReadWriteLockN implements ReadWriteLock {
  int readAcquires; // read acquires since start
  int readReleases; // read releses since start
  int writeAcquires; // write acquires since start
  int writeReleases; // write releases since start
  //boolean writer;   // writer present?
  Lock metaLock;    // short-term synchronization
  Condition condition;
  Lock readLock;    // readers apply here
  Lock writeLock;   // writers apply here
  
  public FifoReadWriteLockN() {
    readAcquires = readReleases = 0;
    //writer    = false;
    // Agregamos las variables para llevar el control de los escritores
    writeAcquires = writeReleases = 0;
    metaLock  = new ReentrantLock();
    condition = metaLock.newCondition();
    readLock  = new ReadLock();
    writeLock = new WriteLock();
  }
  
  public Lock readLock() {
    return readLock;
  }
  
  public Lock writeLock() {
    return writeLock;
  }
  private class ReadLock implements Lock {
    public void lock() {
      metaLock.lock();
      try {
        
        //System.out.println("Lock ReadAcquires: " + readAcquires + " ReadReleases: " + readReleases);
        
        //while (writer) {
        // Ahora se verifica si hay escritores en la SC y si hay, se espera
        while (writeAcquires != writeReleases) {
          try {
            condition.await();
          } catch (InterruptedException ex) {
            // do something application-specific
          }
          
        }
        //System.out.println("Writer: " + writer);
        readAcquires++;
      } finally {
        metaLock.unlock();
      }
    }
    public void unlock() {
      metaLock.lock();
      try {
        readReleases++;
        //System.out.println("Unlock ReadAcquires: " + readAcquires + " ReadReleases: " + readReleases);

        if (readAcquires == readReleases)
          condition.signalAll();
      } finally {
        metaLock.unlock();
      }
    }
    public void lockInterruptibly() throws InterruptedException {
      throw new UnsupportedOperationException();
    }
    
    public boolean tryLock() {
      throw new UnsupportedOperationException();
    }
    
    public boolean tryLock(long time, TimeUnit unit) throws InterruptedException {
      throw new UnsupportedOperationException();
    }
    
    public Condition newCondition() {
      throw new UnsupportedOperationException();
    }
  }
  private class WriteLock implements Lock {
    public void lock() {
      metaLock.lock();
      try {
        // Ahora ya no se verifica si hay un escritor en la SC
        /*
        while (writer)
          try {
            condition.await();
          } catch (InterruptedException e) {}
        writer = true;
        */

        while (readAcquires != readReleases)
          try {
            condition.await();
          } catch (InterruptedException e) {}
        // Ahora aumentamos el contador de escritores que entraron a la SC
        writeAcquires++;
        //System.out.println("Writer: " + writer);

      } finally {
        metaLock.unlock();
      }
    }
    public void unlock() {
      
      //writer = false;
      
      metaLock.lock();
      try {
        // Ahora vamos a tener que aumentar el contador de escritores que salieron de la SC
        writeReleases++;
        // Si ya no hay escritores en la SC, se despiertan a los hilos que estan esperando
        if (writeAcquires == writeReleases)
          condition.signalAll();
      } finally {
        metaLock.unlock();
      }
      //System.out.println("Writer: " + writer);
    }
    public void lockInterruptibly() throws InterruptedException {
      throw new UnsupportedOperationException();
    }
    
    public boolean tryLock() {
      throw new UnsupportedOperationException();
    }
    
    public boolean tryLock(long time, TimeUnit unit) throws InterruptedException {
      throw new UnsupportedOperationException();
    }
    
    public Condition newCondition() {
      throw new UnsupportedOperationException();
    }
  }
}

/*
 * Una posible manera de obtener justicia en este candado podria ser
 * que se lleve un registro de la diferencia entre el numero de lecturas y escrituras
 * y que se de prioridad a los que tengan una menor cantidad.
 * Otra idea seria usar una lista de espera donde los hilos se formen y tal vez usar
 * una para que los primeros hilos en llegar sean los primeros en salir, aunque para esta
 * estrategia existen algunas complicaciones ya que los lectores pueden entrar a la SC
 * mientras otro lector esta dentro, pero los escritores no pueden entrar si hay un lector
 * dentro, lo cual complica la justicia, por lo cual una idea es que ninguno pueda entrar
 * mientras alguien este en su SC.
 */