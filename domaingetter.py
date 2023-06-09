import requests

def get_domain_data(domain):

    # Check robots.txt
    robots_request = requests.get("https://"+ domain + "/robots.txt")
    if robots_request.status_code == 200:
        robots_txt = robots_request.text
    else:
        robots_txt = "Not found"

    #check archive.org
    wayback_request = requests.get("https://archive.org/wayback/available?url="+ domain)
    
    wayback_data = wayback_request.json()

    # get subdomains

    subdomain_request = requests.get("https://columbus.elmasy.com/lookup/"+ domain)
    
    subdomain_data = subdomain_request.text


    domain_data = {
        "sources":[
            
            {
                "title": "robots_txt",
                "content": robots_txt
            },
            {
                "title": "wayback_machine",
                "content": wayback_data
            },
            {
                "title": "subdomains",
                "content": subdomain_data
            }
        ]
    }

    return domain_data