from user import user
from tools import command_select, clear

if __name__ == "__main__":
    clear()
    print("speedrun.com statistics fetcher, program written by Niamek")
    user = user("niamek")
    commands = []
    while True:
        clear()
        for attribute in user.__dict__.values():
            if not isinstance(attribute, str):
                commands.append(attribute)

                print(attribute)
        selection = command_select(commands)
        if selection == "end":
            break
        else:
            selection()
        break