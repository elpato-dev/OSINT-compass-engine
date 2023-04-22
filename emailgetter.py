import requests

def get_email_data(email):
    
    # query spycloud
    spycloud_response = requests.get("https://portal.spycloud.com/endpoint/enriched-stats/" + email)
    spycloud_data = spycloud_response.json()

    # query pingutil

    pingutil_response = requests.get('https://api.eva.pingutil.com/email?email=' + email, verify=False)
    pingutil_data = pingutil_response.json()

    email_data = {
        "sources":[
            
            {
                "title": "spycloud",
                "content": spycloud_data
            },
            {
                "title": "pingutil",
                "content": pingutil_data
            }

        ]
    }
    return email_data
