% Utilisation de données vecteur avec Python
% Clément Delgrange
% 03/2018


# Objectifs

* Connaître les différentes primitives géométriques
* Manipuler des objets géolocalisés et effectuer quelques opérations spatiales
* Visualiser les données géolocalisées, créer des cartes statiques et intéractives
* Ouvrir des fichiers géographiques de différents formats, dans différentes projections


* Effectuer des requêtes spatiales



# Introduction
La première partie du cours nous a permis d'établir un panorama des possibilités offertes par l'ensemble des techniques de programmation SIG.
Dans ce chapitre nous nous proposons d'aborder la programmation SIG en laissant le SIG bureautique traditionnel de côté.
Au lieu de cela, nous préférons nous concentrer sur la base de notre métier : la donnée géographique.
Nous commencerons ainsi par un bref rappel des modes de preprésentation de l'information géographique.
Puis nous verrons comment le langage de programmation Python nous permet de manipuler cette information géographique : manipulation de géométries vecteur, opérations spatiales, gestion des projections, représentation, etc.
Nous nous situerons donc ici plutôt dans la dernière des catégories de développements SIG que nous avons établit dans la première partie de ce cours, les applications autonomes, même si les techniques apprises ici pourrons nous être utiles pour développer, par exemple, des plugins pour un SIG.


## Le choix de Python comme langage de programmation
Dans cette partie, comme dans beaucoup de suivantes, nous utiliserons exclusivement le langage de programmation Python.
Aujourd'hui Python est probablement le langage de programmation le plus utilisé en géomatique.
L'écosystème Python s'est enrichi ses dernières années de nombreuses libraires à visées géospatiales.
C'est aussi le langage que les SIG ont choisi depuis plusieurs années pour exécuter des scripts de géotraitements (ArcGIS, QGIS, etc.).
Nous pouvons évoquer plusieurs raisons à cela:

* sa facilité d'utilisation et d'apprentissage pour des "non informaticiens";
* il est gratuit et open-source;
* il est assez facilement intégrable à d'autres langages (`C`, `C++`);
* de nombreuses libraires de calculs numériques existent (`numpy`, `scipy`, `pandas`, etc.);
* les libraires fondamentales de la géomatique (`PROJ.4`, `GDAL`, etc.) bénéficient de bindings Python.


# Représentation de l'information géographique

## Raster vs. vecteur
Deux façons de stocker les données géolocalisées : le mode vecteur et le mode raster.
Ces deux modes permettent de représenter la même information mais le font de manière différente.

En mode raster, le monde réel est représenté sous la forme de matrice où chaque case prend une valeur reflétant la valeur de l'information à représenter.
Des matrices multi-dimentionnelles (ie. à plusieurs bandes) sont fréquement utilisées pour représenter les phénomènes complèxes.

![Représentation vecteur](img/cours1/representation_vecteur.png)

Le mode vecteur représente l'information géographique sous forme de géométries.

![Représentation raster](img/cours1/representation_raster.png)

Les géométries peuvent être dotées d'un sémantique (ie. des attributs) et liées entre elles grace à des liens de topologies (ex : deux routes données sont connectées en un carrefour, ne sont pas connectées, se croisent à un pont mais ne sont pas connectées, etc.).

Si les rasters sont plus faciles à créer, l'analyse des données vecteur est plus aisée.
Dans la suite de cette partie nous nous focaliserons sur les données vecteur, tandis que la prochaine partie reviendra sur les données raster.


## Les primitives géométriques
Dans le mode vecteur le monde réel est donc représenté à l'aide de géométries. Dans sa norme *Simple Feature Access*[^1], l'Open Geospatial Consortium (OGC) définit huit primitives géométriques :

![Les primitives géométriques](img/cours1/primitives_geometriques.png)

[^1]: <http://www.opengeospatial.org/standards/sfa>

\begin{note}
"L'Open Geospatial Consortium, ou OGC, est un consortium international pour développer et promouvoir des standards ouverts, les spécifications OpenGIS, afin de garantir l'interopérabilité des contenus, des services et des échanges dans les domaines de la géomatique et de l'information géographique." (source Wikipedia)

