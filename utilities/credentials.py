from utilities.MongoDB import *
import bcrypt

collection_name='users'

def check_credentials(username, password):
    db = MongoDB.get_db()
    collection = db[collection_name]
    query = {"username": username}
    user = collection.find_one(query)

    if user:
        hashed_password = user['password']
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return True
        else:
            return False
    else:
        return False

'''
if 'thread_id' in user:
    print("User has a thread_id:", user['thread_id'])
else:
    print("User does not have a thread_id.")
'''
def find_user_by_username(username):
    db = MongoDB.get_db()
    collection = db[collection_name]
    query = {"username": username}

    try:
        user = collection.find_one(query)
        if user:
            return user
        else:
            print("No user found with the specified username.")
            return None
    except Exception as e:
        print(f"Error finding user: {e}")
        return None

def get_users():
    db = MongoDB.get_db()
    collection = db[collection_name]
    count = collection.count_documents({})
    if count>20:
        count=20
    documents = collection.find({}, {'username': 1, '_id': 0}).limit(count)
    usernames = [doc['username'] for doc in documents]
    return usernames
        

def insert_user(username, password):
    db = MongoDB.get_db()
    collection = db[collection_name]
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    user_document = {
        "username": username,
        "password": hashed_password,
    }

    try:
        result = collection.insert_one(user_document)
        return True, result.inserted_id  # Return True and the ID of the inserted document
    except Exception as e:
        print(f"Error inserting user: {e}")
        return False, None

'''
username = 'user_1234'
additional_fields = {
    "thread_id": "thread_1234"
}
update_user(username, additional_fields)
'''
def update_user(username, additional_fields):
    db = MongoDB.get_db() 
    collection = db[collection_name]
    query = {"username": username}
    update = {"$set": additional_fields}
    try:
        result = collection.update_one(query, update)
        if result.matched_count > 0:
            if result.modified_count > 0:
                return True
            else:
                print("The document was not updated (it may already have the additional fields).")
                return False
        else:
            return False
    except Exception as e:
        print(f"Error updating user: {e}")

def delete_myuser(username):
    db = MongoDB.get_db()
    collection = db[collection_name]
    query = {"username": username}

    try:
        result = collection.delete_one(query)
        if result.deleted_count > 0:
            return True
        else:
            print("No user found with the specified username.")
            return False
    except Exception as e:
        print(f"Error deleting user: {e}")
        return False