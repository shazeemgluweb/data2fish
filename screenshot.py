import pyautogui    #importeert pyautogui                                                                    
import tkinter as tk    #importeert tkinter en maakt het gebruikbaar als 'tk'
from tkinter.filedialog import * #import filedialog vanuit tkinter

root = tk.Tk() #de root aanmaken voor de canvas met tk

canvas1 = tk.Canvas(root, width = 300, height = 300) #het creeeren van de canvas
canvas1.pack() #ontpakt de canvas in zijn geheel

def takeScreenshot():   #definiteert een functie om een screenshot te maken
    myScreenshot = pyautogui.screenshot() #een object maken om de screenshot op te slaan
    save_path = asksaveasfilename() #opvragen aan de user waar hij/zij de screenshot wilt opslaan
    myScreenshot.save(save_path+"_screenshot.png") #het opslaan van de screenshot in de savepath en er automatisch '_screenshot.png' achter te zetten.


myButton = tk.Button(text="Take Screenshot", command = takeScreenshot,font=10) #een knop creeeren met tkinter waar we de screenshot mee kunnen nemen met de takescreenshot function.
canvas1.create_window(150,150,window=myButton) #de knop in het midden van de canvas zetten.

root.mainloop() #mainloop gebruiken zodat we de canvas altijd kunnen zien