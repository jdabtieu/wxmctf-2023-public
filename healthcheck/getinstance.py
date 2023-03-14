import requests

def getinstance(session, host, chall_id):
    s = requests.Session()
    s.cookies["sessionid"] = session
    r = s.get(f"{host}/problem/{chall_id}", timeout=2)
    if r.status_code != 200:
        raise LookupError(f"{r.status_code}")
    head = {"x-csrftoken": s.cookies["csrftoken"]}
    r = s.get(f"{host}/problem/{chall_id}/challenge", headers=head, timeout=2)
    if r.status_code != 200:
        raise LookupError(f"{r.status_code}")
    elif r.text == "null":
        r = s.post(f"{host}/problem/{chall_id}/challenge", headers=head, timeout=2)
        if r.status_code != 200:
            raise LookupError(f"{r.status_code}")
        elif r.text == "null":
            raise Exception()
    data = r.json()
    return data["endpoints"][0]["host"], data["endpoints"][0]["port"]
