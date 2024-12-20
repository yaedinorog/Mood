from models import create_tables
from test_data import add_test_data, get_data_user, Login, Registration, GetUserChats, AddNewChat, AddMood, GetAllMood

if __name__ == "__main__":
    create_tables()
    add_test_data()
    # get_data_user()
    # try:
    #     Login("@sfsdf")
    # except(TypeError):
    #     print(f"Error: {TypeError} user is not found")
    # Login("@Bebricks")
    # try:
    #     Registration("@asdasd", "+79175435435")
    # except(TypeError):
    #     print(f"Error: {TypeError} user already registered")
    # AddNewChat(1, 3)
    # GetUserChats(1)
    # AddMood("Счастливый")
    # GetAllMood()