import hashlib
def hash_password(password):
    hasher = hashlib.md5()
    # hash password
    hasher.update(password.encode('utf-8'))

    # get hashed password
    hashed_password = hasher.hexdigest()
    return hashed_password

#password = input("Enter your password:")
#hashed = hash(password)
#print(hashed)