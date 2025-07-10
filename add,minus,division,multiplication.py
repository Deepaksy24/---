num1=int(input("enter number :"))
num2=int(input("enter number :"))
print("select your operation 1. + 2. - 3. * 4./")
user_input=(input("enter operation"))
if user_input=="+":
  print(num1+num2)
elif user_input=="-":
 print(num1-num2)
elif user_input=="*":
 print(num1*num2)
elif user_input=="/":
 print(num1/num2)