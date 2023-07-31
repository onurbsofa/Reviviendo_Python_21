""" En este desafío, debes encontrar al gatito más famoso con base en su número de seguidores.

Recibirás una lista de diccionarios que incluirán las siguientes propiedades:

"name": nombre del gatito.
"followers": una lista de números, donde cada uno representa los seguidores de cada red social.
Tu tarea es devolver una lista con los nombres de los gatos que tienen solo el mayor número de seguidores. Si hay dos o más gatos con el mismo número máximo de seguidores, deberás incluirlos en la lista resultante, manteniendo el orden en el que aparecen en la lista de entrada. """

cats_social = [
  {
    "name": "Luna",
    "followers": [100,200, 300]
  },
  {
    "name": "Bob",
    "followers": [100,200, 300]
  },
  {
    "name": "Tom",
    "followers": [45, 76, 34]
  },
    {
    "name": "Linda",
    "followers": [100, 34, 200]
    },
    {
    "name": "joan",
    "followers": [100,200, 300]
  },
]


"""
priemra solucion con ayuda de copilot que funciona mal en los test
def find_famous_cat(cats):
  cats_return = []
  max_followers = 0
  for cat in cats:
    for followers in cat["followers"]:
        if followers > max_followers:
            max_followers = followers
            cats_return = [cat["name"]]
        elif followers == max_followers:
            cats_return.append(cat["name"])
  return cats_return
  pass """

# solucion de platzi
def find_famous_cat(cats):
  record = 0
  winners = []
  for i in cats:
    count = 0
    
    for j in i['followers']:
      count+=j
    
    if winners==[]:
      winners.append(i['name'])
      record = count    
    elif count > record:
      winners.pop()          
      winners.append(i['name'])
      record = count
    elif count == record:
      winners.append(i['name'])
    
  return winners
  pass

print(find_famous_cat(cats_social))
