class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "8156600797"
    sudo_users = "6675050163", "8156600797"
    GROUP_ID = -1002636451157
    TOKEN = "7777554185:AAG9zpq6bdDbVDIL_fMuNaVQLa8Kj92uoSg"
    mongo_url = "mongodb+srv://BesicWaifubot:TGDARK11798@cluster0.rg9k8ag.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://graph.org/file/e7141e5486f22f92e35dd-1159f787abdf660245.jpg", "https://graph.org/file/4335bf26d5b8de64a5aa2-caced1ff4b83d82478.jpg"]
    SUPPORT_CHAT = "t.me/voixVerse_Group_Chat"
    UPDATE_CHAT = "https://t.me/+Gq6FEGLuwa5mMDBl"
    BOT_USERNAME = "BasicWaifuBot"
    CHARA_CHANNEL_ID = "-1002527180063"
    api_id = 28159105
    api_hash = "a0936ddf210a7e091e19947c7dc70c91"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
