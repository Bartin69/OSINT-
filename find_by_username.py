import requests
from bs4 import BeautifulSoup
import json
import time

def request_with_retries(url, retries=3, delay=5):
    for i in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response
            else:
                print(f"Failed with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        time.sleep(delay)
    return None

def search_vk(name):
    url = f"https://vk.com/search?c[q]={name}&c[section]=people"
    response = request_with_retries(url)
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for profile in soup.find_all('div', class_='user_name'):
            profile_name = profile.get_text(strip=True)
            profile_url = profile.find('a')['href']
            results.append({
                'name': profile_name,
                'profile_url': f"https://vk.com{profile_url}"
            })
        return results
    return []

def search_telegram(username):
    url = f"https://t.me/{username}"
    response = request_with_retries(url)
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        name_tag = soup.find('div', {'class': 'tgme_page_title'})
        if name_tag:
            return {
                'name': name_tag.get_text(strip=True),
                'profile_url': url
            }
    return {}

def search_ok(name):
    url = f"https://ok.ru/search?st.query={name}&st.cmd=userMain"
    response = request_with_retries(url)
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for profile in soup.find_all('div', class_='gs_result_i_t'):
            profile_name = profile.get_text(strip=True)
            profile_url = profile.find('a')['href']
            results.append({
                'name': profile_name,
                'profile_url': f"https://ok.ru{profile_url}"
            })
        return results
    return []

def search_pinterest(username):
    url = f"https://www.pinterest.com/{username}/"
    response = request_with_retries(url)
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        name_tag = soup.find('h1', {'class': 'tBJ dyH iFc sAJ pBj DrD IZT swG zDA uLJ'})
        if name_tag:
            return {
                'name': name_tag.get_text(strip=True),
                'profile_url': url
            }
    return {}

def search_person(name_or_username):
    results = {
        'vk': search_vk(name_or_username),
        'telegram': search_telegram(name_or_username),
        'odnoklassniki': search_ok(name_or_username),
        'pinterest': search_pinterest(name_or_username),
    }
    return results

def save_results_to_file(results, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    name_or_username = input("Введите имя и фамилию или никнейм: ")
    results = search_person(name_or_username)
    
    # Вывод в консоль
    print(json.dumps(results, ensure_ascii=False, indent=4))
    
    # Сохранение в файл
    save_results_to_file(results, 'osint_results.json')