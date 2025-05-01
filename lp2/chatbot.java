import java.util.*;

class chatbot {
    public static void main(String args[]) {
        System.out.println("------Welcome To Chatbot System-------");
        Scanner sc = new Scanner(System.in);

        boolean ans = true;
        while (ans) {
            System.out.print("You : ");
            String response = sc.nextLine();

            // Convert input to lower case to simplify comparison
            response = response.toLowerCase();

            if (response.equals("hii") || response.equals("hello")) {
                System.out.println("Bot : Hello Buddy! How can I help you?");
            } else if (response.equals("exit")) {
                ans = false;
                System.out.println("Bot : Goodbye!");
            } else {
                System.out.println("Bot : Sorry, I didn't understand that.");
            }
        }

        sc.close();
    }
}
