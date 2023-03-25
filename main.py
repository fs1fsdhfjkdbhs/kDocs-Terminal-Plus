import pyperclip
import os
import time
import sys
import playsound
import settings

#info

password = settings.password
username = settings.username

#script

def script():
    print(time.ctime())
    cmd = input("∂ ")
    if cmd == "print":
        string = input("")
        print(string)
        script()
    elif cmd == "new_file":
        name = input("name: ")
        type = input("format: ")
        os.system("cd {}".format(settings.file_path))
        open(name + type, "w").close()
        os.system("cd {}".format(os.getcwd()))
        script()
    elif cmd == "-cmd":
        command_ = input("command: ")
        os.system(command_)
        script()
    elif cmd == "del_file":
        path_ = input("path: ")
        try:
            os.remove(path_)
            script()
        except:
            print("ERROR: invalid file!")
            script()
    elif cmd == "name_file":
        path = input("path: ")
        newName = input("new-name: ")
        try:
            os.rename(path, newName)
            script()
        except:
            print("ERROR: invalid file!")
            script()
    elif cmd == "audio-play":
        file = input("path: ")
        playsound.playsound(file)
        script()
    elif cmd == "-help":
        print("kDocs-Terminal Commands")
        print("-------------------------")
        print("1. print\nMake the computer say something that you want it to say.")
        print("2. new_file\nCreate a new file.")
        print("3. del_file\nDelete a file.")
        print("4. name_file\nRename a file.")
        print("5. -cmd\nEnable CMD mode. One CMD command at a time!")
        print("6. audio-play\nPlay an audio file. Supported formats: mp3, wav")
        print("7. file\nManage your files.")
        print("8. settings --username\nYour username settings.")
        print("9. settings --password\nYour password settings.")
        print("10. exit\nExit kDocs-Terminal.")
        print("11. settings --filePath\nYour settings for where files get created. (Default: where script is)")
        print("")
        script()
    elif cmd == "file":
        f = input("file-path: ")
        print("")
        print("File Manager")
        print("-------------------")
        print("Write content: -w")
        print("Overwrite content: -ow")
        print("Show content: -c")
        _action = input("")
        if _action == "-w":
            content = input("content: ")
            with open(f, "a+") as __file:
                __file.write("\n" + content)
            script()
        elif _action == "-ow":
            content_ = input("content: ")
            with open(f, "w") as _file_:
                _file_.write("")
                _file_.write(content_)
            script()
        elif _action == "-c":
            fi = open(f)
            print(fi.read())
            fi.close()
            script()
        else:
            print("ERROR: invalid action!")
            script()
    elif cmd == "settings --username":
        print("Current username: {}".format(username))
        print("---------------------------")
        print("Copy username: -c")
        print("Change username: -ch")
        a = input("Enter action: ")
        if a == "-c":
            pyperclip.copy(username)
            print("Username copied to clipboard.")
            script()
        elif a == "-ch":
            new_username = input("new-username: ")
            with open("user/username.txt", "w") as f_:
                f_.write(new_username)
            print("Username changed to {}.".format(new_username))
            script()
        else:
            print("ERROR: invalid action!")
            script()
    elif cmd == "settings --password":
        print("Current password: {}".format(password))
        print("---------------------------")
        print("Copy password: -c")
        print("Change password: -ch")
        a_ = input("Enter action: ")
        if a_ == "-c":
            pyperclip.copy(password)
            print("Password copied to clipboard.")
            script()
        elif a_ == "-ch":
            new_password = input("new-password: ")
            with open("user/password.txt", "w") as _f_:
                _f_.write(new_password)
            print("Password changed to {}.".format(new_password))
            script()
        else:
            print("ERROR: invalid action!")
            script()
    elif cmd == "exit":
        yn = input("Are you sure you want to exit kDocs-Terminal? (y/n)\n")
        if yn == "y":
            exit()
        elif yn == "n":
            print("")
            script()
        else:
            print("")
            script()
    elif cmd == "":
        print("")
        script()
    else:
        print("ERROR: invalid command!")
        script()


print("Downloading unavailable modules..")
time.sleep(1)
os.system("pip3 install playsound")
os.system("pip3 install pyperclip")

passinput = input("Enter your computer password to continue: ")

if passinput == password:
    print("Checking input..")
    time.sleep(2)
    print("Login successfull! Welcome to kDocs-Terminal, {}.".format(username))
    time.sleep(2)
    script()
else:
    print("Checking input..")
    time.sleep(2)
    print("Login unsuccessfull. Terminating window..")
    time.sleep(2)
    sys.exit()
