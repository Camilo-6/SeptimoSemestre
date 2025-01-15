import java.io.*;
import java.net.Socket;
import java.util.Scanner;

/**
 * 
 * Implementación del cliente para el juego de Serpientes y Escaleras.
 * El cliente se conecta al servidor y de esta forma puede empezar a jugar
 * presionando enter, lo que simula lanzar dados para avanzar en el tablero
 * 
 */

public class Cliente {
    private static final String SERVER_ADDRESS = "localhost";
    private static final int SERVER_PORT = 4500;

    public void start() {
        try {
            Socket socket = new Socket(SERVER_ADDRESS, SERVER_PORT);
            System.out.println("Conectado al servidor.");

            DataInputStream input = new DataInputStream(socket.getInputStream());
            DataOutputStream output = new DataOutputStream(socket.getOutputStream());
            Scanner scanner = new Scanner(System.in);

            boolean gameOver = false;

            // Leemos el mensaje de bienvenida e instrucciones
            String messageFromServer = input.readUTF();
            System.out.println(messageFromServer);

            while (!gameOver) {
                // Esperamos a que el usuario presione Enter
                scanner.nextLine();
                output.writeUTF("El jugador ha lanzado el dado.");
                // Leeemos el estado del juego después del turno
                messageFromServer = input.readUTF();
                System.out.println(messageFromServer);

                if (messageFromServer.contains("Felicidades!") || messageFromServer.contains("ha ganado el juego")) {
                    gameOver = true;
                }
            }

            // Cerramos las conexiones
            scanner.close();
            input.close();
            output.close();
            socket.close();
            System.out.println("Conexión cerrada.");

        } catch (IOException ex) {
            System.err.println(ex.getMessage());
        }
    }

    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.start();
    }
}
