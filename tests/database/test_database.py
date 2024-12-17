import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


@pytest.mark.database
def test_tables_list():
    db = Database()
    tables = db.get_tables()

    assert len(tables) == 3
    assert ('customers',) in tables
    assert ('products',) in tables
    assert ('orders',) in tables


@pytest.mark.database
def test_user_insert():
    db = Database()
    db.insert_user(3, 'Natali', 'Mykoly Lysenka str, 3', 'Kyiv', '01030', 'Ukraine')
    person = db.select_user_by_id(3)

    assert person[0] == 3
    assert person[4] == '01030'


@pytest.mark.database
def test_user_name_update():
    db = Database()
    db.insert_user(4, 'Jana', '5th Ave, 754', 'New York', '10019', 'USA')
    db.update_user_name_by_id(4, 'Sara')
    person = db.select_user_by_id(4)
    
    assert person[1] == 'Sara'


@pytest.mark.database
def test_user_delete():
    db = Database()
    db.insert_user(99, 'Abc', 'Def, 11', 'Krk', '9999', '?')
    db.delete_user_by_id(99)
    person = db.select_user_by_id(99)
    
    assert person == None


@pytest.mark.database
def test_check_user_postCode_3127():
    db = Database()
    user = db.get_user_addresses_by_postalCode(3127)
    print(user)
   
    assert user[0][2] == "3127"


@pytest.mark.database
def test_check_user_not_found():
    db = Database()
    user = db.select_user_by_id(0)
    
    assert user == None