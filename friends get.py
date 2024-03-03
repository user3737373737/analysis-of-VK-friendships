import vk_api


tok = 'vk1.a.mEMdYdt4WnIoCkdIo-spABdjJzAWZ7lBMBwNmkwbWpu0ZoOCEVLznRReqImaqr0VI0wvTVyF_K0h5sE_WjITwW1pH8J--mZdF0iOoNGbwE-R5fbqCcZI1_3h_VL_TvDUIMk26cKbmYh4wDq3LN2FOZ7DdamdSlq-mxmzK2vg3GV2GihsAqIhgLAwcoOKWp2h'

session = vk_api.VkApi(token=tok)
vk = session.get_api()


def get_friends(user_id):
    friends = session.method("friends.get", {"user_id": user_id})
    for friend in friends["items"]:
        user = session.method("users.get", {"user_ids": friend,
                                            "fields": "city, sex"})
        name = user[0]["last_name"]
        surname = user[0]["first_name"]
        if user[0]["sex"] == 1:
            sex = 'жен'
        else:
            sex = 'муж'
        # birth = user[0]["bdate"]
        # city = user[0]["city"]
        # photo = user[0]["photo_id"]
        print(name, surname, sex)


get_friends(633714088)