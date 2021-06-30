import threading
import util
import keyboard
import time
import subprocess
import ctypes

class GenerateThread(threading.Thread):
    
    def get_id(self):
  
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
    
def jj(config_instance):
    punctuation = config_instance.punctuation
    dir = config_instance.dir
    for num in range(config_instance.start, config_instance.end + 1):
        output = util.capitalize(config_instance, util.get_number(num)) + punctuation
        keyboard.wait("space")
        subprocess.call(["cscript.exe", str(dir) + "\\openchat.vbs", "//NOLOGO"])
        time.sleep(0.1)
        keyboard.write(output)
        keyboard.wait('enter')

def hj(config_instance):
    punctuation = config_instance.punctuation
    dir = config_instance.dir
    for num in range(config_instance.start, config_instance.end + 1):
        output = util.capitalize(config_instance, util.get_number(num)) # no punctuation
        for char in output.replace(' ', ''): # all except last character, no spaces
            keyboard.wait("space")
            subprocess.call(["cscript.exe", str(dir) + "\\openchat.vbs", "//NOLOGO"])
            time.sleep(0.1)
            keyboard.write(char)
            keyboard.wait('enter')
        keyboard.wait("space")
        subprocess.call(["cscript.exe", str(dir) + "\\openchat.vbs", "//NOLOGO"])
        time.sleep(0.1)
        keyboard.write(output + punctuation)
        keyboard.wait('enter')

def dj(config_instance):
    punctuation = config_instance.punctuation
    dir = config_instance.dir
    for num in range(config_instance.start, config_instance.end + 1):
        output = util.capitalize(config_instance, util.get_number(num))[::-1] # no punctuation, reversed
        for char in output.replace(' ', ''): # all except last character, no spaces
                keyboard.wait("space")
                subprocess.call(["cscript.exe", str(dir) + "\\openchat.vbs", "//NOLOGO"])
                time.sleep(0.1)
                keyboard.write(char)
                keyboard.wait('enter')

        keyboard.wait("space")
        subprocess.call(["cscript.exe", str(dir) + "\\openchat.vbs", "//NOLOGO"])
        time.sleep(0.1)
        keyboard.write(output + punctuation)
        keyboard.wait('enter')

def cj(config_instance):
    punctuation = config_instance.punctuation
    dir = config_instance.dir
    keyboard.wait('enter')
    for num in range(config_instance.start, config_instance.end + 1):
        output = util.capitalize(config_instance, util.get_number(num)) + punctuation
        subprocess.call(["cscript.exe", str(dir) + "\\openchat.vbs", "//NOLOGO"])
        time.sleep(0.1)
        keyboard.write("/e cheer")
        keyboard.wait('enter')
        time.sleep(0.1)
        subprocess.call(["cscript.exe", str(dir) + "\\openchat.vbs", "//NOLOGO"])
        time.sleep(0.1)
        keyboard.write(output)
        keyboard.wait('enter')




        



        