from pathlib import Path
from decouple import config


TOKEN = config('TOKEN')

BASE_DIR = Path(__file__).resolve().parent.parent
