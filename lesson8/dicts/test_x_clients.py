from CompanyApi import CompanyApi


api = CompanyApi("https://x-clients-be.onrender.com/")


def test_get_companies():
    body = api.get_comany_list()
    assert len(body) > 0


def test_get_active_companies():
    # Получаем список всех компаний
    full_list = api.get_comany_list()

    # Получаем список активных компаний
    filtered_list = api.get_comany_list(params_to_add={'active': 'true'})

    # Проверяем, что список всех компаний > списка активных компаний
    assert len(full_list) > len(filtered_list)


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

    # проверить, что +1
    assert len_after - len_before == 1
    # проверить название и описание последней компании
    # проверить, что id новой компании рвен ответу из шага два
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr
    assert body[-1]["id"] == new_id


def test_get_one_company():
    name = "Apple"
    descr = "Company"
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_company = api.get_company(new_id)

    assert new_company[id] == new_id
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["isActive"] == True


def test_edit():
    name = "Apple"
    descr = "Company"
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_name = "Google"
    new_descr = "__upd__"

    edited = api.edit(new_id, new_name, new_descr)
    assert edited[id] == new_id
    assert edited["name"] == new_name
    assert edited["description"] == new_descr
    assert edited["isActive"] == True


def test_delete():
    name = "Apple delete"
    result = api.create_company(name)
    new_id = result["id"]

    edited = api.delete(new_id)
    assert edited[id] == new_id
    assert edited["name"] == name
    assert edited["description"] == ''
    assert edited["isActive"] == True

    body = api.get_comany_list()
    assert body[-1]["id"] != new_id


def test_deactivate():
    # создать новую компанию
    name = "Apple deactivated"
    result = api.create_company(name)
    new_id = result["id"]

    body = api.set_active_state(new_id, False)
    assert body["isActive"] == False


def test_deactivate_and_activate_back():
    name = "Apple deactivated"
    result = api.create_company(name)
    new_id = result["id"]

    api.set_active_state(new_id, False)

    body = api.set_active_state(new_id, True)
    assert body["isActive"] == True
