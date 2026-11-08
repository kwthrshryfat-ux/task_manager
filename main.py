from models import Taskmanager
from storage import load_tasks, save_tasks

def ask_index(manager):
    try:
        return int(input("شماره: ")) - 1
    except ValueError:
        print("لطفا عدد وارد کن.")
        return None


def main():
    manager = Taskmanager(load_tasks())

    while True:
        cmd = input("\n1) افزودن  2) نمایش  3) ویرایش  4) حذف  5) انجام شد  0) خروج: ")

        try:
            if cmd == "1":
                manager.add(input("عنوان: "))
            elif cmd == "2":
                manager.show()
            elif cmd == "3":
                i = ask_index(manager)
                if i is not None:
                    manager.edit(i, input("عنوان جدید: "))
            elif cmd == "4":
                i = ask_index(manager)
                if i is not None:
                    manager.remove(i)
            elif cmd =="5":
                i = ask_index(manager)
                if i is not None:
                    manager.complete(i)
            elif cmd == "0":
                save_tasks(manager.tasks)
                print("ذخیره شد. خداحافظ!")
                break
            else:
                print("گزینه نامعتبر.")
        except IndexError as e:
            print("خطا:", e)


if __name__ == "__main__":
    main()
