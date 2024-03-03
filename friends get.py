import vk_api


token = ''

session = vk_api.VkApi(token=token)
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


get_friends(1)