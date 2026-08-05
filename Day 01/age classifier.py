name = input("What is your name?")
age = int(input("How old are you?"))

if age < 0:
    print(f" Hello {name}, the age you entered is invalid, please stop trolling and exit the site.")

elif age <= 12:
    print(f" Hello {name}, access denied! you are {age} years old, which is too young to access this content as CHILDREN not allowed.")
elif age <= 17:
    print(f" Hello {name}. limited access to content due to you being {age} years old, TEENS cant get full access coz they are not mature enough.")
elif age <= 64:
    print(f" Hello {name}, Since you are an ADULT you have full access to the content please move forward and enter your country.")
    country = input ("which country are you from?")
    print(f"  welcome to the site, you can access all data related to {country}.")

    
else:
    print(f" Hello {name}, Since you are a SENIOR, you have full access to our site and we wish you a simple surfing to the content, Bonne journee!")
    country = input ("which country are you from?")
    print(f" welcome to the site, you can access all data related to {country}.")

