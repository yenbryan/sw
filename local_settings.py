DATABASES = {
    'default': {
        # 'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'ENGINE':'django.contrib.gis.db.backends.postgis',
        'NAME':     'fundy',
    }
}
