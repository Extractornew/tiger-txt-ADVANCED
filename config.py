import os

API_ID = API_ID = 29611474

API_HASH = os.environ.get("43b3fdc649a8266de1b8ba3facc4aa75")

BOT_TOKEN = os.environ.get("7159828976:AAFlwpuCRlnmIx1wiV65hMwyEbH-8i7EvwU")
p
PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7037323404)

LOG = -1002004650552

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7037323404").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


