from ipwhois import IPWhois

def lookup_ip_whois(ip_address):
    result = {}
    try:
        obj = IPWhois(ip_address)
        data = obj.lookup_rdap()

        result['IP'] = ip_address
        result['Network Name'] = data.get('network', {}).get('name', 'N/A')
        result['Country'] = data.get('network', {}).get('country', 'N/A')
        result['Start Address'] = data.get('network', {}).get('start_address', 'N/A')
        result['End Address'] = data.get('network', {}).get('end_address', 'N/A')
        result['ASN'] = data.get('asn', 'N/A')
        result['ASN Description'] = data.get('asn_description', 'N/A')

    except Exception as e:
        result['Error'] = str(e)

    return result
