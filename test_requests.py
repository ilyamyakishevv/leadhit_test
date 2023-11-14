import requests

URL = "http://127.0.0.1:8000/get_form"

def post_request(user_unput1, user_input2):
    data = {
        "f_name1": f"{user_input1}",
        "f_name2": f"{user_input2}"
    }
    response = requests.post(URL, params=data)
    print(response.text)


if __name__ == "__main__": 
    user_input1 = input("Введите данные для отправки: ")
    user_input2 = input("Введите еще немного данных для отправки: ")
    post_request(user_input1, user_input2)


