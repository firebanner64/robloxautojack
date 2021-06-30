import num2words

def get_number(num: int):
    return num2words.num2words(num).replace("-", " ")



def capitalize(config_instance, txt):
    if config_instance.cap_mode == 3:
        return txt.lower()
    elif config_instance.cap_mode == 2:
        return txt[0].upper() + txt[1:].lower()
    elif config_instance.cap_mode == 1:
        return txt.upper()