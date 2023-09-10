import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = getenv('SESSION', 'Media_search')
API_ID = int(getenv('API_ID', '23830477'))
API_HASH = getenv('API_HASH', '19f8365d98fb11c9cd6c1eaa8b1fa4b8')
BOT_TOKEN = getenv('BOT_TOKEN', '6384094059:AAEpXeEB5KdvmMjfQn8VlTlKtCsTsyPOq4g')

# Bot settings
CACHE_TIME = int(getenv('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(getenv('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6408116706').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001561813692').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001629572693')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Khrish:98982khrishisveryop07@cluster1.hh7bbcz.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster1")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Searcher Data')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001607412183'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MHA_Discussion')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>Join - [ @MOVIES_HUB_ALPHA_Official ] </b> <code>{file_caption}</code>\n<b>━━━━━━━━━━•••••━━━━━━━━━\n🏘 Backup - @MOVIES_HUB_ALPHA_official\n❤️ SHARE AND SUPPORT US</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌‌‌‌IMDb Data by: @MOVIES_HUB_ALPHA_OFFICIAL \n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 \n\n♥️ we are nothing without you ♥️ \n\n💛 Please Share Us 💛\n\n⚠️Click on the button 👇 below to get your query privately\n\n🎊 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [『 MOVIES HUB ALPHA 』](t.me/MOVIES_HUB_ALPHA_Official)")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

#LazyRenamer Configs
FLOOD = int(environ.get("FLOOD", "10"))
LAZY_MODE = bool(environ.get("LAZY_MODE", "6408116706"))
#Add user id of the user in this field those who you want to be Authentic user for file renaming features
lazy_renamers = [int(lazrenamers) if id_pattern.search(lazrenamers) else lazrenamers for lazrenamers in environ.get('LAZY_RENAMERS', '').split()]
LAZY_RENAMERS = (lazy_renamers + ADMINS) if lazy_renamers else []
REQ_CHANNEL = int(environ.get('REQ_CHANNEL', '0'))

#ai
OPENAI_API = environ.get("OPENAI_API","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")
AI = is_enabled((environ.get("AI","True")), False)
LAZY_AI_LOGS = int(environ.get("LAZY_AI_LOGS","-1001888075413")) #GIVE YOUR NEW LOG CHANNEL ID TO STORE MESSAGES THAT THEY SEARCH IN BOT PM.... [ i have added this to keep an eye on the users message, to avoid misuse of LazyPrincess ]
# Requested Content template variables ---
ADMIN_USRNM = environ.get('ADMIN_USRNM','SpidyRockss') # WITHOUT @
MAIN_CHANNEL_USRNM = environ.get('MAIN_CHANNEL_USRNM','MOVIES_HUB_ALPHA_OFFICIAL') # WITHOUT @
DEV_CHANNEL_USRNM = environ.get('DEV_CHANNEL_USRNM','MOVIES_HUB_ALPHA_OFFICIAL') # WITHOUT @
LAZY_YT_HANDLE = environ.get('LAZY_YT_HANDLE','0')  # WITHOUT @ [  add only handle - don't add full url  ] 
MOVIE_GROUP_USERNAME = environ.get('MOVIE_GROUP_USERNAME', "MOVIES_HUB_ALPHA_SEARCH_GROUP") #[ without @ ]

# Url Shortner
URL_MODE = is_enabled((environ.get("URL_MODE","False")), False)
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', '') #Always use website url from api section 
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '')
LZURL_PRIME_USERS = [int(lazyurlers) if id_pattern.search(lazyurlers) else lazyurlers for lazyurlers in environ.get('LZURL_PRIME_USERS', '5965340120').split()]
lazy_groups = environ.get('LAZY_GROUPS','')
LAZY_GROUPS = [int(lazy_groups) for lazy_groups in lazy_groups.split()] if lazy_groups else None # ADD GROUP ID IN THIS VARIABLE
my_users = [int(my_users) if id_pattern.search(my_users) else my_users for my_users in environ.get('MY_USERS', '').split()]
MY_USERS = (my_users) if my_users else []



