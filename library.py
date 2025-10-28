class Library:
    def __init__(self):
        self.books = []  # هر کتاب به صورت دیکشنری ذخیره می‌شود: {"title": ..., "author": ...}

    def add_book(self, title, author):
        """اضافه کردن کتاب به فهرست"""
        self.books.append({"title": title, "author": author})
        print(f"✅ کتاب '{title}' از {author} اضافه شد.")

    def remove_book(self, title):
        """حذف کتاب با عنوان خاص"""
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f"❌ کتاب '{title}' حذف شد.")
                return
        print(f"⚠️ کتابی با عنوان '{title}' پیدا نشد.")

    def search_book(self, title):
        """جستجوی کتاب با عنوان خاص"""
        for book in self.books:
            if book["title"].lower() == title.lower():
                print(f"📖 پیدا شد: {book['title']} از {book['author']}")
                return book
        print(f"❌ کتاب '{title}' یافت نشد.")
        return None

    def show_books(self):
        """نمایش همه‌ی کتاب‌ها"""
        if not self.books:
            print("📚 هیچ کتابی در کتابخانه موجود نیست.")
        else:
            print("📚 فهرست کتاب‌ها:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book['title']} — {book['author']}")
