import requests
import ipaddress
import json

def validate_ip(ip):
    try:
        ip__ = ipaddress.ip_address(ip)
        return 0
    except:
        return 1


def get_location(ip): 
    response = requests.get(f'https://ipapi.co/{ip}/json/').json()
    location_data = {
        "ip": ip,
        "network": response.get("network"),
        "version": response.get("version"),
        "city": response.get("city"),
        "region": response.get("region"),
        "region_code": response.get("region_code"),
        "country": response.get("country"),
        "country_name": response.get("country_name"),
        "country_code": response.get("country_code"),
        "country_code_iso3": response.get("country_code_iso3"),
        "country_capital": response.get("country_capital"),
        "country_tld": response.get("country_tld"),
        "continent_code": response.get("continent_code"),
        "in_eu": response.get("in_eu"),
        "postal": response.get("postal"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "timezone": response.get("timezone"),
        "utc_offset": response.get("utc_offset"),
        "country_calling_code": response.get("country_calling_code"),
        "currency": response.get("currency"),
        "currency_name": response.get("currency_name"),
        "languages": response.get("languages"),
        "country_area": response.get("country_area"),
        "country_population": response.get("country_population"),
        "asn": response.get("asn"),
        "org": response.get("org")
    }
    return location_data

ip = input('IP: ')

y = json.dumps(get_location(ip), indent=4)
print(y)
