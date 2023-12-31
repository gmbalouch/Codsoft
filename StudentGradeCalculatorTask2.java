
import java.util.*;

public class StudentGradeCalculatorTask2{
	public static void main(String args[]){
		Scanner ob=new Scanner(System.in);
		System.out.println("-------Student Grade Calculator-------");
		System.out.println("Enter number of Subjects: ");
		int noOfSub=ob.nextInt();

		int totalMarks=0;
		for(int i=1; i<=noOfSub; i++){
			System.out.println("Enter marks of Subject :"+i);
			int marks=ob.nextInt();
			totalMarks+=marks;	
		}

		int argPer=totalMarks/noOfSub;
		System.out.println(argPer);

		if(argPer>=90 && argPer<=100){
			System.out.println("Grade: A1");
		}else if(argPer>=80 && argPer<=89){
			System.out.println("Grade: A");	
		}else if(argPer>=70 && argPer<=79){
			System.out.println("Grade: B");
		}else if(argPer>=60 && argPer<=69){
			System.out.println("Grade: C");	
		}else if(argPer>=50 && argPer<=59){
			System.out.println("Grade: D");
		}else if(argPer<=49){
			System.out.println("Fail");	
		}

	}


}