Les principaux acteurs du marché (Esri, Oracle, etc.) ainsi que des instituts nationaux sont membre de l'OGC.
Aussi il est fort probable qu'une norme publiée par l'OGC soit aussitôt reprise par l'ensemble de la communauté géomatique.
\end{note}

Le modèle géométrique complet vous est donné ci-dessous.
Il nous intéresse pour comprendre comment sont structurées les données géographiques vecteur.
Vous constaterez, qu'en plus des huit primitives géométriques, d'autres classes abstraites sont introduites pour donner du sens au modèle et lier les primitives géométriques entre elles.

![Hiérarchie des classes géométriques](img/cours1/modele_geometrique.png)

Ce modèle nous intéresse également parce qu'il est repris dans la pluspart des outils que nous utiliserons.
C'est notament le cas de la librairie GEOS maintenue par la Fondation Open Source Geospatial (OSGeo) qui occupe une place centrale dans le monde de la géométique.
Basée sur la Java Topology Suite (JTS)[^2], cette librairies est notament utilisée dans PostGIS ou `shapely` que nous utiliserons dans la suite de ce chapitre.

[^2]: <https://github.com/locationtech/jts>

\begin{note}
"La Fondation Open Source Geospatial (OSGeo) est une organisation non gouvernementale fondée en 2006 pour soutenir et construire une offre de logiciels open source en géomatique." (source Wikipedia)

Alors que l'OGC édite des normes favorisant l'interopérabilité et les échanges de données, l'OSGeo soutient le développement d'outils open source mettant en oeuvre ces normes.
\end{note}

## validité des géométries
Au delà d'une simple hiérarchie entre les objets géométriques, la norme *Simple Feature Access* définie également des règles de validité pour chacune des géométries.

* polygones croisées
* spikes
* trou dont le contour touche le contour extérieur du polygon en plus d'un points
* etc.


## Les opérations spatiales

Enfin, la norme *Simple Feature Access* definit les opérations spatiales permises pour chaque type de géométrie.

* distance
* buffer
* rectangle englobant
* enveloppe convexe
* intersections / union / différence / différence symétrique


## La librairie `shapely`
Le module `shapely` a été créé par Sean Gillies pour permettre d'effectuer, avec un syntaxe pythonique, ce qu'il est possible de faire avec GEOS pour manipuler et analyser des géométries.
Aussi tout comme GEOS, `shapely` reprend une bonne part des principes exposés dans la norme *Simple Feature Access* de l'OGC.

`shapely` ne traite que des géométries et ne s'intéresse pas aux formats de données (lecture/écriture de fichiers) ou encore aux reprojections.
Il s'agit d'un parti pris de Sean Gillies qui a par ailleurs travaillé sur d'autres librairies pour ces taches : par exemple `fiona` pour la lecture/écriture de shapefiles ou `affine` pour effectuer des transformations affines.

Les notions d'*intérieur* (interior), de *frontière* (boundary) et d'*extérieur* (exterior) sont introduites par la librairie.
L'union de ces trois ensemble correspond à l'ensemble du plan.

* l'intérieur d'un point est égale au point lui même, sa frontière est nulle et l'extérieur correspond à tous les autres points;
* pour une ligne (linestring ou linearring), l'intérieur équivaut à l'ensemble des points sur sa longueur, la frontière aux deux extrémités et l'extérieur au reste des points;
* pour un polygone, l'intérieur est composé des points à l'intérieur de celui-ci, la frontière à une ou plusieurs lignes constituant le contour du polygone et l'extérieur au reste des points (y compris ceux à l'intérieur des trous).




## Exercices
1. Ecrire une fonction prennant une liste de point `shapely` et retournant deux éléments :
  * un boolean indiquant si le polygon `shapely` dont le contour extérieur est contitué de la suite de points est valide;
  * une chaîne de caractère détaillant le motif d'invalidité (ou une chaîne vide s'il est valide).
2. Ecrire une fonction qui prend en entrée deux linestrings et retourne leur intersection.
Le deux linestring et l'intersection seront ensuite dessinées dans un graphique matplotlib.
3. Ecrire un programme qui prend en entrée un fichier csv[^3] contenant les coordonnées d'une liste de points et une distance `dist_ref` et qui retourne un booléen indiquant si un point se situe à une distance supérieure à `disr_ref` de tous les autres points ou si chacun des points se situe à moins de `dist_ref` d'un autre point.

