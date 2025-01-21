import requests


base_url = "https://x-clients-be.onrender.com"

def test_semple_req():
    resp = requests.get(base_url+"/company")

    response_body = resp.json()
    first_company = response_body[0]
    assert first_company["name"] == "Барбершоп 'ЦирюльникЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"

def test_auth():
    creds = {
        'username': 'leonardo',
        'password': 'leads'
    }
    

    resp = requests.post(base_url+"/auth/login", json=creds)
    token = resp.json()["userToken"]
    assert resp.status_code == 201

def test_create_company():
    creds = {
        'username': 'leonardo',
        'password': 'leads'
    }
    
    company = {
        'name': 'Весельчак',
        'description': 'Организация детских праздников'
    }
    
    # авторизация
    resp = requests.post(base_url+"/auth/login", json=creds)
    token = resp.json()["userToken"]

    # создание организации
    my_heders = {}
    my_heders['x-client-token'] = token
    
    resp = requests.post(base_url+"/company", json=company, headers=my_heders)
    assert resp.status_code == 201
