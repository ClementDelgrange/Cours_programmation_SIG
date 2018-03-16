% Programmation SIG
% Clément Delgrange
% 03/2018


# Programmation sous SIG?
Les SIG s'adressent à des communautés d'utilisateurs très diverses oeuvrant dans des domaines tout aussi variés : aménagement, urbanisme, travaux publics, assurance, réseaux, énergie, télécommunication, santé, production de données, etc. Bien que présentant des caractéristiques communes, les outils utilisés doivent dans le détail apporter des solutions personnalisées à chacune d'entre elles. Cela est rendu possible par le développement logiciel. Une formation aux SIG doit donc nécessairement comporter un volet consacré à la programmation de tels systèmes.

L'évolution récente du monde de l'information géographique vers la mise en ligne de données et de services (sur le web ou bien au sein de réseaux d'entreprises) a renforcé l'importance des développements. Aujourd'hui, on consomme de plus en plus l'information géographique à travers des applications web ou mobiles qui sont chacune la réponse à un besoin particulier. Ces applications et les services qu'elles consomment ce sont les développeurs SIG qui les conçoivent.
Face à ces enjeux, les éditeurs de logiciels et la communauté open source proposent des gammes de solutions plus ou moins complètes et spécifiques à une activité, du simple visualiseur à l'application sur mesure en passant par le SIG bureautique au sens historique du terme.

Après avoir rappelé les notions de base de l'architecture d'un SIG et présenté les différents types de développement possibles, ce cours s'attardera sur

les produits de l'éditeur proposant la gamme la plus complète du marché à ce jour : Esri avec la suite ArcGIS. La plate-forme ArcGIS couvre en effet tous les types d'usage : bureautique, réseau, web, mobile. Les différents produits sont par ailleurs "ouverts" aux développements : le développeur dispose d'interfaces de programmation pour personnaliser, étendre les applications qu'Esri a conçues, mais aussi pour en créer de nouvelles.


# Pourquoi Python?
Aujourd'hui Python est probablement le langage de programmation le plus utilisé en géomatique.
L'écosystème Python s'est enrichi ses dernières années de nombreuses libraires à visées géospatiales.
C'est aussi le langage que les SIG ont choisi depuis plusieurs années pour permettant d'exécuter des scripts de géotraitement (ArcGIS, QGIS, etc.).
Nous pouvons évoquer plusieurs raisons à cela:

* facilité d'utilisation et d'apprentissage pour des "non informaticiens"
* gratuit et open-source
* facilement intégrable à d'autres langages
* libraires de calculs numériques (`numpy`, `scipy`, `pandas`, etc.)
* libraires fondamentales de al géomatique (`PROJ.4`, `GDAL`, etc.) bénéficient de bindings Python




# Bibliographie

* <https://www.packtpub.com/application-development/python-geospatial-development-second-edition>
