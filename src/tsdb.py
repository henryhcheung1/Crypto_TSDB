import sqlalchemy as db

# TODO: 
# - add caching functionality ?
# - dont rewrite into TSB when their are duplicate entries (determined by date / time)
class TSDB:

    def __init__(self, driver: str, username: str, password: str, hostname: str, port: str, database: str):

        engine = db.create_engine(f"{driver}://{username}:{password}@{hostname}:{port}/{database}")

        connection = engine.connect()

        metadata = db.MetaData()

        print("DB init")

        print(metadata.tables)


