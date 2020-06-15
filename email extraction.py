import requests
from bs4 import BeautifulSoup as soup
import re
import pyfiglet
emails_encontrados = []
telefone_encontrados = []
ascii_banner = pyfiglet.figlet_format("Programmed by slaki")
print(ascii_banner)
header = {
'user_agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
}
proxy = {
'https':'200.255.122.170:8080'
}
escolha = int(input("Voce deseja extrair email(0)/ Ou telefone(1) ?: "))
if escolha == 0:
    print(pyfiglet.figlet_format("email extractor"))

    try:
        url = requests.get(input('Digite a url: ').strip(),headers = header, proxies = proxy).text
        a = soup(url,'html.parser').prettify()
        mail = re.findall('[a-zA-Z\.-]+@[\w\.-]+',a)

        with open('emails.txt','a') as email:
         for emails in mail:
            emails_encontrados.append(emails)
            email.write(emails + '\n')
            print(emails)
    except Exception as erro:
        print(f'Ocorreu um erro inesperado {erro}')
elif escolha == 1:
    print(pyfiglet.figlet_format("tel extractor"))
    try:

        url = requests.get(input('Digite a url: ').strip(), headers=header, proxies=proxy).text
        a = soup(url, 'html.parser').prettify()
        tele = re.findall('(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})', a)
        with open('telefones.txt','a') as tel:
            for telefone in tele:
                telefone_encontrados.append(telefone)
                tel.write(str(telefone[1]) + '\n')
                print(telefone)
    except Exception as erro:
        print(f'Ocorreu um erro inesperado {erro}')
else:
    print('Digite apenas numeros/Digite apenas os numeros mostrados')
