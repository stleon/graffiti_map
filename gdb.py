from pony.orm import *
from datetime import datetime

db = Database("sqlite", "graffity_net.sqlite", create_db=True)

class Graffity(db.Entity):
    id = PrimaryKey(int, auto=True)
    image = Required(str, unique=True)
    lat = Required(float)
    lon = Required(float)
    date_created = Required(datetime)
    name = Required(str, 140)
    text = Optional(LongStr)
    active = Required(bool, default=1)
    checked = Required(bool, default=1)

#sql_debug(True)
db.generate_mapping(create_tables=True)

@db_session
def populate_database():
    graffity = Graffity(image='123.png', lat=55.739701, lon=37.664635, date_created=datetime.now(), 
        name='На Таганке', text='Только не рисуйте это на моем доме',)
    graffity1 = Graffity(image='456.png', lat=55.739701, lon=37.664635, date_created=datetime.now(), 
        name='Воу-воу', text='Такое я увидел сегодня утром...',)
    graffity2 = Graffity(image='789.png', lat=55.807881, lon=37.580831, date_created=datetime.now(), 
        name='Без комментариев', text='Такое я увидел сегодня утром...',)

@db_session
def test_queries():
    result = select(g.name for g in Graffity)[:]
    print(result)



if __name__ == '__main__':
    with db_session:
        if Graffity.select().first() is None:
            populate_database()
    test_queries()

