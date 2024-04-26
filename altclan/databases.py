DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': os.getenv('DATABASE_NAME'),
       'USER': os.getenv('USER'),
       'PASSWORD': os.getenv('PASSWORD'),
       'HOST': os.getenv('HOST'),
       'PORT': '5432',
   }
}


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'db.sqlite3',
      
   }
}
