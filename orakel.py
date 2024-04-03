from email_client import send_mail
import random
import string
import db

def evalute(name):
    desc = db.get_user_name(name)
    if desc:
        return name + " " + desc
    else:
        return not_found(name)

def add_user(id, name, desc):
    db.add_user(id, name, desc)

def check_request(id):
    if db.get_request(id):
        return True
    return False


def find_id(id):
    return db.get_request(id)
    
def add_request(name, description):
    id = str(random.randint(0, 10000000000))
    print(id, name, description)
    db.add_request(id, name, description)
    return id

def request_orakel(name, description, url="127.0.0.1:5000"):
    print(f"{name} mit Begründung: {description}")
    id = add_request(name, description)
    msg = f"{name} will auch cool sein. Begründung:\n{description}\n{url}/accept/{id}"
    send_mail("edgar.bennemann@gmail.com", f"{name} bittet um Aufnahme in das Orakel", msg)

def not_found(name):
    alphabet = string.ascii_lowercase + "öäüß. "

    sum = 0
    for n in name:
        sum += alphabet.index(n.lower())

    sentences = [f"{name} ist leider nicht cool.", 
                 f"{name} ist bei uns nicht als cool gelistet.", 
                 f"{name} gehört leider nicht zu den coolen...",
                 f"Als cool ist {name} leider nicht gelistet.",
                 f"Nope, {name} ist leider nicht cool.",
                 f"Folgende Person ist leider nicht cool: {name}.",
                 f"Wir müssen dich leider enttäuschen, aber {name} ist leider nicht cool.",
                 f"{name} steht nicht auf der Liste der Coolen."]
    return sentences[sum % len(sentences)]
