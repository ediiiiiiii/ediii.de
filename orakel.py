from email_client import send_mail
import random
import string

filename_orakel = "orakel.geheim"
filename_request = "request.orakel"

def evalute(name):
    name = " ".join([n for n in name.split() if len(n) > 0]) # remove spaces

    file = open(filename_orakel, "r").read().split("\n") # open file and split at linebreaks
    names = [n[2:].lower() for n in file[::2] if n[0:2] == "# "] # list of all names
    descriptions = file[1::2] # list of all descriptions
    try:
        return name + " " + descriptions[names.index(name.lower())]
    except ValueError:
        return not_found(name)

def save(name, description):
    file = open(filename_orakel, "a")
    file.write(f"\n# {name}\n")
    file.write(description)
    file.close()

""" def delete_index(index):
    with open(filename_request, "r") as f:
        lines = f.readlines()
    with open(filename_request, "w") as f:
        for l in (len(lines)):
            if ()
 """
def check_id(id):
    file = open(filename_request).read().split("\n")
    ids = [f.split(" ")[1] for f in file[::2] if f[0] == "#"]
    names = [" ".join(f.split(" ")[2:]) for f in file[::2] if f[0] == "#"]
    descriptions = file[1::2]

    try:
        index = ids.index(str(id))
        return True
    except ValueError:
        return False

def find_id(id):
    file = open(filename_request).read().split("\n")
    ids = [f.split(" ")[1] for f in file[::2] if f[0] == "#"]
    print(ids)
    names = [" ".join(f.split(" ")[2:]) for f in file[::2] if f[0] == "#"]
    print(names)
    descriptions = file[1::2]

    try:
        index = ids.index(str(id))
    except ValueError:
        return 0, 0

    return names[index], descriptions[index]
    
def add_request(name, description):
    file = open(filename_request, "a")
    id = str(random.randint(0, 10000000000000000000000))
    file.write(f"\n# {id} {name}\n")
    file.write(description)
    file.close()
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