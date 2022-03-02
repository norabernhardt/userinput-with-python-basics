import os

def putFolder(username,profile):
    os.mkdir("username")
    os.system("touch" + username + "/profile.txt")
    os.system("echo" + input + username >> "/profile.txt")