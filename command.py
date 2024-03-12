# help: python3 command.py migrate:fresh
import glob
import os
import sys
from instagramFlow import App


command = sys.argv[1]
commandA = command.strip().split(':')
conn = App.db_connection()


if commandA[0]:
    if commandA[0] == "migrate":
        if len(commandA) > 1:
            if commandA[1] == 'fresh':
                conn.execute("DO $$ DECLARE\
                    r RECORD;\
                BEGIN\
                    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP\
                        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';\
                    END LOOP;\
                END $$;")

        try:
            conn.execute('SELECT 1 from migrations')
        except:
            conn.execute("""CREATE TABLE IF NOT EXISTS migrations
            (
                id SERIAL PRIMARY KEY,
                migration character varying(191) NOT NULL,
                batch integer NOT NULL
            )""")

        sqlFiles = glob.glob('./database/migrations/*.sql')
        for sqlFile in sqlFiles:
            fileName = os.path.basename(sqlFile)
            conn.execute("select id from migrations where migration='" + fileName + "'")

            if conn.fetchone() is None:
                conn.execute(open(sqlFile, 'r', encoding="utf8").read())
                conn.execute("insert into migrations (migration, batch) values('" + fileName + "', 1)")
                print("Migration " + fileName + " Done!")
    else:
        print("Command Not Found!")
