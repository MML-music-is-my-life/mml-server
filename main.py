from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import MetaData
from sqlalchemy import create_engine
import datetime

now = datetime.datetime.now()

today_date = now.strftime('%Y-%m-%d')

print(today_date)

engine = create_engine(
    'mysql+mysqldb://<username>:<password>@<host>:<port>/<dbname>')

conn = engine.connect()

ranks = Table(
    'rank', MetaData(),
    Column('id', Integer, primary_key=True),
    Column('ranking', Integer),
    Column('title', String),
    Column('album_art', String),
    Column('album_name', String),
    Column('artist', String),
    Column('date', String),
    Column('bf_day', Integer),
    Column('bf_week', Integer),
    Column('bf_month', Integer),
    Column('platform', String)
)

MetaData().create_all(engine)


def insert_today_rank():
    # api 서버 호출 및 결과 저장

    conn.execute(ranks.insert(), [
        {'name': 'Jin', 'age': 28},
        {'name': 'Suga', 'age': 27}
    ])


def select_ranks(v_platform):
    return ranks.select().where(date=today_date, platform=v_platform)
