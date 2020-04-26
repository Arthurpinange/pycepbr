from postman import Address as a

if __name__ == '__main__':
    print('test get_address')
    cep = '01001000'
    print(a.get_address(cep))
    print('********************')
    print('test get_street')
    uf = 'RS'
    cidade = 'Porto Alegre'
    bairro = 'Domingos Jose'
    endereco = {'UF': uf, 'cidade': cidade, 'bairro': bairro}

    print(a.get_street(endereco))
