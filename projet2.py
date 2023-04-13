import hashlib


password = input("Entrez votre mot de passe : ")


hash_object = hashlib.sha256(password.encode())


print("Le mot de passe crypté est :", hash_object.hexdigest())