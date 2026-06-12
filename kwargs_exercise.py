
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# You can pass any number of key-value pairs
print_user_info(name="Alice", age=30, location="Bursa")