DEBUG = True
APP_TITLE = 'Notes'
SALT_LENGTH = 64

# Configuration data that will be pushed to any rendered page ever
data = {
    'app_title'  : APP_TITLE,
    'page_title' : 'home'
}

DB_NAME = "notes_app"

NOTES_TABLE_NAME  = "notes"