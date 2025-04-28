import requests
import hashlib


def request_api_data(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching data from API: {response.status_code}')
    return response


def get_password_leaks_count(hashes, hash_to_check):
    hash_count_pairs = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hash_count_pairs:
        if h == hash_to_check:
            return int(count)
    return 0


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    response = request_api_data(prefix)
    return get_password_leaks_count(response, suffix)


if __name__ == "__main__":
    password = input('Enter your password: ')
    leaks_count = pwned_api_check(password)
    if leaks_count:
        print(f'This password has been leaked {leaks_count} times. You should consider changing it.')
    else:
        print('Your password has not been found in any known breaches. Good job!')
