import java.io.*;
import java.net.*;

public class MyServerF {
    public static void main(String[] args) {
        try {
            ServerSocket ss = new ServerSocket(7777);
            Socket s = ss.accept();

            DataInputStream dis = new DataInputStream(s.getInputStream());

            // Specify the location where you want to save the received file
            File receivedFile = new File("file.txt");

            FileOutputStream fos = new FileOutputStream(receivedFile);
            byte[] buffer = new byte[1024];
            int bytesRead;

            // Read data from the client and write it to the received file
            while ((bytesRead = dis.read(buffer)) != -1) {
                fos.write(buffer, 0, bytesRead);
            }

            fos.close();
            ss.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
