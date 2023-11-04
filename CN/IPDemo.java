// DNS lookup
import java.net.*;
import java.util.Scanner;

public class IPDemo {
    public static void main(String[] args) {
        String host;
        Scanner input = new Scanner(System.in);
        
        System.out.println("1. Enter Host Name");
        System.out.println("2. Enter IP address");
        System.out.print("Choice: ");
        int choice = input.nextInt();

        if (choice == 1) {
            System.out.print("\nEnter host name: ");
            host = input.next();
            try {
                InetAddress address = InetAddress.getByName(host);
                System.out.println("IP address: " + address.getHostAddress());
                System.out.println("Host name: " + address.getHostName());
                System.out.println("Host name and IP address: " + address.toString());
            } catch (UnknownHostException ex) {
                System.out.println("Could not find " + host);
            }
        } else if (choice == 2) {
            System.out.print("\nEnter IP address: ");
            host = input.next();
            try {
                InetAddress address = InetAddress.getByName(host);
                System.out.println("Host name: " + address.getHostName());
                System.out.println("IP address: " + address.getHostAddress());
                System.out.println("Host name and IP address: " + address.toString());
            } catch (UnknownHostException ex) {
                System.out.println("Could not find " + host);
            }
        } else {
            System.out.println("Invalid choice. Please select 1 or 2.");
        }
    }
}
