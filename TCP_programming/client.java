import java.io.*;
import java.net.*;

public class client {
    public static void main(String[] args) {
        try {
            Socket clientSocket = new Socket("localhost", 6666);
            DataOutputStream dos = new DataOutputStream(clientSocket.getOutputStream());
            dos.writeUTF("Welcome..!! This is TCP protocol example");
            clientSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
