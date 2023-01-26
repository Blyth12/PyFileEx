import os
import shutil
import winreg
import time
def main():
    ui = input("----- (R)un , (D)elete , (M)ove , (V)iew, (W)inreg ----- ")
    if ui.lower() == "d":
        ff = input("(F)older or (Fi)le ")
        if ff.lower() == "f":
            dir = input ("State folder directory: ")
            #dir = r"C:\Users\ccs18blyth-larrubiae\AppData\Local\Google\Chrome\User Data\Profile 1\Extensions\jaoebcikabjppaclpgbodmmnfjihdngk"
            shutil.rmtree(dir, ignore_errors=True)
            print("Deleted '%s' directory successfully" % dir)
            main()
        elif ff.lower() == "fi":
            fdir = input ("State file directory: ")
            os.remove(fdir)
            main()
            
    elif ui.lower() == "r":
        fdir = input("State file directory: ")
        os.startfile(fdir)
        main()

    elif ui.lower() == "m":
        ff = input ("(F)older or (Fi)le ")
        if ff.lower() == "f":
            forg = input("Enter origin folder path: ")
            fnd = input("Enter new folder path: ")
            main()
        elif ff.lower() == "fi":
            ford = input("Enter origin file path: ")
            fnd = input("Enter new folder path: ")
            main()
        
    elif ui.lower() == "v":
        print("view")
        main()
        
    elif ui.lower() == "w":
        print("Initializing WinReg...")
        time.sleep(3)
        cmd = input("Enter command:")
        #winreg.SetValue(Software\Policies\Google\Chrome\DeveloperToolsAvailability, 1)

    else:
        print("Inavlid")
        main()
    
main()

