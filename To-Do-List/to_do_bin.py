import time
import textwrap
import glob
import pickle

def note_lesen():
    global note_liste
    if not glob.glob("notes.bin"):
        note_liste = []
        return
    d = open("notes.bin", "rb")
    note_liste = pickle.load(d)
    d.close()

def note_anzeigen():
    if not note_liste:
        print("Nothing here yet, sorry:(")
        return
    print("Nr. Name            Date\n      Text")
    for i in range(len(note_liste)):
        print(f"{i+1:2d}. {note_liste[i][0]:20}"
              f" {note_liste[i][1]:15}\n {note_liste[i][2]}\n")

def note_schreiben():
    d = open("notes.bin", "wb")
    pickle.dump(note_liste, d)
    d.close()

def deleteNote():
    print("Which Note do you want to delete? (Enter the Number)")
    nr = int(input())
    print("You`ve chosen this Note to be deleted")
    note_lesen()
    print(f"{note_liste[nr - 1]}\n"
          "Are you sure you want to delete? (1: Yes, 2: No")
    delete = int(input())
    if delete == 1:
        note_liste.pop(nr - 1)
        print("OK, your Note has been deleted")
        note_schreiben()
        note_anzeigen()
    elif delete == 2:
        menu()

def editNote():
    print("Which Note do you want to edit? (Enter the Number)")
    global nrE
    nrE = int(input())
    print("You`ve chosen this Note:", end="")
    note_lesen()
    print(f"{note_liste[nrE - 1]}\n"
          "Do you really want to edit this Note? (1: Yes, 2: No)")
    confirm = int(input())
    if confirm == 1:
        what = str(input("What would you like to edit? (Name or text?)")).lower()
        if what == "name":
            print(f"That`s the Name: \n{note_liste[nrE - 1][0]}")
            print("What would you like to replace it with? \n"
                  "Please enter the new Name (max. 20 Letters)")
            neuN = str(input())
            note_lesen()
            note_liste[nrE - 1][0] = neuN
            note_liste[nrE - 1][1] = time.strftime("%d.%m.%Y %H:%M")
            note_schreiben()
            print("Your Title has been replaced")
        if what == "text":
            print(f"That`s the text: \n{note_liste[nrE - 1][2]}")
            print("What would you like to replace it with? \n"
                  "Enter your new Text (max. 100 Letters)")
            neuT = str(input())
            note_lesen()
            note_liste[nrE - 1][2] = neuT
            note_liste[nrE - 1][1] = time.strftime("%d.%m.%Y %H:%M")
            note_schreiben()
            print("The Text has been replaced")





#Programm:
note_lesen()

def menu():
    while True:
        print("Please choose "
                         "(0: Break, 1: History, 2: New Note")
        menu = int(input())
        if menu == 2:
            try:
                nameRegular = str(input("Enter your Name"))

                datum = time.strftime("%d.%m.%Y %H:%M", time.localtime())
                text = str(input("Please enter your Note (max. 100 Characters)"))
            except:
                print("wrong input!")
                continue
            save = int(input("Do you want to save your Note?? (1: Yes, 2: No"))
            if save == 1:
                note_liste.append([nameRegular, datum, text])
                note_schreiben()
                print("OK, your Note has been saved")
            else:
                break
        elif menu == 1:
            note_anzeigen()
            if note_liste:

                remove = int(input("\nDo you want to delete a Note?? (1: Yes, 2: No)\n"))
                if remove == 1:
                    deleteNote()
                if note_liste:
                    edit = int(input("Do you want to edit a Note?? (1: Yes, 2: No)\n"))

                    if edit == 1:
                        editNote()

        elif menu == 0:
            break
        else:
            print("wrong input")
            continue

#Programm:

menu()