import requests

# 1. URL de la page web que tu veux télécharger
url = 'https://fr.wikipedia.org/wiki/Wikipédia:Accueil_principal'

# 2. Télécharger la page avec Requests
response = requests.get(url)

# 3. Vérifier si la requête a réussi (code 200 = succès)
if response.status_code == 200:
    # 4. Afficher le contenu HTML de la page
    print(response.text)
else:
    print(f"Erreur : {response.status_code}")
