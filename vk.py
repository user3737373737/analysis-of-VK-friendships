import vk_api
import vk
import requests


tok = 'vk1.a.mEMdYdt4WnIoCkdIo-spABdjJzAWZ7lBMBwNmkwbWpu0ZoOCEVLznRReqImaqr0VI0wvTVyF_K0h5sE_WjITwW1pH8J--mZdF0iOoNGbwE-R5fbqCcZI1_3h_VL_TvDUIMk26cKbmYh4wDq3LN2FOZ7DdamdSlq-mxmzK2vg3GV2GihsAqIhgLAwcoOKWp2h'
login = 'gorelova_2008@vk.com'
password = 'gorelowa375689'
access_token = '22rJ4XkoxgM0PWbSYjBT'
server_access_token = '1b47eba61b47eba61b47eba6a118508cf011b471b47eba67e9a221d602c56249c8475a0'
id = '51865430'
"""
https://oauth.vk.com/authorize?client_id=51865430&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,status,groups&response_type=token&v=5.21


https://oauth.vk.com/blank.html#access_token=vk1.a.mEMdYdt4WnIoCkdIo-spABdjJzAWZ7lBMBwNmkwbWpu0ZoOCEVLznRReqImaqr0VI0wvTVyF_K0h5sE_WjITwW1pH8J--mZdF0iOoNGbwE-R5fbqCcZI1_3h_VL_TvDUIMk26cKbmYh4wDq3LN2FOZ7DdamdSlq-mxmzK2vg3GV2GihsAqIhgLAwcoOKWp2h&expires_in=86400&user_id=633714088
"""
#session = vk.Session()
#v = vk.API(session)

"""
friends_url = 'https://api.vk.com/method/status.get?user_id={}'
# также вы можете добавить access_token в запрос, получив его через OAuth 2.0
json_response = requests.get(friends_url.format()).json()
if json_response.get('error'):
    print(json_response.get('error'))
"""


vk_session = vk_api.VkApi(token=tok)
vk = vk_session.get_api()
user_info = vk.users.get(users_ids=217435224)

first_name = user_info[0]['first_name']
last_name = user_info[0]['last_name']
print(f'Имя пользователя: {first_name}, {last_name}')
"""
def send(msg):
    vk.messages.send(user_id = 633714088, message = msg, random_id=0 )

while True:
    send(input())
"""