[^3]: Comma-separated Values (CSV) : format représentant des données tabulaires sous forme de de valeurs séparées par des virgules.

### Indices
1. L'essentiel de la documentation de `shapely` peut se retrouver sur une seule page web à l'adresse : <https://shapely.readthedocs.io/en/latest/manual.html>.
Essayer d'y effectuer une recherche avec un mot clé adéquat (en anglais ;-)).
2. Les instructions suivantes permettent d'afficher un point puis une ligne dans un graphique matplotlib :
```
import matplotlib.pyplot as plt

plt.plot(2, 3)  # dessine le point (2, 3)
plt.plot([0, 1, 2], [0, 1, 0])  # dessine la ligne [(0, 0), (1, 1), (2, 0)]
plt.show()
```
Vous pouvez consulter la documentation de la fonction `plot` pour avoir plus d'options d'affichage (couleurs, formes, etc.) : <https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot>.
3. Un ficheir csv est un fichier texte. Vous pouvez le lire comme un fichier texte classique ou utiliser une librairie adaptée.


# Les formats d'échange
Depuis une trentaine d'années, les SIG se sont implantés dans de nombreux domaines.
Diverses solutions commerciales se sont développées permettant à l'utilisateur un vaste choix parmi ces solutions.
Cette diversité de solutions implique une diversité de formats, chaque éditeur de logiciel étant à l'origine de sont propre format.

Lorsque les utilisateurs cherchent à faire communiquer leurs applications, ils sont confrontés au problème de l'*interopérabilité* : la capacité des système à s'échanger et se partager des données.

Dans ce contexte nous distinguerons les formats dits *ouverts* (pensons aux shapefiles d'Esri) de ceux dits *fermés* (les géodatabases d'Esri).
Par ouverts/fermés nous entendons que les spécifications de ces formats sont respectivement publiques ou pas.
Naturellement des formats ouverts permettent l'interopérabilité des données tandis que les formats fermés la limite.

La problématique sera identique pour le développeur : un format ouvert sera manipulable au travers de différentes librairies.
Les formats fermés ne le seront généralement que via les librairies de l'éditeur de SIG propriétaire du format.

Aujourd'hui les données ont de plus en plus besoin d'être échangées entre divers acteurs.
On comprendra alors aisément que l'importance des formats ouverts dans ce contexte.

Pour les données vecteur, l'OGC a mis en avant le *well-known text* (WKT) dans la norme *Simple Feature Access* pour décrire de manière textuelle tous les types de géométrie.
D'autres formats permettant d'inclure des informations sémantiques sur les géométries ont également été mis en oeuvre par la communauté : le GeoJSON, le GML, etc.
Parmi eux le **GeoJSON** semble aujourd'hui être plébiscité par la communauté SIG pour manipuler les données vecteur.


## Le GeoJSON
Basé sur le format JSON (JavaScript Open Notation), le GeoJSON permet de représenter toutes les primitives géométriques définies par l'OGC.
Il est lisible par un humain et manipulable par la plupart des libraires géospatiales ainsi que par les principaux SIG du marché.

\begin{note}
Le format JSON (JavaScript Open Notation) est un format textuel qui permet de représenter une information structurée.
Il est fréquemment utilisé comme format d'échange dans le monde du web en raison de sa facilité de mise en oeuvre.
Un document JSON ne comporte que deux types d'éléments : des couples clé/valeur et des listes ordonnées de valeurs.
Les types permis pour les valeurs sont : nombres, chaînes de caractères, booléens, null, liste ordonnées ou objet JSON.
\end{note}

La structure du GeoJSON est celle d'un dictionnaire en Python. Les différents types de géométries sont listés dans le tableau suivant :

