import requests
import re

def get_theme_info(url):
  # Envoie une requête GET à l'URL cible et récupère la page HTML
  html = requests.get(url).text

  # Utilise une expression régulière pour extraire le nom du thème de la page HTML
  name_match = re.search(r"<h1 class='theme-name'>(.*?)</h1>", html)
  if name_match:
    name = name_match.group(1)
  else:
    name = None

  # Utilise une expression régulière pour extraire la version du thème de la page HTML
  version_match = re.search(r"<span class='theme-version'>(.*?)</span>", html)
  if version_match:
    version = version_match.group(1)
  else:
    version = None

  # Envoie une requête GET au fichier readme.txt du thème
  readme_url = url + "/readme.txt"
  readme = requests.get(readme_url).text

  # Utilise une expression régulière pour extraire la description du thème du fichier readme.txt
  description_match = re.search(r"== Description ==(.*?)==", readme, re.DOTALL)
  if description_match:
    description = description_match.group(1).strip()
  else:
    description = None

  return {
    "name": name,
    "version": version,
    "description": description
  }

def main():
  # Demander à l'utilisateur de saisir l'URL cible
  target_url = input("Enter the target URL: ")

  # Récupérer les informations du thème à partir de l'URL cible
  theme_info = get_theme_info(target_url)
  print("Name:", theme_info['name'])
  print("Version:", theme_info['version'])
  print("Description:", theme_info['description'])

if __name__ == "__main__":
  main()
