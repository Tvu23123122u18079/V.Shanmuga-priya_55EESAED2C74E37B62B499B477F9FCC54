def checkLeap(Year):
# checking if the given year is Leap year
    if((Year % 400==0)or
      (Year % 100!=0)and
      (Year % 4==0)):
     print("Given year is a leap year");
  # Else if is not a leap year 
    else: 
     print("Given year is not a leap year")
# Taking an input year from uses  
year = int(input("Enter the number: "))
# printing result 
checkLeap(year)