# main.py
import database

print("Starting Feature Store...")

database.connect_db()

# Add some features
database.add_feature("user_1", "age", 25, version="1")
database.add_feature("user_1", "age", 26, version="2")
database.add_feature("user_1", "income", 50000, version="1")

# Retrieve features
print("Latest 'age' for user_1:", database.get_feature("user_1", "age"))
print("Version 1 'age' for user_1:", database.get_feature("user_1", "age", version="1"))
print("Income for user_1:", database.get_feature("user_1", "income"))
