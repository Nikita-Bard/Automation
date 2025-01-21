from lesson9.CompApi import CompanyApi
from lesson9.CompanyTable import CompanyTable

api = CompanyApi("https://x-clients-be.onrender.com")
# Здесь должны быть подключение к БД
db = CompanyTable("")


def test_get_companies():
    # шаг 1 - получить список компаний через api
    api_result = api.get_comany_list()

    # шаг 2 - получить список компаний из БД
    db_result = db.get_companies()

    # шаг 3 - проверить, что списки равны
    assert len(api_result) == len(db_result)


def test_get_active_companies():
    # Получаем список активных компаний
    filtered_list = api.get_comany_list(params_to_add={'active': 'true'})
    db_list = db.get_active_companies()
    # Проверяем, что список всех компаний > списка активных компаний
    assert len(filtered_list) == len(db_list)


def test_add_new():
    # получить количество компаний
    body = api.get_comany_list()
    len_before = len(body)
    # создать новую компанию
    name = "Autotest",
    descr = "Descr"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # получить количество компаний
    body = api.get_comany_list()
    len_after = len(body)

    # удаляем компании через БД
    db.delete(new_id)

    # проверить, что +1
    assert len_after - len_before == 1
    for company in body:
        if company["id"] == new_id:
            # проверить название и описание последней компании
            # проверить, что id новой компании рвен ответу из шага два
            assert company["name"] == name
            assert company["description"] == descr
            assert company["id"] == new_id


def test_get_one_company():
    name = "Apple"
    db.create(name)
    max_id = db.get_max_id()
    new_company = api.get_company(max_id)
    db.delete(max_id)

    assert new_company[id] == max_id
    assert new_company["name"] == name
    # Необходимо дописать данный метод
    # assert new_company["description"] == descr
    assert new_company["isActive"] == True


def test_edit():
    name = "Apple"
    db.create(name)
    max_id = db.get_max_id()

    new_name = "Google"
    new_descr = "__upd__"
    edited = api.edit(max_id, new_name, new_descr)

    db.delete(max_id)

    assert edited[id] == max_id
    assert edited["name"] == new_name
    assert edited["description"] == new_descr
    assert edited["isActive"] == True


def test_delete():
    name = "Apple"
    db.create(name)
    max_id = db.get_max_id()

    deleted = api.delete(max_id)
    assert deleted[id] == max_id
    assert deleted["name"] == name
    # Необходимо дописать данный метод
    # assert deleted["description"] == ''
    assert deleted["isActive"] == True

    rows = db.get_company_by_id(max_id)
    assert len(rows) == 0


def test_deactivate():
    # создать новую компанию
    name = "Apple"
    db.create(name)
    max_id = db.get_max_id()
    db.delete(max_id)

    body = api.set_active_state(max_id, False)

    db.delete(max_id)
    assert body["isActive"] == False


def test_deactivate_and_activate_back():
    name = "Apple"
    db.create(name)
    max_id = db.get_max_id()

    api.set_active_state(max_id, False)
    body = api.set_active_state(max_id, True)

    db.delete(max_id)
    assert body["isActive"] == True
