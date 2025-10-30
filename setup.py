from setuptools import setup, find_packages

setup(
    name="mylibrary",                    # نام پکیج
    version="1.0.0",                     # نسخه
    author="Your Name",                  # نام شما
    description="A simple library management system",  # توضیح کوتاه
    packages=find_packages(),            # خودکار پوشه‌ها را پیدا می‌کند
    python_requires=">=3.8",             # نسخه حداقلی پایتون
)
