import os
from decouple import Config, RepositoryEnv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_FILE = os.path.join(BASE_DIR, '.env')
env_config = Config(RepositoryEnv(DOTENV_FILE))

SERVER_ADDR = env_config.get("SERVER_ADDR")
SERVER_PORT = env_config.get("SERVER_PORT")
MSG_LEN = 1024
