import todo_list


def test_write_to_csv():
    todo_list.todos = [{"TODO": "play sports", "Completed": False}]
    todo_list.write_to_csv()
    with open("todo_list.csv", "r") as file:
        assert file.read() == "TODO,Completed\nplay sports,False\n"
    todo_list.todos = [{"TODO": "play sports", "Completed": True}]
    todo_list.write_to_csv()
    with open("todo_list.csv", "r") as file:
        assert file.read() == "TODO,Completed\nplay sports,True\n"
    todo_list.todos = [
        {"TODO": "play sports", "Completed": True},
        {"TODO": "practice programming", "Completed": False},
    ]
    todo_list.write_to_csv()
    with open("todo_list.csv", "r") as file:
        assert (
            file.read()
            == "TODO,Completed\nplay sports,True\npractice programming,False\n"
        )
    todo_list.todos = []
    todo_list.write_to_csv()
    with open("todo_list.csv", "r") as file:
        assert file.read() == "TODO,Completed\n"
