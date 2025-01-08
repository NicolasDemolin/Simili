import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
client_id = os.getenv("client_id_legifrance")
client_secret = os.getenv("client_secret_legifrance")
print(client_id)