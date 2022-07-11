import os 
import sys

BOT_TOKEN = '5330673710:AAGYvJ9YfgCS-7fBxnptlGO9fFqFRgVnHH8'
HEROKU_APP_NAME = os.getenv('audiobookbott')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'https://audiobookbott.herokuapp.com/{BOT_TOKEN}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT', 5000))

catalog_page_size = 3
chapters_page_size = 6