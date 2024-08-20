import csv
import re
import sys
from tabulate import tabulate

todos = []
table = []


def main():
    while True:
        _ = False
        command = input("")
        if match := re.search(r"add todo:(.*)", command):
            todos.append({"TODO": match.group(1), "Completed": False})
            write_to_csv()
        elif match := re.search(r"remove todo:(.*)", command):
            try:
                todos.remove({"TODO": match.group(1), "Completed": False})
                write_to_csv()
            except ValueError:
                print("Todo does not exist")
        elif command == "exit":
            sys.exit()
        elif command == "show":
            try:
                with open("todo_list.csv") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        table.append(row)
                print(
                    tabulate(tabular_data=table, tablefmt="outline", headers="firstrow")
                )
            except FileNotFoundError:
                print("No todos created.")
        elif match := re.search(r"(.*) completed", command):
            for dict in todos:
                if match.group(1) == dict["TODO"]:
                    dict["Completed"] = True
                    _ = True
                    write_to_csv()
                    break
            if _ == False:
                print("Todo does not exist")
        elif command == "help":
            with open("README.md", "r") as file:
                print("\n" + file.read())
        else:
            print("Command not recognised")


def write_to_csv():
    with open("todo_list.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["TODO", "Completed"])
        writer.writeheader()
        writer.writerows(todos)


if __name__ == "__main__":
    main()
