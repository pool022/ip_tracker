import os
import requests
import argparse

RED = '\033[91m'
GREEN= '\033[92m'
YELLOW= '\033[93m'
BLUE= '\033[94m'
MAGENTA= '\033[95m'
CYAN= '\033[96m'
WHITE= '\033[0m'


def erase():
    os.system('cls' if os.name == 'nt' else 'clear')

def cwrap(data: str, type: str = 'R') -> str:
    '''
    Formats the data with the given color codes.
    :param data: str Data to format
    :param type: str Color code type
    :return: str 
    '''
    match type:
        case 'R': # Red
            return '{}{} '.format(RED, data)
        case 'RN': # Red, NewLine
            return '{}{}\n'.format(RED, data)
        case 'WRW': # White, Red, White
            return '{}({}{}{})'.format(WHITE, RED, data, WHITE)

def get_info(ip: str) -> dict:
    '''
    Request data from api and organize in dictionary.
    :param ip: str User IP to query.
    :return: dict Response data to output.
    '''
    # Response data
    res = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query")
    data = res.json()
    status = res.status_code

    # Check for api success
    if data['status'] == 'fail':
        return { }

    return {
        'API status code': status,
        'IP Address':      cwrap(data["query"]),
        'city':            cwrap(data["city"]),
        'region':          cwrap(data["regionName"]+',') + \
                           cwrap(data["region"], 'WRW'),
        'country':         cwrap(data['country']) + \
                           cwrap(data['countryCode'], 'WRW'),
        'postal/zip':      cwrap(data["zip"]),
        'timezone':        cwrap(data["timezone"]),
        'ISP':             cwrap(data["isp"]),
        'Provider':        cwrap(data["org"]),
        'ASN':             cwrap(data["as"]),
        'Lat':             cwrap(float(data["lon"])),
        'Long':            cwrap(float(data["lat"]))
    }

def display_info(data: dict) -> None:
    '''
    Go through dictionary and output data to screen.
    :param data: dict Data from api request.
    '''
    # Invalid api request check.
    if not data:
        print('[!] Invalid input!')
        return

    # Display dict data.
    for k, v in enumerate(data):
        print('{}{}: {}'.format(WHITE, v, data[v]))

if __name__=='__main__':
    argParser = argparse.ArgumentParser()
    argParser.add_argument('ip', help='IP to query.')
    args = argParser.parse_args()
    # Grab data from request.
    data = get_info(args.ip)
    # Display data
    display_info(data)