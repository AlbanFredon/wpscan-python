import requests
import re
import xlwt

def get_site_info(url):
  # Envoie une requête GET à l'URL cible et récupère la page HTML
  html = requests.get(url).text

  # Utilise une expression régulière pour extraire le nom du site de la page HTML
  name_match = re.search(r"<title>(.*?)</title>", html)
  if name_match:
    name = name_match.group(1)
  else:
    name = None

  # Utilise une expression régulière pour extraire la description du site de la page HTML
  description_match = re.search(r"<meta name='description' content='(.*?)'>", html)
  if description_match:
    description = description_match.group(1)
  else:
    description = None

  # Utilise une expression régulière pour extraire les mots-clés du site de la page HTML
  keywords_match = re.search(r"<meta name='keywords' content='(.*?)'>", html)
  if keywords_match:
    keywords = keywords_match.group(1)
  else:
    keywords = None

  # Utilise une expression régulière pour vérifier si le site est optimisé pour les mobiles
  mobile_optimized_match = re.search(r"<meta name='viewport' content='.*?'>", html)
  if mobile_optimized_match:
    mobile_optimized = "Yes"
  else:    mobile_optimized = "No"

  # Utilise une expression régulière pour vérifier si le site utilise un fichier .htaccess
  htaccess_match = re.search(r"<a href='/.htaccess'>", html)
  if htaccess_match:
    htaccess = "Yes"
  else:
    htaccess = "No"

  # Utilise une expression régulière pour vérifier si le site utilise un fichier robots.txt
  robots_match = re.search(r"<a href='/robots.txt'>", html)
  if robots_match:
    robots = "Yes"
  else:
    robots = "No"

  # Utilise une expression régulière pour vérifier si le site utilise le plugin WordPress SEO
  wp_seo_match = re.search(r"<a href='/wp-content/plugins/wordpress-seo/'>", html)
  if wp_seo_match:
    wp_seo = "Yes"
  else:
    wp_seo = "No"

  return {
    "name": name,
    "description": description,
    "keywords": keywords,
    "mobile_optimized": mobile_optimized,
    ".htaccess": htaccess,
    "robots.txt": robots,
    "wp_seo": wp_seo
  }

def main():
  # Demander à l'utilisateur de saisir l'URL cible
  target_url = input("Enter the target URL: ")

  # Récupérer les informations du site à partir de l'URL cible
  site_info = get_site_info(target_url)

  # Créer un fichier Excel et ajouter une feuille de calcul
  workbook = xlwt.Workbook()
  worksheet = workbook.add_sheet("SEO")

  # Écrire les informations du site dans la feuille de calcul
  worksheet.write(0, 0, "Site name")
  worksheet.write(0, 1, site_info['name'])
  worksheet.write(1, 0, "Description")
  worksheet.write(1, 1, site_info['description'])
  worksheet.write(2, 0, "Keywords")
  worksheet.write(2, 1, site_info['keywords'])
  worksheet.write(3, 0, "Mobile optimized")
  worksheet.write(3, 1, site_info['mobile_optimized'])
  worksheet.write(4, 0, ".htaccess")
  worksheet.write(4, 1, site_info['.htaccess'])
  worksheet.write(5, 0, "robots.txt")
  worksheet.write(5, 1, site_info['robots.txt'])
  worksheet.write(6, 0, "WordPress SEO plugin")
  worksheet.write(6, 1, site_info['wp_seo'])

  # Enregistrer le fichier Excel
  workbook.save("resultat.xls")

if __name__ == "__main__":
  main()

