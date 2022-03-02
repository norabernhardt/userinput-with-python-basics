import os

def putFolder(username):
    os.mkdir(username)
    os.system("touch " + username + "/profile.txt")
    os.system("echo " + username + ">> "+ username + "/profile.txt")
    