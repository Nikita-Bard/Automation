from sqlalchemy import create_engine, inspect, text

db_connection_path = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_path)

def test_db_connection():
    # Используем inspect для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()

    assert names[1] == 'app_users'


def test_select():
    # Создаем соединение
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM company"))
    # Получаем результат в виде словарей
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['id'] == 1
    assert row1['name'] == "QA Студия 'ТестировщикЪ'"

    # Закрываем соединение
    connection.close()


def test_select_1_row():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company WHERE id = :company_id")
    result = connection.execute(sql_statement, {"company_id": 1})
    rows = result.mappings().all()

    assert len(rows) == 1
    assert rows[0]["name"] == "QA Студия 'ТестировщикЪ'"

    connection.close()


def test_select_1_row_with_two_filters():
    connection = db.connect()
    sql_statement = text("select * from company where \"is_active\" = :is_active and id >= :id")
    my_params = {
        'id': 65,
        'is_active': True
    }

    rows = connection.execute(sql_statement, my_params).fetchall()

    assert len(rows) == 316

    connection.close()


def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("insert into company(\"name\") values (:new_name)")

    connection.execute(sql, {"new_name":"SkyPro"})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE company SET description = :descr WHERE id = :id")
    connection.execute(sql, {"descr": 'New descr', "id": 10})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM company WHERE id = :id")
    connection.execute(sql, {"id": 10})

    transaction.commit()
    connection.close()
