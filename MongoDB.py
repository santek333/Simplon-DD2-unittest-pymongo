class Film:

  def __init__(self, id):
    self.id = id

  def get_nb_films(db):
    # retourne le nombre de films présents dans la base
    films = db.films.find()

    return len(list(films))

    
  def get_actors(self,db):
    # retourne la liste des acteurs du film

    actors = list(db.films.find_one({"imdb_id":self.id}).get('actors'))

    return actors

class Actor:

  def __init__(self, name):
    self.name = name
    self.films = []

  def add_film(self, film):
    self.films.append(film)

  def load(self, db):
    # ajoute l'acteur dans la base de données
    pass

  def get_nb_actors(db):
    # retourne le nombre d'acteurs présents dans la base
    tmp = []
    actors=[]
    for elem in db.films.find():
      tmp.append(elem.get('actors'))
    tmp1 = []
    for elem in tmp:
      for el in elem:
        tmp1.append(el)
    actors = set(tmp1)
    actors_final = []
    for elem in actors:
      actors_final.append(elem.strip())

    return len(actors_final)
    

