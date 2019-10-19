from os.path import dirname, abspath, join
from decouple import Config, RepositoryEnv

BASE_DIR = dirname(abspath(__file__))
DOTENV_FILE = join(BASE_DIR, '.env')
env_config = Config(RepositoryEnv(DOTENV_FILE))

SERVER_ADDR = env_config.get("SERVER_ADDR")
SERVER_PORT = env_config.get("SERVER_PORT")
MSG_LEN = 1024
