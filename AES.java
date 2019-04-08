import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.Base64;
import java.io.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
public class AES {
 
    private static SecretKeySpec secretKey;
    private static byte[] key;
 
    public static void setKey(String myKey) 
    {
        MessageDigest sha = null;
        try {
            key = myKey.getBytes("UTF-8");
            sha = MessageDigest.getInstance("SHA-1");
            key = sha.digest(key);
            key = Arrays.copyOf(key, 16); 
            secretKey = new SecretKeySpec(key, "AES");
        } 
        catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        } 
        catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
    }
    public static String encrypt(String strToEncrypt, String secret) 
    {
        try
        {
            setKey(secret);
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
            cipher.init(Cipher.ENCRYPT_MODE, secretKey);
            return Base64.getEncoder().encodeToString(cipher.doFinal(strToEncrypt.getBytes("UTF-8")));
        } 
        catch (Exception e) 
        {
            System.out.println("Error while encrypting: " + e.toString());
        }
        return null;
    }
 
    public static String decrypt(String strToDecrypt, String secret) 
    {
        try
        {
            setKey(secret);
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5PADDING");
            cipher.init(Cipher.DECRYPT_MODE, secretKey);
            return new String(cipher.doFinal(Base64.getDecoder().decode(strToDecrypt)));
        } 
        catch (Exception e) 
        {
            System.out.println("Error while decrypting: " + e.toString());
        }
        return null;
    }
    public static void main(String[] args)throws IOException 
    {
        final String secretKey = "ssshhhhhhhhhhh!!!!";
        
        int status_code=0;
        FileReader fin1=new FileReader("statusCode.txt");
        BufferedReader bin1=new BufferedReader(fin1);
        if(bin1.readLine().equals("1"))
        {
            status_code=1;  
        }
        else if(bin1.readLine().equals("-1"))
        {
            status_code=-1;
        }
        bin1.close();
        fin1.close();
        if(status_code==1)
        {
            FileReader fin2=new FileReader("source.txt");
            BufferedReader bin2=new BufferedReader(fin2);
            String originalString=bin2.readLine();
            String encryptedString = AES.encrypt(originalString, secretKey) ;
            bin2.close();
            fin2.close();
            FileWriter fout2=new FileWriter("dest.txt");
            BufferedWriter bout2=new BufferedWriter(fout2);
            PrintWriter pout2=new PrintWriter(bout2);
            pout2.print(encryptedString);
            pout2.close();
            bout2.close();
            fout2.close();

        }
        else if(status_code==-1)
        {
            FileReader fin3=new FileReader("source.txt");
            BufferedReader bin3=new BufferedReader(fin3);
            String encryptedString=bin3.readLine();
            String decryptedString= AES.decrypt(encryptedString, secretKey) ;
            bin3.close();
            fin3.close();
            FileWriter fout3=new FileWriter("dest.txt");
            BufferedWriter bout3=new BufferedWriter(fout3);
            PrintWriter pout3=new PrintWriter(bout3);
            pout3.print(decryptedString);
            pout3.close();
            bout3.close();
            fout3.close();
        }
}
}