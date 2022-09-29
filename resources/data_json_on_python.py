import json
# Пока не разобрался как поместить это в class

with open('/Users/antongrunt/Desktop/project/Hillel_selenium/resources/data.json', 'r') as f:
    secret_variables = json.load(f)

NAME_ADMIN = secret_variables['name']
PASSWORD_ADMIN = secret_variables['password']
URL_ENDPOINT = secret_variables['endpoint']


