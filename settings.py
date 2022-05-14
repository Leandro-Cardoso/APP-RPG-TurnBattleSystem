from os import listdir

# Local config:
LANGUAGE = 'pt_br'
LANGUAGES = listdir('languages')
if LANGUAGE not in LANGUAGES:
    LANGUAGE = 'en-us'
LANGUAGE_DIR = 'languages/' + LANGUAGE + '/'
