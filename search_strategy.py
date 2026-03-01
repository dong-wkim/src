import requests
import bs4
import selenium

# To be revised

def api(url, file):
    url = 'https://' + input('Enter the url: ')
    site =  url
    file = input('Enter the output file name: ') + '.txt' 
    
    response = requests.get(site)
    response.raise_for_status()
    
    with open(file, 'wb') as play_file:
        for chunk in response.iter_content(100000):
            play_file.write(chunk)

