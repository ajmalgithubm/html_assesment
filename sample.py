import requests
import hashlib
import random 
import string

def generate_random_name():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(10))

def calculate_mad5_hash(name):
    return hashlib.md5(name.encode()).hexdigest()

def send_post_request(url, name, code):
    headers = {'Authorization':f'Bearer{code}'}
    data = {
        'name' : name,
        'code' : code
    }
    try:
        response = requests.post(url, data=data, headers=headers)

        if response.status_code == 200:
            print('post request is Successfull')
            print(response.json())
        else:
            print('post request failed')
    except requests.exceptions.RequestException as e:
        print('An error occur' + {e})


if __name__ == '__main__':
    api_url = 'https://dev.29kreativ.com/recruitment/levels/'

    random_name = generate_random_name()
    md5_hash = calculate_mad5_hash(random_name)
    send_post_request(api_url, random_name, md5_hash)