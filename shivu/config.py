class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "8156600797"
    sudo_users = "6675050163", "8156600797"
    GROUP_ID = -1002636451157
    TOKEN = "7777554185:AAG9zpq6bdDbVDIL_fMuNaVQLa8Kj92uoSg"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
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
