import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

# Bot information
SESSION = environ.get('SESSION', 'Webavbot')
API_ID = int(environ.get('API_ID', '27258953'))
API_HASH = environ.get('API_HASH', '0add43fc460daca0a86077989cfc414f')
BOT_TOKEN = environ.get('BOT_TOKEN', "")
BOT_USERNAME = environ.get("BOT_USERNAME", 'mlfiletolinkbot') # without @ 

# Admins, Channels & Users
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '-1002005906539')) # admin your channel in stream 
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-1002005906539')) # admin your channel in users log 
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '949657126').split()] # 3567788, 678899, 5889467
OWNER_USERNAME = environ.get("OWNER_USERNAME", 'mladminbot') # without @ 

# pics information
PICS = environ.get('PICS', 'https://graph.org/file/a319f6b9ce3b993c6e22f.jpg')

# channel link information
CHANNEL = environ.get('CHANNEL', 'https://t.me/MovieEntertainment4u')
SUPPORT = environ.get('SUPPORT', 'http://t.me/movie_loverzz')

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

# ban information
BANNED_CHANNELS = [int(banned_channels) if id_pattern.search(banned_channels) else banned_channels for banned_channels in environ.get('BANNED_CHANNELS', '').split()]   
BAN_CHNL = [int(ban_chal) if id_pattern.search(ban_chal) else ban_chal for ban_chal in environ.get('BAN_CHNL', '').split()]
BAN_ALERT = environ.get('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.ᴄᴏɴᴛᴀᴄᴛ [ᴀᴠ ᴄʜᴀᴛ ᴏᴡɴᴇʀ](https://telegram.me/mladminbot) ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>')

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://primebaby11220:TuGa0I5ZsiC8mp5A@cluster0.df4rivj.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "primebaby11220")

# fsub  information
AUTH_PICS = environ.get('AUTH_PICS', 'https://graph.org/file/a319f6b9ce3b993c6e22f.jpg')              
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002230197603"))
FSUB = environ.get("FSUB", True)

# port information
PORT = int(getenv('PORT', '8080'))
NO_PORT = bool(getenv('NO_PORT', False))

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

# time information
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))

# Online Stream and Download
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
WORKERS = int(getenv('WORKERS', '6'))
MULTI_CLIENT = False
name = str(environ.get('name', 'Movie_loverzz'))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
else:
    ON_HEROKU = False
FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', 'https://a-loki-bot2-b9b930b68654.herokuapp.com/') else APP_NAME+'.herokuapp.com'
HAS_SSL=bool(getenv('HAS_SSL',True))
if HAS_SSL:
    URL = "https://a-loki-bot2-b9b930b68654.herokuapp.com/".format(FQDN)
else:
    URL = "https://a-loki-bot2-b9b930b68654.herokuapp.com/".format(FQDN)
      
#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP
