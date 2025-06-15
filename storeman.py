import random
import string

storage = {}
    
def passwd_gen() -> str:
    total = string.ascii_letters + string.digits + string.punctuation
    count = 18
    result = ''.join(random.sample(total, count))
    return result

def adduser(username: str)  -> None:
    storage[username] = passwd_gen()
    
def remuser(username: str) -> None:
    storage.pop(username)