\begin{tabular}{|c|l|}
	\hline
	Point &
	\begin{lstlisting}
{ "type": "Point",
    "coordinates": [30, 10]
}
	\end{lstlisting} \\
	\hline
	Polyligne &
	\begin{lstlisting}
{ "type": "LineString",
    "coordinates": [
        [30, 10], [10, 30], [40, 40]
    ]
}
	\end{lstlisting} \\
	\hline
	\begin{tabular}{c}
		Polygone \\
		(y compris avec trous)
	\end{tabular} &
	\begin{lstlisting}
{ "type": "Polygon",
    "coordinates": [
        [[35, 10], [45, 45], [15, 40], [10, 20], [35, 10]],
        [[20, 30], [35, 35], [30, 20], [20, 30]]
    ]
}
	\end{lstlisting} \\
	\hline
	Multi-point &
	\begin{lstlisting}
{ "type": "MultiPoint",
    "coordinates": [
        [10, 40], [40, 30], [20, 20], [30, 10]
    ]
}
	\end{lstlisting} \\
	\hline
	Multi-polyligne &
	\begin{lstlisting}
{ "type": "MultiLineString",
    "coordinates": [
        [[10, 10], [20, 20], [10, 40]],
        [[40, 40], [30, 30], [40, 20], [30, 10]]
    ]
}
	\end{lstlisting} \\
	\hline
	Multi-polygone &
	\begin{lstlisting}
{ "type": "MultiPolygon",
    "coordinates": [
        [
            [[40, 40], [20, 45], [45, 30], [40, 40]]
        ],
        [
            [[10, 30], [10, 10], [40, 5], [40, 30], [20, 35]],
            [[30, 20], [20, 15], [20, 25], [30, 20]]
        ]
    ]
}
	\end{lstlisting} \\
	\hline
\end{tabular}

Une entité géométrique `Feature` possède une balise `geometry` et une balise `properties` pour la sémantique de la géométrie:
```
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [100.0, 0.0],
        [101.0, 0.0],
        [101.0, 1.0],
        [100.0, 1.0],
        [100.0, 0.0]
      ]
    ]
  },
  "properties": {
    "nom": "Paris",
    "population": 2000000
  }
}
```

Le type `FeatureCollection` permet de regrouper un ensemble de géométries de types différents au sein d'une même entité géométrique :

```
{ "type": "FeatureCollection",
    "features": [
      { "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [...]
        },
        "properties": {
          "prop0": "value0"
        }
      },
      { "type": "Feature",
        "geometry": {
          "type": "LineString",
          "coordinates": [...]
        },
        "properties": {
          "prop0": "value0",
          "prop1": 0.0
        }
      },
      { "type": "Feature",
         "geometry": {
           "type": "Polygon",
           "coordinates": [...]
         },
         "properties": {
           "prop0": "value0",
           "prop1": 123456
           }
         }
       ]
     }
```


## Le protocole `__geo_interface__`
Sean Gillies a proposé un protocole pour représenter les informations géographiques vecteur dans Python en se basant sur le GeoJSON : <https://gist.github.com/sgillies/2217756>
Ce protocole est adopté petit à petit par la communauté Python géomatique et les les principales libraires l'implémentent maintenant (`shapely`, `arcpy`, `geojson`, `PySAL`, etc.).

Par exemple avec `shapely`, les instructions suivantes retournent la représentation GeoJSON d'un multipoint :
```
>>> from shapely.geometry import MultiPoint
>>> mpt = MultiPoint([[0, 0], [1, 0], [0, 1], [1, 1]])
>>> mpt.__geo_interface__
{'coordinates': ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (1.0, 1.0)),
 'type': 'MultiPoint'}
```


## Exercices
1. Le format gpx est un format d'échange de données GPS. Il est notament utilisé par les montres GPS de sport.
En utilisant la librairie `gpxpy` (<https://github.com/tkrajina/gpxpy>) pour lire un fichier au format gpx, créer une fonction prenant en entrée un fichier gpx et retournant une géométrie shapely représentant la trace contenue dans le fichier.
Ecrire ensuite une seconde fonction permettant d'écrire un fichier GeoJSON à partir de la géométrie shapely précédente.



# Les projections
PROJ.4 et pyproj (simple et efficace, mais uniquement des points)

osr : plus compliqué à prendre en main mais plus abouti aussi


## Exercices
1. calculer l'aire dans une projection donnée d'un polygone en wgs84




# Lecture de shapefiles
`fiona`



# Exercice
enveloppe autour de points



# Créer des cartes




# Bibliographie

* <https://www.packtpub.com/application-development/python-geospatial-development-second-edition>
