from pytest import fixture


@fixture(autouse=True)
def db_access(db):
    pass
