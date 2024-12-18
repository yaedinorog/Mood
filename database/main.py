from models import create_tables
from test_data import add_test_data, get_data_user

if __name__ == "__main__":
    create_tables()
    add_test_data()
    get_data_user()