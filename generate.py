import threading
import util
import keyboard
import time

import ctypes

def base(word,do_jump): #base code for all of the types
    keyboard.press_and_release("/")
    time.sleep(0.05)
    keyboard.write(word,0.03)
    time.sleep(0.05)
    keyboard.press_and_release("enter")
    time.sleep(0.05)
    if do_jump: keyboard.press("space")
    time.sleep(0.05)
    keyboard.release("space")
    time.sleep(2.3)


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
    time.sleep(3)
    punctuation = config_instance.punctuation
    dir = config_instance.dir
    for num in range(config_instance.start, config_instance.end + 1):
        output = util.capitalize(config_instance, util.get_number(num)) + punctuation
        base(output,True)

def hj(config_instance):
    time.sleep(3)
    punctuation = config_instance.punctuation
    dir = config_instance.dir
    for num in range(config_instance.start, config_instance.end + 1):
        output = util.capitalize(config_instance, util.get_number(num)) # no punctuation
        for char in output.replace(' ', ''): # all except last character, no spaces
            base(char,True)
        base(output+punctuation,True)

        

def dj(config_instance):
    time.sleep(3)
    punctuation = config_instance.punctuation
    dir = config_instance.dir
    for num in range(config_instance.start, config_instance.end + 1):
        output = util.capitalize(config_instance, util.get_number(num))[::-1] # no punctuation, reversed
        for char in output.replace(' ', ''): # all except last character, no spaces
                base(char,True)

        base(output + punctuation,True)

def cj(config_instance):
    time.sleep(3)
    punctuation = config_instance.punctuation
    dir = config_instance.dir
    for num in range(config_instance.start, config_instance.end + 1):
        output = util.capitalize(config_instance, util.get_number(num)) + punctuation
        base("/e cheer",False)
        base(output,False)




        



        