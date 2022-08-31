import requests


def getusersdata():
    url = "https://api.heroku.com/teams/autodesk-stg/members"

    payload = {}
    headers = {
        'Accept': 'application/vnd.heroku+json; version=3',
        'Authorization': 'Bearer b65c71d5-e78b-4097-8443-e07b4b76e15e'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code, response.headers, response.text, sep="\n")
    return response.status_code, response.headers, response.text
