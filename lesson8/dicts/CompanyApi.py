import requests


class CompanyApi:
    def __init__(self, url):
        self.url = url
        self.haders = {"x-client-token": self.get_token()}

    def get_token(self, user='leonardo', password='leads'):
        creds = {
            'username': user,
            'password': password
            }

        resp = requests.post(self.url+"/auth/login", json=creds)
        return resp.json()["userToken"]

    def get_comany_list(self, params_to_add=None):
        resp = requests.get(self.url+"/company", params=params_to_add)
        return resp.json()

    def get_company(self, id):
        resp = requests.get(self.url + "/company" + str(id))
        return resp.json()

    def create_company(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }

        resp = requests.post(self.url+'/company', json=company, headers=self.haders)
        return resp.json()

    def edit(self, new_id, new_name, new_descr):
        company = {
            "name": new_name,
            "description": new_descr
        }

        resp = requests.patch(self.url+"/company" + str(new_id), headers=self.haders, json=company)
        return resp.json()

    def delete(self, id):
        resp = requests.get(self.url+"/company/delete" + str(id), headers=self.haders)
        return resp.json()

    def set_active_state(self, id, isActive):
        resp = requests.patch(self.url+"/company/status" + str(id), headers=self.haders, json={"isActive": isActive})

        return resp.json()
