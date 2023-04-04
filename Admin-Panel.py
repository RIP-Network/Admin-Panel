#!/usr/bin/python

#!/usr/bin/python

import os
import time
import sys
import requests as req
from colorama import Fore, init
from colored import fg, bg, attr
import pyuseragents as agent

os.system('clear')

class color:
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[36m'
    pink = '\033[35m'
    orang = '\033[34m'
    white = '\033[00m'
def banner():
    print(f'''


{color.red}   _____       .___      .__                                    .__      _____.__            .___            {color.red}
{color.red}  /  _  \    __| _/_____ |__| ____   ___________    ____   ____ |  |   _/ ____\__| ____    __| _/___________ {color.red}
{color.red} /  /_\  \  / __ |/     \|  |/    \  \____ \__  \  /    \_/ __ \|  |   \   __\|  |/    \  / __ |/ __ \_  __ \{color.red}
{color.red}/    |    \/ /_/ |  Y Y  \  |   |  \ |  |_> > __ \|   |  \  ___/|  |__  |  |  |  |   |  \/ /_/ \  ___/|  | \/{color.red}
{color.red}\____|__  /\____ |__|_|  /__|___|  / |   __(____  /___|  /\___  >____/  |__|  |__|___|  /\____ |\___  >__|   {color.red}
{color.red}        \/      \/     \/        \/  |__|       \/     \/     \/                      \/      \/    \/       {color.red}

{color.red}Created by RIP-Network  V1.0{color.red}

{color.red}https://github.com/RIP-Network{color.red}

''')

banner()

print(Fore.WHITE+'['+Fore.RED+'#'+Fore.WHITE+'] Ingrese la URL por ejemplo: google.com (sin http o https)')

target_url = input('TARGET [URL] '+Fore.RED+'>_'+Fore.GREEN+' ')


print(Fore.RESET+'')

if len(target_url) < 5:
    print('['+Fore.RED+'!'+Fore.WHITE+']'+Fore.YELLOW+' El enlace es demasiado corto vuelvalo a intentar')
    time.sleep(3.0)
    sys.exit()
else:
    pass

if 'http://' or 'https://' in target_url:
    pass


if 'http://' or 'https://' not in target_url:
    target_url = 'http://'+target_url

test = req.get(target_url)

time.sleep(5)

if test.status_code == 200:
    pass

else:
    print(Fore.RED+'Imposible conectarse al objetivo '+Fore.WHITE+'> '+Fore.YELLOW+''+target_url)
    sys.exit()
target_url = target_url.replace('http://', '')
print (f'''
{color.red}Metodos:{color.red}

    {color.red}Metodo 1 :
        {color.red}el buscador de subdominios para encontrar subdamins de {target_url}{color.red}
        {color.red}prueba de ejemplo con sub_manual:{color.red}
        {color.red}objetivo > {target_url}{color.red}
        {color.red}ejemplo > administrador.{target_url}{color.red}
        {color.red}ejemplo > cpanel.{target_url}{color.red}

    {color.red}Metodo 2:{color.red}
        
        {color.red}los paneles de administración de {target_url}{color.red}
        {color.red}ejemplo de búsqueda con lista manual:{color.red}
        {color.red}objetivo > {target_url}{color.red}
        {color.red}ejemplo > {target_url}/admin{color.red}
        {color.red}ejemplo > {target_url}/cpanel{color.red}
    


''')

select_method = input('Selecciona el metodo : 1 subdomain finder —— 2 administration finder '+Fore.WHITE+'> :'+Fore.WHITE+' ')
os.system('sleep 4')
os.system('clear')

print(f'''


{color.red}   _____       .___      .__                                    .__      _____.__            .___            {color.red}
{color.red}  /  _  \    __| _/_____ |__| ____   ___________    ____   ____ |  |   _/ ____\__| ____    __| _/___________ {color.red}
{color.red} /  /_\  \  / __ |/     \|  |/    \  \____ \__  \  /    \_/ __ \|  |   \   __\|  |/    \  / __ |/ __ \_  __ \{color.red}
{color.red}/    |    \/ /_/ |  Y Y  \  |   |  \ |  |_> > __ \|   |  \  ___/|  |__  |  |  |  |   |  \/ /_/ \  ___/|  | \/{color.red}
{color.red}\____|__  /\____ |__|_|  /__|___|  / |   __(____  /___|  /\___  >____/  |__|  |__|___|  /\____ |\___  >__|   {color.red}
{color.red}        \/      \/     \/        \/  |__|       \/     \/     \/                      \/      \/    \/       {color.red}

{color.red}Created by RIP-Network  V1.0{color.red}

{color.red}https://github.com/RIP-Network{color.red}

''')


def sub_manual():

    print('['+Fore.GREEN+'*'+Fore.WHITE+'] Objetivo >>> '+Fore.GREEN+''+target_url)

    

    links = open('.sub.txt', 'r').read().split()

    for link in links:

        def heders():
            hd = agent.random()
            return hd
        heders1 = {
    'User-Agent': heders()
    }
        try:
            url = ('http://'+link+'.'+target_url)
        
        except KeyboardInterrupt:
            print('\nBye !')
            time.sleep(3)
            sys.exit()



        try:
            get_req = req.get(url, timeout=5, headers=heders1)
            print(f'['+Fore.GREEN+'OK'+Fore.WHITE+'] OK - URL > %s%s {} %s'.format(url) % (fg('black'), bg('green'), attr('reset')))
        
        except Exception:
            print(f'['+Fore.RED+'NOT'+Fore.WHITE+'] FAIL - URL > %s%s {} %s'.format(url) % (fg('black'), bg('red'), attr('reset')))
    
        except KeyboardInterrupt:
            print('\nBye !')
            time.sleep(3)
            sys.exit()
        

def manual_list():

    print('['+Fore.GREEN+'*'+Fore.WHITE+'] Objetivo >>> '+Fore.GREEN+''+target_url)

    links = open('.link.txt', 'r').read().split()

    for link in links:
        def heders():
            hd = agent.random()
            return hd
        heders1 = {
    'User-Agent': heders()
    }

        try:
            url = ('http://'+target_url+'/'+link)
            get_req = req.get(url, timeout=5, headers=heders1)
        except KeyboardInterrupt:
            print('\nBye !')
            time.sleep(3)
            sys.exit()

        sisad = 399
        charsad = 400
        charnono = 499


        try:
            if get_req.status_code < sisad:
                print(f'['+Fore.GREEN+'OK'+Fore.WHITE+'] OK - URL > %s%s {} %s'.format(url) % (fg('black'), bg('green'), attr('reset')))
            
            if get_req.status_code > charsad:
                print(f'['+Fore.RED+'NOT'+Fore.WHITE+'] FAIL - URL > %s%s {} %s'.format(url) % (fg('black'), bg('red'), attr('reset')))
    
            if get_req.status_code > charnono:
                print(f'['+Fore.YELLOW+'Server-ERROR'+Fore.WHITE+'] ERROR 404 - URL > %s%s {} %s'.format(url) % (fg('white'), bg('yellow'), attr('reset')))
    
        except KeyboardInterrupt:
            
            
            print('\nBye !')
            time.sleep(3)
            sys.exit()

if select_method == '1':
    sub_manual()
elif select_method == '2':
    manual_list()
else:
    print (Fore.RED+'ERROR'+Fore.WHITE+' Por favor eliga un metodo valido 1 o 2   \n Enter para salir .')
    input ('')
    sys.exit(1)
