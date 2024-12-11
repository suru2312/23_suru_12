# Email ID
a = input("Enter your Email-id : ")
flag = True
# Email should contain @ and should not contain " ".
if "@" in a and " " not in a: 
    # Spliting Email on '@'
    z = a.split("@")                                      # suraj23   @    gmail    .     com
    # Splitting company name and domain name on '.'.
    y = z[1].split(".")
    u_name = z[0]
    c_name = y[0]
    d_name = y[1]
    # Checking if the username is in lower case
    if not u_name.islower():
        flag = False
    # Checking if the username, company name, domain name have atlest 1 character.
    if len(u_name) < 1 and len(c_name) < 1 and len(d_name) < 1:
        flag = False
    # Domain name must be between (including) 2 and 4. 
    if len(d_name) > 4 and len(d_name) < 2:
        flag = False
    # Checking if the first character is a digit or '.'.
    if u_name[0].isdigit() or u_name[0] == ".":
        flag = False
    # username must only contain one '.'. 
    if u_name.count(".") > 1:
        flag = False
    # u_name = suraj.sharma.great
    for i in u_name.split("."):
        # i = suraj , i = sharma
        if not i.isalnum():
            flag = False
            break
    if not c_name.isalnum():
        flag = False
    if not d_name.isalpha():
        flag = False
else:
    flag = False
if flag:
    print(f"Your E-Mail ID '{a}' is Valid.")
else:
    print(f"Your E-Mail ID '{a}' is Invalid.","\nTry in 'xyz.abc@email.dom' this format.")



# --------------------------sir answer------------------------------
# email = input("enter your email : ")
# k =  False
# if (len(email)>=6) and (email.count(" ")==0) and (email.count("@")==1) :
#     if email.count(".")>0 and email.count(".")<=2 and email[0].isalpha() and email.islower()  :
#         if "." in email.split("@")[1] :
#             username,company,domain = email.split("@")[0],email.split("@")[1].split(".")[0] ,email.split("@")[1].split(".")[1]
#             if len(username)>0 and len(company)>0 and len(domain)>1 and len(domain)<5 :
#                 if domain.isalpha() and company.isalpha() :
#                     for i in username :
#                         if i.isalnum() or i == ".":
#                             pass
#                         else :
#                             k=True
#                 else :
#                     k=True
#             else :
#                 k=True
#         else :
#             k=True
#     else :
#         k=True
# else :
#     k=True

# if k == False :
#     print("Right email")
# else :
#     print("wrong email")