import os
import subprocess
import hashlib
import pickle
import sqlite3

# 1. Hardcoded Secret / API Token
AWS_SECRET_KEY = "AKIA1234567890EXAMPLEKEY"
ADMIN_PASSWORD = "SuperSecretPassword123!"

# 2. Command Injection / Shell Execution
user_input = input("Enter command: ")
os.system(user_input)
subprocess.call(user_input, shell=True)
subprocess.Popen(f"ls -la {user_input}", shell=True)

# 3. Code Injection / Insecure Deserialization
eval(user_input)
pickle.loads(user_input.encode())

# 4. Weak Cryptography (MD5)
hashed_password = hashlib.md5(ADMIN_PASSWORD.encode()).hexdigest()

# 5. SQL Injection via string formatting
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE username = '%s'" % user_input)
cursor.execute(f"SELECT * FROM users WHERE id = {user_input}")
