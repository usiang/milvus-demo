from src.demo import init_db, load_data

def test_init_db():
    init_db()
    assert True


def test_load_data():
    load_data()
    assert True 