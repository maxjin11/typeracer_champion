# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 20:42:57 2021

@author: maxpe
"""

from tkinter import * 
import pyautogui as p, time as t
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command

def main():	
    root = Tk()
    root.title("Automated Typeracer Bot")
    global first_start
    first_start = 0
    global start 
    start = False
    global status
    status = "none"
    global play_again_yes
    play_again_yes = False

    def window_check():
        global first_start
        global start
        global status

        if start == True:
            if first_start == 0:
                global driver
                driver = webdriver.Chrome("C:\\Users\\maxpe\\Downloads\\chromedriver_win32\\chromedriver.exe")
                driver.get("https://play.typeracer.com/")

                if driver.session_id == None:
                	first_start = 0    

    
    def real_race():
        global start
        start = True
        global status
        status = "real"
        window_check()
        racing()
        
    def practice_race():
        global start
        start = True
        global status
        status = "practice"
        window_check()
        racing()

    def play_again():
        global first_start
        global start
        start = True
        global play_again_yes
        play_again_yes = True

        if first_start == 1:
	        window_check()
	        racing()
        else:
	        print("Please enter a race in order to play again!")


    def kill_program():
        global driver
        driver.quit()
        root.destroy()
        
    title = Label(root, text="The Automated Typeracer Bot")
    description = Label(root, text='"If you can\'t beat them, my bot can."') 
    credit = Label(root, text="Project made by Max Jin, December 2020.")

    # real races against typeracer terms of service, to use: remove state=DISABLED
    button_real = Button(root, text="Enter a real race", command=real_race, padx=40, pady=40, borderwidth=5, state=DISABLED)
    button_practice = Button(root, text="Enter the practice track", command=practice_race, padx=40, pady=40, borderwidth=5)
    button_play_again = Button(root, text="Play the same race again", command=play_again, padx=150, pady=40, borderwidth=5)
    button_quit = Button(root, text="Exit the race track", command=kill_program, padx=158, pady=40, borderwidth=5)
    
    title.grid(row=0, column=0, columnspan=2)
    description.grid(row=1, column=0, columnspan=2)
    credit.grid(row=2, column=0, columnspan=2)
    button_real.grid(row=3, column=0)
    button_practice.grid(row=3, column=1)
    button_play_again.grid(row=4, column=0, columnspan=2)
    button_quit.grid(row=5, column=0, columnspan=2)


    def racing():
        global first_start
        global start
        global status
        global play_again_yes

        if start == True:
            t.sleep(4)
            # driver.switch_to.window(driver.current_window_handle)
            # focus = driver.find_element(By.ID, "tr_textHeader")
            # focus.click()
            if first_start == 1:
            	p.hotkey("alt", "tab")

            t.sleep(1)

            if play_again_yes == True:
                p.hotkey("ctrl", "alt", "k")
                if status == "real":
                	t.sleep(17) # extra time to account for pop-up messages that could appear
                elif status == "practice":
                	t.sleep(7) 
                else:
                	print("Please enter a race.")
                play_again_yes = False
            
            else:
	            if status == "real":
	                p.hotkey("ctrl", "alt", "i")
	                t.sleep(15)
	            
	            elif status == "practice":
	                p.hotkey("ctrl", "alt", "o")
	                t.sleep(5)
	            else:
	                print("Please enter a race.")        
        # race starts
            # scrape text
            # typingtext = driver.find_element_by_class_name("inputPanel").text ***old code for previous version of selenium/chromium
            typingtext = driver.find_element(By.CLASS_NAME, "inputPanel").text
            realtext = typingtext.split("\n")
        
            print(realtext[0])
        
            f = open("typeracertext.txt", "w")
            f.write(realtext[0])
            f.close()
            

        # program types
            f = open("typeracertext.txt", "r")
            for word in f:
                p.typewrite(word, interval=0.018)
                p.press("space")
            f.close()
            start = False
            first_start = 1
            play_again_yes = False


        else:
            print("You are currently on the interface.")

    root.mainloop()

if __name__ == "__main__":
    main()