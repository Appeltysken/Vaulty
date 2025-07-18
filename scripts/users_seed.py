def seed_users(users_collection):
    if users_collection.count_documents({"username": "mongo"}) == 0:
        users_collection.insert_one({
            "username": "mongo",
            "password": "Ivan",
            "first_name": "SpaceBiker",
            "last_name": "Johnson",
            "gender": "Мужской",
            "about": '''Сотрудник ООО "Black Mesa".\n
            Информация для себя:
            mongo-workAccount%2b876f616764461e2b6d6c8a58c4023b'''
        })

    if users_collection.count_documents({"username": "mongo-workAccount"}) == 0:
        users_collection.insert_one({
            "username": "mongo-workAccount",
            "password": "mongodb1",
            "first_name": "Gordon",
            "last_name": "Freeman",
            "gender": "Мужской",
            "about": "You got a flag!"
        })