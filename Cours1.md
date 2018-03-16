% Une introduction à la géomatique via Python
% Clément Delgrange
% 03/2018

# Objectifs

* Connaître les différentes primitives géométriques
* Ouvrir des fichiers géographiques de différents formats, dans différentes projections
* Manipuler des objets géolocalisés et effectuer quelques opérations spatiales
* Effectuer des requêtes spatiales
* Visualiser les données géolocalisées, créer des cartes statiques et intéractives





# Les primitives géométriques
* Point
* MultiPoint
* LineString
* LineaRing
* MultiLineString
* Polygon
* MultiPolygon
* Collection

Validité des géométries  :

* polygones croisées
* spikes
* trou dont le contour touche le contour extérieur du polygon en plus d'un points
* etc.[^1]

[^1]: voir les spécifications de l'OGC pour le détail complet de la validité des géométriques : <>

Parler de la lib GEOS / parenthèse sur l'OSGEO


# GeoJSON
Les éditeurs de SIG proposent quasiment tous des formats propriétaires.
Ces formats peuvent être *ouverts* (pensons aux shapefiles d'Esri) ou *fermés* (les géodatabases d'Esri).
Par ouverts/fermés nous entendons que les spécifications de ces formats sont respectivement publiques ou pas.
Pour l'utilisateur des données dans un format ouvert signifient des données qui pourront être ouvertes dans différents logiciels.

Il en sera de même pour le développeur : un format ouvert sera manipulable au travers de différentes librairies.
Les formats fermés ne le seront généralement que via les librairies de l'éditeur de SIG propriétaire du format.

Aujourd'hui les données ont de plus en plus besoin d'être échangées entre divers acteurs.
On comprendra alors aisément que l'importance des formats ouverts dans ce contexte.
Parmi eux le **GeoJSON** semble aujourd'hui être plébiscité par la communauté SIG pour manipuler les données vecteur.
Basé sur le format JSON (JavaScript Open Notation), le GeoJSON permet de représenter toutes les primitives géométriques définies par l'OGC.
Il est lisible par un humain et manipulable par la plupart des libraires géospatiales.

\begin{note}
Le format JSON (JavaScript Open Notation) est un format textuel qui permet de représenter une information structurée.
Il est fréquemment utilisé comme format d'échange dans le monde du web en raison de sa facilité de mise en oeuvre.
Un document JSON ne comporte que deux types d'éléments : des couples clé/valeur et des listes ordonnées de valeurs.
Les types permis pour les valeurs sont : nombres, chaînes de caractères, booléens, null, liste ordonnées ou objet JSON.
\end{note}

KML, GML, WKT : d'autres formats présentant les mêmes caractéristiques que le GeoJSON.


## `__geo_interface__`
Sean Gillies a proposé un protocole pour représenter les informations géographiques vecteur dans Python en se basant sur le GeoJSON.
Ce protocole est adopté petit à petit par la communauté et les les principales libraires l'implémentent maintenant (`shapely`, `arcpy`, `geojson`, `PySAL`, etc.).



https://gist.github.com/sgillies/2217756

# Opérations spatiales

* distance
* buffer
* rectangle englobant
* enveloppe convexe





# Annexes

## Principales libraires Python


* GDAL –> Fundamental package for processing vector and raster data formats (many modules below depend on this). Used for raster processing.
* Geopandas –> Working with geospatial data in Python made easier, combines the capabilities of pandas and shapely.
* Shapely –> Python package for manipulation and analysis of planar geometric objects (based on widely deployed GEOS).
* Fiona –> Reading and writing spatial data (alternative for geopandas).
* Pyproj –> Performs cartographic transformations and geodetic computations (based on PROJ.4).
* Pysal –> Library of spatial analysis functions written in Python.
* Geopy –> Geocoding library: coordinates to address <-> address to coordinates.
* GeoViews –> Interactive Maps for the web.
* Geoplot –> High-level geospatial data visualization library for Python.
* Dash –> Dash is a Python framework for building analytical web applications.
* OSMnx –> Python for street networks. Retrieve, construct, analyze, and visualize street networks from OpenStreetMap
* Networkx –> Network analysis and routing in Python (e.g. Dijkstra and A* -algorithms), see this post.
* Cartopy –> Make drawing maps for data analysis and visualisation as easy as possible.
* Scipy.spatial –> Spatial algorithms and data structures.
* Rtree –> Spatial indexing for Python for quick spatial lookups.
* Rasterio –> Clean and fast and geospatial raster I/O for Python.
* RSGISLib –> Remote Sensing and GIS Software Library for Python.
