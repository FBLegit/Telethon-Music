import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20554636"))
    API_HASH = os.environ.get("API_HASH", "c2aaacd61ce709d0a67c8537059bb5fb")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6359288426:AAFvbaibkOTs6VwGjS2pEVXPblMK-6yR79E")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1sBu6UeUcvAMT87fsNzXmsNBUmOVyFo9MolthgXkYQ4L66ebqVFQU_L52Nvuas_EGMTGxDyEKBZBfxpMtUNoBRgUvCo3B3YRvdHIt3UuSSGoxzdXvIzLhhxgC_16pL3i9h_EzVUpzUmp0ukiTyFiBFzdFDr_-VkjUvp74kcLC165qXRMH_9vuHtlR6x4TNNfoA38JCRJjPXe3N64H1TXBmD3qGmFVBU8ue-F1BdtzKRlSzvxf2IlSO6jrGVj32GIKOtw8G_aTgjt8z79MlI17gVa4njwRYDdMcbE6lGu4CxNzn8OtaFItrmrsnGqX3Pv3LdsxYy1ioDAyM_u7cKCCKi2aw=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "fayask_bot")
    SUPPORT = os.environ.get("SUPPORT", "Legit") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Rematric") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6483965508")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
