class script(object):
    START_TXT = """Hello {},
Myself <a href=https://t.me/MHA_SearchBot>MHA Searcher</a>,

ɪ ᴀᴍ ᴘᴏᴡᴇʀ ғᴜʟʟ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ʙᴏᴛ
ɪ ᴀᴍ ᴘᴍ sʜᴏʀᴛɴᴇʀ-ʟɪɴᴋ ʙᴏᴛ

ᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/MOVIES_HUB_ALPHA_OFFICIAL">MHA Team</a> 😏</b>"""
    LZTHMB_TEXT = """Hello {},
Glad to see you here. It seems that you really love <a href=https://t.me/SpidyRockss >Spidy's</a> work.
<b>Thumbnail extracting</b> feature will be available soon, please join <a href=https://t.me/MOVIES_HUB_ALPHA_OFFICIAL>Dev Channel</a> and stay tuned for next <a href=https://t.me/MOVIES_HUB_ALPHA_OFFICIAL>update</a>.\n\n  🐞 Report Bug here: <a href=https://t.me/MHA_Discussion>MHA Discusson/Support</a>"""
    LZLINK_TEXT = """Hay {},
Glad to see you here. It seems that you really love <a href=https://t.me/SpidyRockss >Spidy's</a> work.
<b>File to LiNK converting</b> feature will be available soon, please join <a href=https://t.me/MOVIES_HUB_ALPHA_OFFICIAL>Dev Channel</a> and stay tuned for next <a href=https://t.me/MOVIES_HUB_ALPHA_OFFICIAL>update</a>.\n\n  🐞 Report Bug here: <a href=https://t.me/MHA_Discussion>MHA Discusson/Support</a>"""
    DNT_TEXT = """Hey sweetie {},
Thanks for thinking about us.\nIt seems that you really love <a href=https://t.me/SpidyRockss >Spidy's</a> work.\n\n<b>For your kind information, we do not ask or force anyone for any kind of payment</b>. But if you really want to donate us then you can send money to us from below links...\n\n💵 Reach Donation Page : <a href=http://t.me/Donate_To_MHA_Team>Click here...</a>\n\n❤️ Thank you so much..
    """
    REQ_AUTH_TEXT = """Hello {},
\nSorry sweetie.. You must have to be the Authentic User to complete this operation...\n\n👮‍♀ REPORT ISSUE HERE: <a href=https://t.me/MHA_Discussion>MHA Discusson/Support</a>\n\n
    """
    ALRDY_UPLDD_TEXT = """✅ Content is already uploaded.\n\nName:{}\nPlease make sure about your spelling before submiting request..."""
    HELP_TXT = """𝙷𝙴𝚈 {}
Here is the help for my COMMANDS."""
    ABOUT_TXT = """<b>
 🤖 ᴍʏ ɴᴀᴍᴇ :  <a href='https://t.me/MHA_SearchBot'>MHA Searcher</a>
 👨‍💻 ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/SpidyRockss'>Spidy</a>
 📚 ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
 📝 ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a>
 ♻️ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>
 📡 ʜᴏsᴛᴇᴅ ᴏɴ  : <a href='https://www.linode.com/'>VPS</a>
 🥶 ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ3.1.0 [semi-sᴛᴀʙʟᴇ​]
 
 ᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/MOVIES_HUB_ALPHA_OFFICIAL">MHA Team</a> 😏</b>"""
    SOURCE_TXT = """<b>𝙰𝚊𝚋𝚎 𝙰𝚊𝚎 𝙻𝚊𝚞𝚍𝚒𝚢𝚊 🙃

<b>DEVS:</b>
- <a href=https://t.me/LazyDeveloper>LazyDeveloper</a> Lazy Bhai Love U ❤"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and MHA Searcher will respond whenever that keyword hits the message

<b>NOTE:</b>
1. BOT should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. BOT supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MOVIES_HUB_ALPHA_OFFICIAL)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:𝙰𝚊𝚋𝚎 𝙰𝚊𝚎 𝙻𝚊𝚞𝚍𝚒𝚢𝚊 🙃)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of MHA Searcher

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    PROGRESS_BAR = """\n
╭━━━━❰ PROGRESS BAR ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """
