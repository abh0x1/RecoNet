import dns.resolver

def resolve_dns(domain):
    records = {}

    try:
        a_records = dns.resolver.resolve(domain, 'A')
        records['A'] = [r.address for r in a_records]
    except Exception as e:
        records['A'] = [f"Error: {str(e)}"]

    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        records['MX'] = [str(r.exchange) for r in mx_records]
    except Exception as e:
        records['MX'] = [f"Error: {str(e)}"]

    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        records['NS'] = [str(r.target) for r in ns_records]
    except Exception as e:
        records['NS'] = [f"Error: {str(e)}"]

    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        records['TXT'] = [
            b''.join(r.strings).decode('utf-8') if r.strings else ''
            for r in txt_records
        ]
    except Exception as e:
        records['TXT'] = [f"Error: {str(e)}"]

    return records