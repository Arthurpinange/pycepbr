# pycepbr
 Consulta CEPs de todo território brasileiro

 Você que precisa consultar um endereço a partir de um cep, identificar o CEP de uma determinada rua de forma rápida  o pycepbr vai lhe ajudar muito.
 
 Para obter acesso a todos os CEPs de forma atualizada consumimos o webservice do viacep, você que é DEV e não conhece o ótimo trabalho dos caras devia dar uma olhada. 

Dessa forma para facilitar nossa vida o pycepbr é um pacote em python que já vai nos entregar os dados tratados.

### Como instalar

    pip install https://github.com/Arthurpinange/pycepbr.git
    
vamos precisar instalar duas dependências

    pip install requests
    pip install json

### Agora podemos conhecer os nosso métodos

 * get_address → retorna um dicionário com o endereço recebendo o CEP como parâmetro.

 * get_street → retorna um dicionários com n endereços recebendo um dicionário por parâmetro com UF, Cidade, Bairro e Rua, por exemplo se você passar o nome da rua apenas com “João” o Metodo vai retornar um dicionário com todos endereços que contem “João” no nome da rua.

