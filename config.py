import os
class Config:
    def prompt_console_configuration(self):
        print('BY: "firebanner641#1218" (Discord)')
        
        mode_menu_str = "1) JJ/GJ (Single message per number, forward order)\n2) HJ (Individual characters, end with full message, forward order)\n3) DJ (Individual characters, end with full message, backwards order)\n4) CJ (Single message per number, enter to start, /e cheer instead of jump, forward order)\nMode : "
        self.mode = int(input(mode_menu_str))

        cap_menu_str = "1) ONE\n2) Two\n3) three\nCap mode : "
        self.cap_mode = int(input(cap_menu_str))

        self.punctuation = input("Punctuation : ")
        self.start = int(input("Start at : "))
        self.end = int(input("End at : "))
        self.dir = os.getcwd()

        return self
    
    def default_configuration(self):
        self.mode = 1
        self.cap_mode = 1
        self.punctuation = ""
        self.start = 1
        self.end = 1
        self.dir = os.getcwd()

        return self


        

