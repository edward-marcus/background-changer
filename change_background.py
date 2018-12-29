from os import getenv ,system
from shutil import copyfile
from glob import glob
from random import randint

images = []
for imagename in glob("C:/Users/[your windows username]/Pictures/Pictures/*.jpg"):     # a path to a folder with pictures, can be other    
    images.append(imagename)   # Create a list of pictures from that path on C drive

new_wallpaper = images[randint(0, len(images)-1)]  #store in a variable a random selection(picture) from that list
appdata = getenv("APPDATA")
dst = appdata + "\Microsoft\Windows\Themes"
copyfile(new_wallpaper, dst+"\TranscodedWallpaper")  # add that random selection to a specific file in Windows that displays the current background 

system("taskkill /f /IM explorer.exe")   
system("start C:/Windows/explorer.exe")  #kill and restart the windows explorer.exe process so that the change can take place.
                                        #If you don't do that you will be stuck to a black background,no GUI windows.  