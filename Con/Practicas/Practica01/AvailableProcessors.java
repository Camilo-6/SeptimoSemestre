public class AvailableProcessors {
    public static void main(String[] args) {
        int processors = Runtime.getRuntime().availableProcessors();
        System.out.println("Available processors (cores): " + processors);

        
    }
}

