import json
import requests


class Address:

    def __init__(self):
        pass

    @staticmethod
    def get_address(cep):
        """
        returns the address from the zip code
        :param cep:
        :return:
        """
        url = 'http://viacep.com.br/ws/'+cep+'/json/'
        req = requests.get(url)

        if req.status_code == 200:
            json_data = json.loads(req.content)
            return json_data
        return

    @staticmethod
    def get_street(public_place):
        """
        returns all streets and zip codes from the neighborhood
        :param public_place:
        :return:
        """
        uf = public_place['UF']
        cidade = public_place['cidade']
        bairro = public_place['bairro']

        url = 'http://viacep.com.br/ws/'+uf+'/'+cidade+'/'+bairro+'/json/'
        req = requests.get(url)

        if req.status_code == 200:
            json_data = json.loads(req.content)
            return json_data
        return
