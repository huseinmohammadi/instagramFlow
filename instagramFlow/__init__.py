import psycopg2
from psycopg2.extras import RealDictCursor



class App():

    def env(self, name: str, default: str = None):
        envF = open('./.env', 'r')
        Lines = envF.readlines()
        for line in Lines:
            envA = line.split('=')
            if envA[0].strip() == name:
                val = envA[1].strip()
                if val.lower() == "true":
                    return True
                elif val.lower() == "false":
                    return False
                else:
                    return envA[1].strip()
        return default

    
    def db_connection(self=None):
        conn = psycopg2.connect(
            dbname=App().env('DB_NAME'),
            host=App().env('DB_HOST'),
            user=App().env('DB_USERNAME'),
            password=App().env('DB_PASSWORD'),
            port=App().env('DB_PORT')
        )

        conn.autocommit = True

        return conn.cursor(cursor_factory=RealDictCursor)