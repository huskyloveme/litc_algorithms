import requests
from bs4 import BeautifulSoup

wp_login = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
wp_admin = 'http://45.79.43.178/source_carts/wordpress/wp-admin/'
username = 'admin'
password = '123456aA'

def sent_rq():

    datas = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In',
        'testcookie': '1'
    }
    resp = requests.Session().post(wp_login, data=datas)
    
    new_headers = "Cookie: "
    for c in resp.cookies:
        new_headers += c.name
        new_headers += '='
        new_headers += c.value
        new_headers += ';'
    
    new_headers = new_headers[:-1]

    headers = {
        'Cookie': new_headers
    }

    resp2 = requests.Session().get(wp_admin, headers=headers)

    soup = BeautifulSoup(resp2.content, 'html.parser')

    soup.prettify()

    form = soup.find_all('span', class_='display-name')[0].get_text()
    print(form)

if __name__ == '__main__':
    sent_rq()
