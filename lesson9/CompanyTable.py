from sqlalchemy import create_engine, text


class CompanyTable:

    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def get_companies(self):
        with self.engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM company"))
            return result.fetchall()
        
    def get_company_by_id(self, id):
        with self.engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM company where id = :select_id"), select_id = id)
            return result.fetchall()

    def get_active_companies(self):
        with self.engine.connect() as connection:
            return connection.execute(text("select * from company where \"is_active\" = true")).fetchall()

    def delete(self, id):
        sql = (text("delete from company where id = :id_to_delete"), id_to_delete = id)
        with self.engine.connect() as connection:
            connection.execute(sql, id_to_delete=id)

    # Данный метод не доделан (не работает)
    def create(self, name):
        transaction = connection.begin()
        sql = text("insert into company(\"name\") values (:new_name)")
        with self.engine.connect() as connection:
            connection.execute(sql, id_to_delete=id)
        
        transaction.commit()

    def get_max_id(self):
        with self.engine.connect() as connection:
            result = connection.execute(text("SELECT MAX(id) from company"))
            return result.fetchall()[0][0]
