import java.util.*;

public class Board {
    private int size;
    // Casillas especiales con su símbolo (Ei o Si) escaleras/serpientes
    private Map<Integer, String> specialTiles; 
     // Posiciones de cada Ei y Si
    private Map<String, List<Integer>> tilePositions;

    // Códigos de color ANSI para cambiar el color del texto en la terminal
    private static final String resetear = "\u001B[0m";
    private static final String color_escalera = "\u001B[32m"; 
    private static final String color_serpiente = "\u001B[31m"; 

    public Board(int size) {
        this.size = size;
        specialTiles = new HashMap<>();
        tilePositions = new HashMap<>();

        // Inicializamos las serpientes y escaleras (9 de cada una)
        addSnakeOrLadder("S1", 17, 7);
        addSnakeOrLadder("S2", 54, 34);
        addSnakeOrLadder("S3", 62, 19);
        addSnakeOrLadder("S4", 64, 60);
        addSnakeOrLadder("S5", 87, 24);
        addSnakeOrLadder("S6", 93, 73);
        addSnakeOrLadder("S7", 95, 75);
        addSnakeOrLadder("S8", 98, 79);
        addSnakeOrLadder("S9", 49, 11);

        addSnakeOrLadder("E1", 2, 38);
        addSnakeOrLadder("E2", 4, 14);
        addSnakeOrLadder("E3", 9, 31);
        addSnakeOrLadder("E4", 21, 42);
        addSnakeOrLadder("E5", 28, 84);
        addSnakeOrLadder("E6", 36, 44);
        addSnakeOrLadder("E7", 51, 67);
        addSnakeOrLadder("E8", 71, 91);
        addSnakeOrLadder("E9", 80, 99);
    }

    private void addSnakeOrLadder(String symbol, int pos1, int pos2) {
        specialTiles.put(pos1, symbol);
        specialTiles.put(pos2, symbol);

        tilePositions.computeIfAbsent(symbol, k -> new ArrayList<>());
        tilePositions.get(symbol).add(pos1);
        tilePositions.get(symbol).add(pos2);
    }

    public int move(Player player, int roll) {
        int currentPosition = player.getPosition();
        int newPosition = currentPosition + roll;

        if (newPosition > size) {
            newPosition = currentPosition; // Se queda en el mismo lugar
        }

        // Verificar si cayó en una casilla especial
        if (specialTiles.containsKey(newPosition)) {
            String symbol = specialTiles.get(newPosition);
            int targetPosition = getCorrespondingPosition(symbol, newPosition);

            if (targetPosition != newPosition) {
                player.setPosition(targetPosition);
            } else {
                player.setPosition(newPosition);
            }
        } else {
            player.setPosition(newPosition);
        }

        return player.getPosition();
    }

    private int getCorrespondingPosition(String symbol, int currentPos) {
        List<Integer> positions = tilePositions.get(symbol);

        if (symbol.startsWith("E")) {
            // Como estamos en escalera, buscamos la posición más alta
            int maxPos = currentPos;
            for (int pos : positions) {
                if (pos > maxPos) {
                    maxPos = pos;
                }
            }
            if (maxPos != currentPos) {
                return maxPos;
            }
        } else if (symbol.startsWith("S")) {
            // Como estamos en serpiente, buscamos la posición más baja
            int minPos = currentPos;
            for (int pos : positions) {
                if (pos < minPos) {
                    minPos = pos;
                }
            }
            if (minPos != currentPos) {
                return minPos;
            }
        }
        // Si no hay movimiento, regresar la posición actual
        return currentPos;
    }

    public int getSize() {
        return size;
    }

    private String colorize(String symbol) {
        if (symbol.startsWith("E")) {
            return color_escalera + symbol + resetear;
        } else if (symbol.startsWith("S")) {
            return color_serpiente + symbol + resetear;
        } else {
            return symbol;
        }
    }

    public String printBoard(Player player1, Player player2) {
        StringBuilder sb = new StringBuilder();
        sb.append("\nTablero:\n");

        // Iteramos de arriba hacia abajo
        for (int i = size; i > 0; i -= 10) {
            // Determinamos el índice de inicio para la fila actual
            int start = Math.max(1, i - 9);
            // Determina en que orden se debe de imprimir la fila actual
            boolean isZigzagRow = ((size - i) / 10) % 2 != 0;

            if (isZigzagRow) {
                // Derecha a izquierda
                for (int j = start; j <= i; j++) {
                    sb.append(getCellRepresentation(j, player1, player2));
                }
            } else {
                // izquierda a derecha
                for (int j = i; j >= start; j--) {
                    sb.append(getCellRepresentation(j, player1, player2));
                }
            }

            sb.append("\n");
        }

        // Leyenda con colores
        sb.append("\nLeyenda:\n");
        sb.append("1: Jugador 1\n");
        sb.append("2: Jugador 2\n");
        sb.append("X: Los dos jugadores están en la misma casilla\n");
        sb.append(colorize("Si") + ": Serpiente número i\n");
        sb.append(colorize("Ei") + ": Escalera número i\n");
        sb.append(colorize("Si-N") + " / " + colorize("Ei-N") + ": Jugador N en casilla especial\n");

        return sb.toString();
    }

    // Método auxiliar para obtener la representación de la celda
    private String getCellRepresentation(int position, Player player1, Player player2) {
        String specialSymbol = specialTiles.getOrDefault(position, "");
        String cell;

        // Si ambos jugadores están en la misma posición
        if (player1.getPosition() == position && player2.getPosition() == position) {
            cell = !specialSymbol.equals("") ? "[" + colorize(specialSymbol) + "-X]" : "[X]";
            // Si solo el Jugador 1 está en la posición.
        } else if (player1.getPosition() == position) {
            cell = !specialSymbol.equals("") ? "[" + colorize(specialSymbol) + "-1]" : "[1]";
            // Si solo el Jugador 2 están en la posición
        } else if (player2.getPosition() == position) {
            cell = !specialSymbol.equals("") ? "[" + colorize(specialSymbol) + "-2]" : "[2]";
        } else {
            // Casilla vacía o con un símbolo especial (escalaera o serpiente)
            cell = !specialSymbol.equals("") ? "[" + colorize(specialSymbol) + "]" : "[ ]";
        }

        return cell;
    }

}
