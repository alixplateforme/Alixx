MIN_LENGTH = 8
REQUIRE_DIGIT = True
REQUIRE_UPPER = True
REQUIRE_LOWER = True
while True:
    # Demander à l'utilisateur de choisir un mot de passe
    password = input("Choisissez un mot de passe : ")

    # Vérifier les exigences de sécurité
    errors = []
    if len(password) < MIN_LENGTH:
        errors.append("Le mot de passe doit contenir au moins {} caractères.".format(MIN_LENGTH))
    if REQUIRE_DIGIT and not any(char.isdigit() for char in password):
        errors.append("Le mot de passe doit contenir au moins un chiffre.")
    if REQUIRE_UPPER and not any(char.isupper() for char in password):
        errors.append("Le mot de passe doit contenir au moins une lettre majuscule.")
    if REQUIRE_LOWER and not any(char.islower() for char in password):
        errors.append("Le mot de passe doit contenir au moins une lettre minuscule.")

    # Si le mot de passe est valide, afficher un message de confirmation et quitter le programme
    if not errors:
        print("Le mot de passe est sécurisé.")
        break

    # Sinon, afficher un message d'erreur et demander à l'utilisateur de choisir un nouveau mot de passe
    else:
        print("Le mot de passe ne répond pas aux exigences de sécurité suivantes :")
        for error in errors:
            print("-", error)
        print("Veuillez choisir un nouveau mot de passe.")