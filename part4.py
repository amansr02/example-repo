import base64

def main():
    write_to_file()
    read_from_file()

def read_from_file():
    username = ""
    passwd = ""
    with open("login.txt",'r') as login_file:
        username = login_file.readline()
        passwd = login_file.readline()
    b = base64.b64decode((passwd))
    passwd = b.decode("utf-8")
    print(username + passwd)

def write_to_file():
    with open("login.txt","w") as login_file:
        login_file.write("amansr@umich.edu\n")
        password = "my_password"

        password = str.encode(password)
        temp = base64.b64encode(password)
        password = temp.decode("utf-8")

        login_file.write(password)

if __name__ == "__main__":
    main()
