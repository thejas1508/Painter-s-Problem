  Alice_residency_count=int(input("Enter Alice_residency_count:"))
  Bob_residency_count=int(input("Enter Bob_residency_count:"))
  Alice_Daily_Painting_Wages=int(input("Enter Alice_Daily_Painting_Wages:"))
  Bob_Daily_Painting_Wages=int(input("Enter Bob_Daily_Painting_Wages:"))
  if (Alice_residency_count>Bob_residency_count):
       Largest_colony=Alice_residency_count	
       Smallest_colony=Bob_residency_count
  else:
       Smallest_colony=Alice_residency_count
       Largest_colony=Bob_residency_count
  Remainder=Largest_colony%Smallest_colony
  If (Remainder==0):
    Largest_colony=Smallest_colony
    Smallest_colony=Largest_colony
  Remainder=Largest_colony%Smallest_colony
  Max_residency=Smallest_colony
  Largest_colony=Bob_residency_count
  Alice_Daily_Painting_Wages=Alice_Daily_Painting_Wages*Max_residency
  Alice_painting_Days=Alice_residency_count/Max_residency
  Alice_Total_Wages=Alice_Daily_Painting_Wages*Alice_painting_Days
  Print("The Total Wages of Alice:", Alice_Total_Wages)
  Bob_Daily_Painting_Wages=Bob_Daily_Painting_Wages*Max_residency
  Bob_Painting_Days=Bob_residency_count/Max_residency
  Bob_Total_Wages=Bob_Daily_Painting_Wages*Bob_Painting_Days
  Print("The Total Wages of Bob:", Bob_Total_Wages)
 


