public class Player {
    private int position;

    public Player() {
        this.position = 1;
    }

    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
        if (this.position > 100) {
            this.position = 100;
        }
    }
}
