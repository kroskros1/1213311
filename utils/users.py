authorized_users = {307247876}
user_lang = {}
user_freq = {}

def is_authorized(user_id):
    return user_id in authorized_users

def add_user(user_id):
    authorized_users.add(user_id)

def get_lang(user_id):
    return user_lang.get(user_id, "ua")

def set_lang(user_id, lang):
    user_lang[user_id] = lang

def set_freq(user_id, freq):
    user_freq[user_id] = freq
