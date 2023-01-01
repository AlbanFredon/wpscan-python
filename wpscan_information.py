import requests
import re

def get_site_info(url):
  # Envoie une requête GET à l'URL cible et récupère la page HTML
  html = requests.get(url).text

  # Utilise une expression régulière pour extraire le nom du site de la page HTML
  name_match = re.search(r"<title>(.*?)</title>", html)
  if name_match:
    name = name_match.group(1)
  else:
    name = None

  # Envoie une requête GET à l'URL wp-content pour récupérer la liste des fichiers dans ce répertoire
  content_url = url + "/wp-content"
  content_html = requests.get(content_url).text

  # Utilise une expression régulière pour extraire la liste des fichiers du répertoire wp-content
  file_list_match = re.findall(r"<a href='(.*?)'>", content_html)
  if file_list_match:
    file_list = file_list_match
  else:
    file_list = None

  # Envoie une requête GET à l'URL wp-admin pour vérifier si l'accès est autorisé
  admin_url = url + "/wp-admin"
  admin_html = requests.get(admin_url).text

  # Utilise une expression régulière pour vérifier si l'accès à l'URL wp-admin est autorisé
  access_match = re.search(r"<p>Access denied</p>", admin_html)
  if access_match:
    access = "denied"
  else:
    access = "allowed"

  return {
    "name": name,
    "wp_content_files": file_list,
    "wp_admin_access": access
  }

def main():
  # Demander à l'utilisateur de saisir l'URL cible
  target_url = input("Enter the target URL: ")

  # Récupérer les informations du site à partir de l'URL cible
  site_info = get_site_info(target_url)
  print("Site name:", site_info['name'])
  print("Files in wp-content:", site_info['wp_content_files'])
  print("Access to wp-admin:", site_info['wp_admin_access'])

if __name__ == "__main__":
  main()
