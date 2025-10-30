from mylibrary.library import Library

def menu():
    lib = Library()

    while True:
        print("\n===== سیستم مدیریت کتابخانه =====")
        print("1. اضافه کردن کتاب")
        print("2. حذف کتاب")
        print("3. جستجوی کتاب")
        print("4. نمایش همه کتاب‌ها")
        print("5. خروج")

        choice = input("انتخاب کنید (1-5): ")

        if choice == "1":
            title = input("عنوان کتاب: ")
            author = input("نویسنده: ")
            lib.add_book(title, author)
        elif choice == "2":
            title = input("عنوان کتابی که می‌خواهید حذف کنید: ")
            lib.remove_book(title)
        elif choice == "3":
            title = input("عنوان کتابی که می‌خواهید جستجو کنید: ")
            lib.search_book(title)
        elif choice == "4":
            lib.show_books()
        elif choice == "5":
            print("👋 خداحافظ!")
            break
        else:
            print("❗ انتخاب نامعتبر است، لطفاً دوباره تلاش کنید.")

# بررسی می‌کند که فایل مستقیماً اجرا شده یا ایمپورت شده
if __name__ == "__main__":
    menu()
