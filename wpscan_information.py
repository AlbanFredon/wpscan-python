import requests
import re

def get_wp_version(url):
  # Envoie une requête GET à l'URL cible et récupère la page HTML
  html = requests.get(url).text

  # Utilise une expression régulière pour extraire la version de WordPress de la page HTML
  match = re.search(r"<meta name='generator' content='WordPress (.*?)' />", html)
  if match:
    return match.group(1)
  return None

def get_plugin_list(url):
  # Envoie une requête GET à l'URL cible avec le paramètre "api"
  # Cela permet de récupérer la liste des plugins sous forme de données JSON
  api_url = url + "/wp-json/wp/v2/plugins"
  data = requests.get(api_url).json()

  # Crée une liste des noms de plugins à partir des données JSON
  plugin_list = []
  for plugin in data:
    plugin_list.append(plugin['name'])
  return plugin_list

def main():
  # Demander à l'utilisateur de saisir l'URL cible
  target_url = input("Enter the target URL: ")

  # Afficher la version de WordPress cible
  version = get_wp_version(target_url)
  if version:
    print("WordPress version:", version)
  else:
    print("Unable to determine WordPress version.")

  # Afficher la liste des plugins installés sur le site cible
  plugin_list = get_plugin_list(target_url)
  print("Installed plugins:", ", ".join(plugin_list))

if __name__ == "__main__":
  main()
