gmail_id = input("Enter Your Gmail_ID :")
while '@' not in gmail_id:
    print("Invalid GMAIL_ID (MUST CONTAIN '@'). Please Try Again")
    gmail_id=input("Enter Your Gmail_ID :")
password = input("Enter Your PASSWORD:")
while len(password)!=10:
      print("Invalid PASSWORD (MUST BE 10 CHARACTERS LONG). Please Try Again")
      password = input("Enter Your PASSWORD:")
print("ACCOUNT CREATED SUCCESSFULLY")

i=1
while i<3:
    login_gmail_id = input("Enter Your GMAIL ID:")
    login_password = input("Enter Your PASSWORD :")


    if login_gmail_id == gmail_id and login_password == password:
        print("You Are In!")
    else:
        print(f"Incorrect. You Have {3-i} Attempts Left")
        if i==3:
             print("Maximum Attempts Reached. Account Locked.")