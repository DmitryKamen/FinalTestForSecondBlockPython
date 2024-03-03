
from Model import create_note, delete_note, edit_note, list_notes

def run():
    while True:
        print("\nМеню:")
        print("Create. Создать заметку")
        print("Show. Показать список заметок")
        print("Edit. Редактировать заметку")
        print("Delete. Удалить заметку")
        print("Exit. Выйти")

        action = input("Выберите действие: ")

        if action == "Create":
            create_note()
        elif action == "Show":
            list_notes()
        elif action == "Edit":
            note_id = int(input("Введите id заметки для редактирования: "))
            edit_note(note_id)
        elif action == "Delete":
            note_id = int(input("Введите id заметки для удаления: "))
            delete_note(note_id)
        elif action == "Exit":
            break
        else:
            print("Некорректный набор команды. Попробуйте еще раз.")