# Online Stream and Download
PORT = int(environ.get('PORT', 4004))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = False
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "http://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)
REPO_OWNER = "LazyDeveloperr"

# Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

# Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/MOVIES_HUB_ALPHA_OFFICIAL"

# Custom Caption Under Button #
CAPTION_BUTTON = "Get Updates"
CAPTION_BUTTON_URL = "https://t.me/MOVIES_HUB_ALPHA_OFFICIAL"
PICS = [
    "https://telegra.ph/file/451a9169cb4bca927080f.jpg",
    "https://telegra.ph/file/9fc8c8de06567f8ae2c2b.jpg",
    "https://telegra.ph/file/c529f35aacc3d2abc8506.jpg",
    "https://telegra.ph/file/510f122c639b622ff58d5.jpg",
    "https://telegra.ph/file/dd4c7a696ad93f61b8237.jpg",
    "https://telegra.ph/file/3dd35884409726bb73b36.jpg",
    "https://telegra.ph/file/8eb078168134871566d30.jpg",
    "https://telegra.ph/file/8d1d4b4a1ed2de4830273.jpg",
    "https://telegra.ph/file/1d28bcea826cc2a2c9799.jpg",
    "https://telegra.ph/file/89bac63888fedc062ccf9.jpg",
    "https://telegra.ph/file/e130508fd1c5a7afbce1d.jpg",
    "https://telegra.ph/file/78c87763cb140992f5ad6.jpg",
    "https://telegra.ph/file/dc92d039fa693acf5d979.jpg",
    "https://telegra.ph/file/e5cf0a4c1ce9e2c309bfe.jpg",
    "https://telegra.ph/file/50392bef6764d8b38b0bf.jpg",
    "https://telegra.ph/file/9206d428a468856bf1e0d.jpg",
    "https://telegra.ph/file/9d6efcb7813d9643067a7.jpg",
    "https://telegra.ph/file/f1a3d6b5a7f7f4ca36ee2.jpg",
    "https://telegra.ph/file/f07947ec8ee7c8560e19e.jpg",
    "https://telegra.ph/file/6660dc2786d6d4788d187.jpg",
    "https://telegra.ph/file/061fd49c54a12bb67e8f9.jpg",
    "https://telegra.ph/file/c1cbb94f2494d1aa528a3.jpg",
    "https://telegra.ph/file/0861d0d95232c6ff6adcd.jpg",
    "https://telegra.ph/file/1f6420b86cc6a4fc877c0.jpg",
    "https://telegra.ph/file/a78a305f1267b00f22ed4.jpg",
    "https://telegra.ph/file/73da3b58b9ce339670474.jpg",
    "https://telegra.ph/file/7a49738026138a2c062d9.jpg",
    "https://telegra.ph/file/fbe0918db37e0f48f30ba.jpg",
    "https://telegra.ph/file/6b07361706ff748816601.jpg",
    "https://telegra.ph/file/a8ec9b2c6db0f9bd6b3a8.jpg",
    "https://telegra.ph/file/7288b5da0fb688414deef.jpg",
    "https://telegra.ph/file/53a816b088124d3c66bc5.jpg",
    "https://telegra.ph/file/6ac56221904580d5d3441.jpg",
    "https://telegra.ph/file/f83b2d99b76e0ac35887d.jpg",
    "https://telegra.ph/file/390e16dcc796cfeb83577.jpg",
    "https://telegra.ph/file/4afbcbaba868f54e7a978.jpg",
    "https://telegra.ph/file/0b6fb808a8e24dae9ec1c.jpg",
    "https://telegra.ph/file/9e2d0a0af022d5ce1f29e.jpg",
    "https://telegra.ph/file/3411143bae8a8172af7e5.jpg",
    "https://telegra.ph/file/82a86dfb865384f3a7605.jpg",
    "https://telegra.ph/file/1649a05bfac2fe427c899.jpg",
    "https://telegra.ph/file/641f50719aa46c861b03b.jpg",
    "https://telegra.ph/file/195692b21de0a08c98e67.jpg",
    "https://telegra.ph/file/8893b4eafc1482fa1a9cc.jpg",
    "https://telegra.ph/file/dc3a6a9d4515bcba92738.jpg",
    "https://telegra.ph/file/3b67fbb27ec76733300d2.jpg",
    "https://telegra.ph/file/68b61bb9247d97e790a18.jpg",
    "https://telegra.ph/file/671337718cd6890dc6fc0.jpg",
    "https://telegra.ph/file/e3727d2204d61c5dde803.jpg",
    "https://telegra.ph/file/1f181a8a26415255079d7.jpg",
    "https://telegra.ph/file/7d74a6ffc20bb32c5965f.jpg",
    "https://telegra.ph/file/df934bd669d3fdce27c47.jpg",
    "https://telegra.ph/file/123c52599b60144a59a9c.jpg",
    "https://telegra.ph/file/7812a61812f1d21e87899.jpg",
    "https://telegra.ph/file/59a4a4e80675ef245772f.jpg",
    "https://telegra.ph/file/8f060e468a55b19d8b7f6.jpg",
    "https://telegra.ph/file/4b84bc8651f1712112755.jpg",
    "https://telegra.ph/file/65e0fe1f2d1bb2a3064ce.jpg",
    "https://telegra.ph/file/40a291550d830b600a052.jpg",
    "https://telegra.ph/file/f62474ef87f87c5f9c098.jpg",
    "https://telegra.ph/file/72f2a02a64218c0d04537.jpg",
    "https://telegra.ph/file/4133a958b124a519c6020.jpg",
    "https://telegra.ph/file/9abf5c4c8d35472536e0a.jpg",
    "https://telegra.ph/file/a846f83e78b5d84b6215f.jpg",
    "https://telegra.ph/file/6fd2b95a54bed69de5add.jpg",
    "https://telegra.ph/file/437f905fe9a8988d07f41.jpg",
    "https://telegra.ph/file/e1ebebf52ce8b2a749707.jpg",
    "https://telegra.ph/file/b877ee2028ebe45a41493.jpg",
    "https://telegra.ph/file/c7af99a1e5809772cafb2.jpg",
    "https://telegra.ph/file/54c502e96ce8505ae876e.jpg",
    "https://telegra.ph/file/d4174f0cdfb15f76f14b5.jpg",
    "https://telegra.ph/file/9859e28b47d7d7734b8f5.jpg",
    "https://telegra.ph/file/a396fb2e8771c5c4360a9.jpg",
    "https://telegra.ph/file/ff63898dcb9f74cdac179.jpg",
    "https://telegra.ph/file/84f57c7b814c33474231c.jpg",
    "https://telegra.ph/file/08a464bed5c135c212fb8.jpg",
    "https://telegra.ph/file/7282ef0777321f6e72a58.jpg",
    "https://telegra.ph/file/470058f042fba90717404.jpg",
    "https://telegra.ph/file/f1e1e9d31bc2a4d1e6798.jpg",
    "https://telegra.ph/file/15719217d3ad505f1346b.jpg",
    "https://telegra.ph/file/9c5aba59a85f1de92bd59.jpg",
    "https://telegra.ph/file/dde366c5b307679b25b1f.jpg",
    "https://telegra.ph/file/25d6e249f017b5c2a25e6.jpg",
    "https://telegra.ph/file/f042b7d173a57ec750082.jpg",
    "https://telegra.ph/file/7e7c20474b2f8601dce8f.jpg",
    "https://telegra.ph/file/fbb6e28a3b311dbb7df3b.jpg",
    "https://telegra.ph/file/79862f5ec9525f367f698.jpg",
    "https://telegra.ph/file/ca1d306c80e0ac0d524e5.jpg",
    "https://telegra.ph/file/04d7c9df026c3c2b75cfe.jpg",
    "https://telegra.ph/file/5da622b0a0b356cea1a4c.jpg"
]
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
# Credit @LazyDeveloper.
# Please Don't remove credit.
# Born to make history @LazyDeveloper !
# Thank you LazyDeveloper for helping us in this Journey
# 🥰  Thank you for giving me credit @LazyDeveloperr  🥰
# for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 
# rip paid developers 🤣 - >> No need to buy paid source code while @LazyDeveloperr is here 😍😍
