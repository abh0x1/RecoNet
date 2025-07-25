import whois

def whois_lookup(domain):
        try:
            
            data = whois.whois(domain)
    
            whois_data = {
                        "domain_name": data.domain_name,
                        "registrar": data.registrar,
                        "registrar_url": data.registrar_url,
                        "reseller": data.reseller,
                        "whois_server": data.whois_server,
                        "referral_url": data.referral_url,
                        "updated_date": data.updated_date,
                        "creation_date": data.creation_date,
                        "expiration_date": data.expiration_date,
                        "name_servers": data.name_servers,
                        "status": data.status,
                        "emails": data.emails,
                        "dnssec": data.dnssec,
                        "name": data.name,
                        "org": data.org,
                        "address": data.address,
                        "city": data.city,
                        "state": data.state,
                        "registrant_postal_code": data.registrant_postal_code,
                        "country": data.country
            }
            
            return whois_data
        except Exception as e:
            print(f"{str(e)}")