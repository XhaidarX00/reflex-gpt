from .utilis import *

# with open(path, 'r') as file:
with open('cookies_headers.json', 'r') as file:
    data = json.load(file)

# Mengambil cookies dan headers
cookies = data.get("cookies", {})
headers = data.get("headers", {})

# from decouple import config

# # Mengambil cookies dan headers
# cookies = config("cookies", default=None)
# headers = config("headers", default=None)

params = {
    'batch': '1',
}

json_data = {
    '0': {
        'json': {
            'title': 'Percakapan Baru',
            'botId': 2,
        },
    },
}

response = requests.post(
    'https://chat.hix.ai/api/trpc/hixChat.createChat',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)


def createChatId():
    data = json.loads(response.content)
    id_value = data[0]['result']['data']['json']['id']
    return id_value
