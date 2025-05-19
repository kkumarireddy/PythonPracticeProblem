
print("______WELCOME TO URL CHECKER______")
URL=input("Enter your URL:")
if URL.startswith("https://"):
    print("It is using HTTPS , Hence it secure")
elif URL.startswith("http://"):
    print("It is using HTTP , Hence not secure")
else:
    print("enter the valid url")
print("------------------------------------")
