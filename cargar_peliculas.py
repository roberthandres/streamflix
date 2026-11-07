
from datetime import date
from peliculas.models import Pelicula

peliculas = [
    ("Interestelar", "Ciencia ficción", 2014, 169, "Un grupo de astronautas viaja por el espacio buscando un nuevo hogar para la humanidad.", "8.7"),
    ("El origen", "Ciencia ficción", 2010, 148, "Un ladrón especializado en robar secretos entra en los sueños de otras personas.", "8.8"),
    ("Titanic", "Romance", 1997, 195, "Dos jóvenes de diferentes clases sociales se enamoran a bordo de un famoso barco.", "7.9"),
    ("Batman: El caballero de la noche", "Acción", 2008, 152, "Batman enfrenta a un peligroso criminal que quiere sumergir Ciudad Gótica en el caos.", "9.0"),
    ("Avatar", "Ciencia ficción", 2009, 162, "Un exmarine llega a un planeta habitado por una especie de seres azules.", "7.9"),
    ("Matrix", "Ciencia ficción", 1999, 136, "Un programador descubre que la realidad que conoce es una simulación.", "8.7"),
    ("Jurassic Park", "Aventura", 1993, 127, "Un parque temático intenta mostrar dinosaurios creados mediante ingeniería genética.", "8.2"),
    ("Gladiador", "Acción", 2000, 155, "Un general romano busca vengarse después de perderlo todo.", "8.5"),
    ("Forrest Gump", "Drama", 1994, 142, "Un hombre con una vida extraordinaria presencia importantes acontecimientos históricos.", "8.8"),
    ("Sueños de libertad", "Drama", 1994, 142, "Un banquero condenado a prisión construye una amistad que cambiará su vida.", "9.3"),
    ("El padrino", "Crimen", 1972, 175, "La historia de una poderosa familia dedicada al crimen organizado.", "9.2"),
    ("Pulp Fiction", "Crimen", 1994, 154, "Varias historias de criminales se entrelazan en Los Ángeles.", "8.9"),
    ("El club de la pelea", "Drama", 1999, 139, "Un hombre insatisfecho con su vida conoce a un vendedor de jabón muy particular.", "8.8"),
    ("El señor de los anillos: La comunidad del anillo", "Fantasía", 2001, 178, "Un joven hobbit recibe la misión de destruir un poderoso anillo.", "8.8"),
    ("Harry Potter y la piedra filosofal", "Fantasía", 2001, 152, "Un niño descubre que tiene poderes mágicos y comienza a estudiar en Hogwarts.", "7.6"),
    ("Avengers: Endgame", "Acción", 2019, 181, "Los superhéroes sobrevivientes intentan revertir una catástrofe universal.", "8.4"),
    ("Iron Man", "Acción", 2008, 126, "Un empresario construye una armadura tecnológica después de vivir una experiencia traumática.", "7.9"),
    ("Spider-Man: Sin camino a casa", "Acción", 2021, 148, "Un joven superhéroe enfrenta las consecuencias de revelar su identidad.", "8.2"),
    ("Coco", "Animación", 2017, 105, "Un niño apasionado por la música viaja al mundo de los muertos.", "8.4"),
    ("Toy Story", "Animación", 1995, 81, "Los juguetes de un niño cobran vida cuando los humanos no están presentes.", "8.3"),
    ("Buscando a Nemo", "Animación", 2003, 100, "Un pez emprende una aventura por el océano para encontrar a su hijo.", "8.2"),
    ("Up: Una aventura de altura", "Animación", 2009, 96, "Un anciano emprende un viaje extraordinario con miles de globos.", "8.3"),
    ("El rey león", "Animación", 1994, 88, "Un joven león debe recuperar su lugar como rey de la sabana.", "8.5"),
    ("Frozen", "Animación", 2013, 102, "Dos hermanas enfrentan un reino cubierto por un invierno mágico.", "7.4"),
    ("Shrek", "Animación", 2001, 90, "Un ogro emprende una misión para rescatar a una princesa.", "7.9"),
    ("Tiburón", "Suspenso", 1975, 124, "Un enorme tiburón aterroriza a los habitantes de una localidad costera.", "8.1"),
    ("Volver al futuro", "Ciencia ficción", 1985, 116, "Un adolescente viaja accidentalmente al pasado en un automóvil especial.", "8.5"),
    ("Terminator 2: El juicio final", "Acción", 1991, 137, "Un cyborg debe proteger a un joven perseguido por otro robot.", "8.6"),
    ("Alien: El octavo pasajero", "Terror", 1979, 117, "La tripulación de una nave espacial descubre una criatura mortal.", "8.5"),
    ("Rocky", "Drama", 1976, 120, "Un boxeador desconocido recibe la oportunidad de enfrentarse a un campeón.", "8.1"),
    ("Whiplash", "Drama", 2014, 107, "Un joven baterista enfrenta a un exigente profesor de música.", "8.5"),
    ("La La Land", "Romance", 2016, 128, "Una actriz y un músico persiguen sus sueños en Los Ángeles.", "8.0"),
    ("Parásitos", "Suspenso", 2019, 132, "Una familia con pocos recursos comienza a trabajar para una familia adinerada.", "8.5"),
    ("Joker", "Drama", 2019, 122, "Un hombre marginado atraviesa una transformación que impacta a Ciudad Gótica.", "8.3"),
    ("Oppenheimer", "Drama", 2023, 180, "Un científico lidera el desarrollo de la primera bomba atómica.", "8.3"),
    ("Barbie", "Comedia", 2023, 114, "Una muñeca abandona su mundo perfecto y descubre la realidad humana.", "6.8"),
    ("Dune", "Ciencia ficción", 2021, 155, "Un joven llega a un planeta desértico que contiene un recurso muy valioso.", "8.0"),
    ("Mad Max: Furia en el camino", "Acción", 2015, 120, "En un futuro desértico, un hombre ayuda a un grupo a escapar de un tirano.", "8.1"),
    ("La red social", "Drama", 2010, 120, "La historia de la creación de una de las redes sociales más conocidas.", "7.8"),
    ("El lobo de Wall Street", "Comedia", 2013, 180, "Un corredor de bolsa alcanza la riqueza mediante negocios fraudulentos.", "8.2"),
    ("El gran hotel Budapest", "Comedia", 2014, 99, "Un conserje de hotel se ve involucrado en una aventura llena de misterio.", "8.1"),
    ("El show de Truman", "Drama", 1998, 103, "Un hombre descubre que toda su vida podría ser un programa de televisión.", "8.2"),
    ("El sexto sentido", "Suspenso", 1999, 107, "Un psicólogo infantil atiende a un niño que asegura ver personas muertas.", "8.2"),
    ("El silencio de los inocentes", "Suspenso", 1991, 118, "Una agente del FBI busca ayuda de un peligroso asesino para resolver un caso.", "8.6"),
    ("Los infiltrados", "Crimen", 2006, 151, "Un policía y un criminal infiltrado intentan descubrirse mutuamente.", "8.5"),
    ("Piratas del Caribe: La maldición del Perla Negra", "Aventura", 2003, 143, "Un pirata busca recuperar su barco y romper una antigua maldición.", "8.1"),
    ("Los juegos del hambre", "Ciencia ficción", 2012, 142, "Una joven participa en un peligroso torneo televisado para sobrevivir.", "7.2"),
    ("Misión imposible: Fallout", "Acción", 2018, 147, "Un agente secreto intenta impedir una catástrofe internacional.", "7.7"),
    ("Ratatouille", "Animación", 2007, 111, "Una rata con talento culinario sueña con convertirse en chef en París.", "8.1"),
    ("Intensamente", "Animación", 2015, 95, "Las emociones de una niña intentan adaptarse a un gran cambio en su vida.", "8.1"),
    ("El viaje de Chihiro", "Animación", 2001, 125, "Una niña entra en un mundo mágico habitado por espíritus.", "8.6"),
]

creadas = 0
existentes = 0

for titulo, genero, anio, duracion, descripcion, calificacion in peliculas:
    pelicula, creada = Pelicula.objects.get_or_create(
        titulo=titulo,
        defaults={
            'descripcion': descripcion,
            'genero': genero,
            'tipo': 'pelicula',
            'fecha_lanzamiento': date(anio, 1, 1),
            'duracion': duracion,
            'calificacion': calificacion,
            'destacado': False,
        }
    )

    if creada:
        creadas += 1
    else:
        existentes += 1

print("CARGA TERMINADA")
print("Películas nuevas:", creadas)
print("Películas que ya existían:", existentes)
print("Total de películas:", Pelicula.objects.filter(tipo='pelicula').count())
