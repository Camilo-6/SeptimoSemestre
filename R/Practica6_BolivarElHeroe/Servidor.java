import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;

/**
 * 
 * Implementación del servidor para el juego de serpientes y escaleras
 * Este servidor maneja toda la lógica del juego 
 * También se encarga de controlar la IA para el jugador 2
 * 
 */

public class Servidor {
    private static final int PORT = 4500;
    private Board board;
    private Player player1; // Cliente
    private Player player2; // Servidor (IA)
    private Random random;

    public Servidor() {
        board = new Board(100);
        player1 = new Player();
        player2 = new Player();
        random = new Random();
    }

    public void start() {
        try {
            ServerSocket serverSocket = new ServerSocket(PORT);
            System.out.println("Servidor iniciado en el puerto " + PORT);
            System.out.println("Esperando conexión del cliente...");

            Socket clientSocket = serverSocket.accept();
            System.out.println("El cliente se conectó :D wuuu");

            DataInputStream input = new DataInputStream(clientSocket.getInputStream());
            DataOutputStream output = new DataOutputStream(clientSocket.getOutputStream());

            boolean gameOver = false;

            // Enviar mensaje de bienvenida e instrucciones
            output.writeUTF("Bienvenido al juego de Serpientes y Escaleras!\n" +
                            "Eres el Jugador 1. Presiona Enter para lanzar el dado.\n" +
                            board.printBoard(player1, player2));

            while (!gameOver) {
                // Esperar a que el cliente presione Enter para lanzar el dado
                String message = input.readUTF();
                System.out.println(message);

                // Jugador 1 lanza el dado
                int roll = random.nextInt(6) + 1;
                int previousPosition = player1.getPosition();
                board.move(player1, roll);
                int newPosition = player1.getPosition();

                String messageToClient = "Has lanzado un " + roll + ". Te mueves de " + previousPosition + " a " + newPosition + ".\n";

                // Comprobar si el jugador 1 ha ganado
                if (player1.getPosition() == board.getSize()) {
                    messageToClient += "Ganaste el juego! Felicidades!\n";
                    output.writeUTF(messageToClient + board.printBoard(player1, player2));
                    gameOver = true;
                    break;
                }

                // Jugador 2 (IA) lanza el dado
                int aiRoll = random.nextInt(6) + 1;
                int aiPreviousPosition = player2.getPosition();
                board.move(player2, aiRoll);
                int aiNewPosition = player2.getPosition();

                messageToClient += "El Jugador 2 (IA) ha lanzado un " + aiRoll + ". Se mueve de " + aiPreviousPosition + " a " + aiNewPosition + ".\n";

                // Comprobar si el jugador 2 ha ganado
                if (player2.getPosition() == board.getSize()) {
                    messageToClient += "El Jugador 2 (IA) ha ganado el juego. Mejor suerte la próxima vez.\n";
                    output.writeUTF(messageToClient + board.printBoard(player1, player2));
                    gameOver = true;
                    break;
                }

                // Enviar estado del juego al cliente
                messageToClient += board.printBoard(player1, player2);
                messageToClient += "\nPresiona Enter para tu próximo turno.";
                output.writeUTF(messageToClient);
            }

            // Cerrar conexiones
            input.close();
            output.close();
            clientSocket.close();
            serverSocket.close();
            System.out.println("Servidor cerrado.");

        } catch (IOException ex) {
        }
    }

    public static void main(String[] args) {
        Servidor servidor = new Servidor();
        servidor.start();
    }
}
