import java.util.*;
import java.util.*;

class Task1GuessNumberGame{
    public static void main(String[] args) {
        Scanner ob = new Scanner(System.in);
        Random random = new Random();

        int minNo = 1;
        int maxNo = 100;
        int totalAttempts = 10;
        int score = 0;
		int round=0;
		
		System.out.println("--------Number Guessing Game!--------");

        do {
            round++;
			int targetno = random.nextInt(maxNo - minNo + 1) + minNo;
			int attempts = 0;
            System.out.println("Round no: "+round+", Guess the number between " + minNo + " and " + maxNo+ ", you have just 10 attempts");

            while (attempts < totalAttempts) {
                System.out.print("Enter your guess: ");
                int userGuess = ob.nextInt();
                attempts++;

                if (userGuess == targetno) {
                    System.out.println("Congratulations! You guessed the correct number in " + attempts + " attempts.");
                    score += totalAttempts - attempts + 1;
                    break;
                } else if (userGuess < targetno) {
                    System.out.println("Your entered number is too low!");
                } else {
                    System.out.println("Your entered number is too high!");
                }

                if (attempts == totalAttempts) {
                    System.out.println("Sorry, you attempted for 10 times. The correct number was: " + targetno);
                }
            }

            System.out.println("Do you want to play again? (yes/no): ");
        } while (ob.next().equalsIgnoreCase("yes"));

        System.out.println("Thanks for playing! Your total score is: " + score);
    }
}	