import os
import dotenv
import pathlib


def environ():
    BASE_ENV=pathlib.Path() / 'env/.env'
    print("STRATING APP" + str(pathlib.Path('env/.env')))
    if BASE_ENV.exists():
        dotenv.read_dotenv(BASE_ENV)
        ENV=os.environ.get('ENVIRONMENT')

        if ENV=='DEVELOPMENT' or ENV=='DEV':
            DEV_ENV=pathlib.Path() / 'env/dev/.env'
            if DEV_ENV.exists():
                dotenv.read_dotenv(DEV_ENV)
            else:
                print('ERROR: Missing DEV environment variables.')
        elif ENV=='STAGING' or ENV=='STAGE':
            STAGING_ENV=pathlib.Path() / 'env/staging/.env'
            if STAGING_ENV.exists():
                dotenv.read_dotenv(STAGING_ENV)
            else:
                print('ERROR: Missing STAGING environment variables.')
        elif ENV=='PRODUCTION':
            PROD_ENV=pathlib.Path() / 'env/prod/.env'
            if PROD_ENV.exists():
                dotenv.read_dotenv(PROD_ENV)   
            else:
                print('ERROR: Missing PROD environment variables.')
        print('Environment used: '+ENV)
        print('Starting app in '+str(os.environ.get('ENVIRONMENT_NAME')))
        print('Environment path = '+str(os.environ.get('ENVIRONMENT_PATH')))
    else:
        print('ERROR: Missing BASE environment variables.')
    print('Debug is '+str(os.environ.get('DEBUG')))