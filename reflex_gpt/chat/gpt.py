from .create_chat import createChatId
from .utilis import *
# from check_text import checkWord

# with open(path, 'r') as file:
with open('cookies_headers.json', 'r') as file:
    data = json.load(file)


# Mengambil cookies dan headers
cookies = data.get("cookies", {})
headers = data.get("headers", {})

from decouple import config

# # Mengambil cookies dan headers
# cookies = config("cookies", default=None)
# headers = config("headers", default=None)


def get_response_value(prompt):
    try:
        # chat_id = os.getenv('chat_id') # ini menggunakan load_env
        chat_id = config('CHAT_ID', cast=str, default=None) # ini pakai decouple
        
        coba = 1
        while coba <= 3:
            json_data = {
                'chatId': chat_id,
                'question': prompt,
                'fileUrl': '',
            }
            
            response = requests.post('https://chat.hix.ai/api/hix/chat', cookies=cookies, headers=headers, json=json_data)
            if response.status_code == 200:
                data = response.text
                matches = re.findall(r'{"content":"(.*?)"}', data)
                text = "".join(matches)
                text = text.replace(r'\n', '\n')
                text_voice = filter_special_characters(text)
                # data, text_voice = extract_content(response_text=response.text)
                
                # temp = ''
                # for text_ in text.split(" "):
                #     temp += f" {text_}"
                #     print(temp)
                
                return text, text_voice
            else:
                logging.info(f"Response tidak 200, status code: {response.status_code}")
                try:
                    logging.info("Mencoba membuat ulang percakapan")
                    chat_id = createChatId()
                    if chat_id:
                        is_update = update_env_variable('CHAT_ID', chat_id)
                        if is_update:
                            logging.info("Berhasil menambahkan chat id yang baru")
                        else:
                            logging.info("Gagal menambahkan chat id yang baru")
                    
                except Exception as e:
                    logging.info(f"Error create chat id: {e}")
                    return None
                
                coba += 1
    except Exception as e:
        logging.info(f"Error in get answer gpt: {e}")
        return None, None


# def extract_content(response_text):
#     matches = re.findall(r'{"content":"(.*?)"}', response_text)
#     text = "".join(matches)
#     result = checkWord(text)
#     text_voice = filter_special_characters(result)
#     print(test)
#     print("="*20)
#     print("="*20)
#     if result:
#         return result, text_voice
#     else:
#         return


def getAnswer(prompt):
    # prompt = input("Masukan Prompt: ")
    prompt_awal = "Kamu adalah asisten virtual bernama darmi, berikan jawaban singkat di bawah 200 karakter dan gunakan bahasa gaul bergaya bahasa anak muda indonesia, dari pertanyaan dibawah:"
    prompt = f'{prompt_awal}\n{prompt}'
    text_voice = None
    coba = 1
    try:
        while coba <= 3:
            content, text_voice = get_response_value(prompt=prompt)
            if content:
                return content
            else:
                coba += 1
                time.sleep(1)
    except:
        return None
    


# if __name__ == "__main__":
#     getAnswer("apa itu manusia?")
    
    # while True:
        # getAnswer()