import configuration
import data
import requests

from data import auth_token


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

def post_new_client_kit(kit_body,auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                         json = kit_body,  # inserta el cuerpo de solicitud
                         headers = data.headers)  # inserta los encabezados

response = post_new_client_kit(data.kit_body,auth_token)
print(response.status_code)
print(response.json())