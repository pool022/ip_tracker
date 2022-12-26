import requests
import os

def erase():
    os.system('cls' if os.name == 'nt' else 'clear')

RED = '\033[91m'
GREEN= '\033[92m'
YELLOW= '\033[93m'
BLUE= '\033[94m'
MAGENTA= '\033[95m'
CYAN= '\033[96m'
WHITE= '\033[0m'



erase()
ip = input("Ip Address: ").strip()
erase()

def get_info():
    res = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query")

    data = res.json()
    status = res.status_code

    ip_address = data["query"]
    lon = float(data["lat"])
    lat = float(data["lon"])
    city = data["city"]
    region = data["region"]
    continent = data["continentCode"]
    country = data["country"]
    country_abbrev = data["countryCode"]
    regionside = data["regionName"]
    postal = data["zip"]
    timezone = data["timezone"]
    isp = data["isp"]
    org = data["org"] 
    asn = data["as"]

    print(f'''    {WHITE}API status code: {RED}{status}\n
    {WHITE}IP Address: {RED}{ip_address}
    {WHITE}city: {RED}{city}
    {WHITE}region: {RED}{regionside}, {WHITE}({RED}{region}{WHITE})
    country: {RED}{country} {WHITE}({RED}{country_abbrev}{WHITE})
    {WHITE}postal/zip: {RED}{postal}
    {WHITE}timezone: {RED} {timezone}
    {WHITE}ISP: {RED}{isp}
    {WHITE}Provider: {RED}{org}
    {WHITE}ASN: {RED}{asn}
    {WHITE}Lat:{RED} {lat}\n    {WHITE}long:{RED} {lon}
    ''')
    
get_info()