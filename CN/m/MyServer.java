import java.io.*;  
import java.net.*;  
public class MyServer {  
public static void main(String[] args){  
try{  
ServerSocket ss=new ServerSocket(7777);  
Socket s=ss.accept();//establishes connection   
DataInputStream dis=new DataInputStream(s.getInputStream());  
String  str=(String)dis.readUTF();  
System.out.println(str);  
ss.close();  
}catch(Exception e){System.out.println(e);}  

try{      
    Socket s=new Socket("localhost",7777);  
    DataOutputStream dout=new DataOutputStream(s.getOutputStream());  
          
      InetAddress ip = InetAddress.getByName("192.168.1.100");  
        dout.writeUTF("Hello");  
        dout.flush();  
    dout.close();  
    s.close();  
    }catch(Exception e){System.out.println(e);} 
}  
} 
