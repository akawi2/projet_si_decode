import itertools
import string

def xor_decrypt(data, key):
    """Déchiffre des données avec un XOR en utilisant une clé donnée."""
    key_length = len(key)
    return bytes(data[i] ^ ord(key[i % key_length]) for i in range(len(data)))

def is_readable(text):
    """Vérifie si le texte semble lisible (caractères ASCII imprimables)."""
    return all(32 <= char < 127 or char in (10, 13) for char in text)

def generate_keys(start_key):
    """Génère toutes les clés possibles à partir d'une clé donnée jusqu'à 'zzzzzz'."""
    alphabet = string.ascii_lowercase
    key_length = len(start_key)

    start_indices = [alphabet.index(c) for c in start_key]

    for indices in itertools.product(range(26), repeat=key_length):
        if indices >= tuple(start_indices):
            yield ''.join(alphabet[i] for i in indices)

def brute_force_xor(file_path, start_key, output_file="resultats.txt"):
    """Brute force XOR en stockant les résultats au fur et à mesure."""
    with open(file_path, "rb") as f:
        encrypted_data = f.read()

    print(f"🔍 Démarrage du brute force à partir de : {start_key}")

    with open(output_file, "w", encoding="utf-8") as result_file:
        result_file.write("Clé testée | Première phrase déchiffrée\n")
        result_file.write("=" * 50 + "\n")

        for key in generate_keys(start_key):
            decrypted = xor_decrypt(encrypted_data, key)
            preview = decrypted[:15].decode(errors='ignore')  # 15 premiers caractères

            # Stocker la clé et l'aperçu dans le fichier
            result_file.write(f"{key} | {preview}\n")

            print(f"🔑 Clé : {key} → Aperçu : {preview}")

            if is_readable(decrypted):
                print(f"\n✅ Clé trouvée : {key}\n🔓 Texte déchiffré :\n{decrypted.decode(errors='ignore')}\n")
                return key

    print("❌ Aucune clé valide trouvée.")
    return None

# Utilisation
file_path = "./PE.txt"  # Remplacez par votre fichier chiffré
start_key = "daaaaa"  # Clé de départ
brute_force_xor(file_path, start_key)
