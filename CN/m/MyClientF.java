import java.io.*;
import java.net.*;

public class MyClientF {
    public static void main(String[] args) {
        try {
            Socket s = new Socket("localhost", 7777);
            DataOutputStream dos = new DataOutputStream(s.getOutputStream());

            // Specify the file you want to send
            File fileToSend = new File("file.txt");

            // Create a FileInputStream to read the file
            FileInputStream fis = new FileInputStream(fileToSend);

            byte[] buffer = new byte[1024];
            int bytesRead;

            // Read the file and send it to the server
            while ((bytesRead = fis.read(buffer)) != -1) {
                dos.write(buffer, 0, bytesRead);
            }

            fis.close();
            dos.close();
            s.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
