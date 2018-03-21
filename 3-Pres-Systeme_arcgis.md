% Le système ArcGIS / ArcGIS pour le développeur
% M1 Géomatique
% 03/2018


# Le système ArcGIS #

##  ##

![Le système ArcGIS](img/cours/arcgis.png)


## Solutions bureautiques ##

| Le SIG bureautique historique | Le viewer gratuit | Les applications métier |
|:-----------------------------:|:-----------------:|:-----------------------:|
| *ArcGIS for Desktop*          | *ArcGIS Explorer* | *ArcGIS Engine*         |
| ![ArcGIS for Desktop](img/cours/arcgis_desktop_pro.jpg) | ![ArcGIS Explorer](img/cours/arcgis_explorer.jpg) | ![ArcGIS Engine](img/cours/arcgis_engine.jpg) |


## ArcGIS for Desktop ##

* 5 applications

| ![Suite ArcMap](img/cours/arcgis_for_desktop.png) | ![ArcGIS Pro](img/cours/arcgis_pro.jpg) |
|:-------------------------------------------------:|:---------------------------------------:|
| *Suite ArcMap*                                    | *ArcGIS Pro*                            |


## ArcGIS for Desktop ##

* Applications disponibles en 3 niveaux de fonctionnalités
	* Basic (*ArcView*) => faire des cartes, géotraitements simples
	* Standard (*ArcEditor*) => outils d'édition, géodatabases avancées
	* Advanced (*ArcInfo*) => géotraitements avancés (ex : topologie)
* +des extensions
	* *Spatial Analyst*, *Data Interoperability*...


## Un peu de vocabulaire ##

* Du côté "données"

![](img/cours/constituants_workspace.png)


## Un peu de vocabulaire ##

* Du côté **document ArcMap** (*map document* / mxd)

![](img/cours/constituants_mxd.png)


## Les géodatabases ##

| Caractéristique			| Géodatabase personnelle	| Géodatabase fichier		| Géodatabase entreprise	|
|:--------------------------|:--------------------------|:--------------------------|:--------------------------|
| Format					| Fichier Access			| Système de fichiers		| Système de fichiers		|
| Taille max				| 2 Go						| Quasi illimitée			| Illimitée					|
| Utilisateurs en lecture	| < 10						| < 50						| Multi-utilisateur			|
| Utilisateurs en écriture	| 1 seul					| 1 par jeu de données		| Multi-utilisateur 		|

> Nous n'utiliserons quasiment jamais de géodatabase personnelle.


## ArcGIS Entreprise ##

* ArcGIS Entreprise == ArcGIS for Server
* Serveur SIG complet
	* *héberger*
	* *partager*
	* *créer des applications web SIG*


## ArcGIS Entreprise (ArcGIS for Server) ##

* 3 niveaux de fonctionnalités
	* Basic
	* Standard
	* Advanced
* 2 niveaux de capacité
	* Workgroup (10 utilisateurs, 10GB, 4 coeurs)
	* Enterprise (*"illimité"*)


## Les services ArcGIS ##

<table style="font-size: 12pt">
<colgroup>
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;"><strong>Type de service</strong></th>
<th style="text-align: left;"><strong>Fonctionnalités disponibles</strong></th>
<th style="text-align: left;"><strong>Ressource SIG</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">Carte</td>
<td style="text-align: left;">Cartographie</br>Accès aux données</br>Analyse de réseau</br>WCS, WFS, WMS, KML</td>
<td style="text-align: left;">Document ArcMap (.mxd)</br>Définition de service de carte (.msd)</td>
</tr>
<tr class="even">
<td style="text-align: left;">Géocodage</td>
<td style="text-align: left;">Géocodage</td>
<td style="text-align: left;">Localisateur d'adresses (.loc, .mxs)</td>
</tr>
<tr class="odd">
<td style="text-align: left;">Géodonnées</td>
<td style="text-align: left;">Géodonnées</br>Accès aux données</td>
<td style="text-align: left;">Géodatabase fichier</br>Fichier de connexion à une base de données (.sde)</td>
</tr>
<tr class="even">
<td style="text-align: left;">Géotraitement</td>
<td style="text-align: left;">Géotraitement</td>
<td style="text-align: left;">Boite à outils</td>
</tr>
<tr class="odd">
<td style="text-align: left;">Globe</td>
<td style="text-align: left;">Globe</td>
<td style="text-align: left;">Document ArcGlobe (.3dd)</td>
</tr>
<tr class="even">
<td style="text-align: left;">Imagerie</td>
<td style="text-align: left;">Traitement d'image</br>WCS, WMS</td>
<td style="text-align: left;">Jeu de données raster</br>Mosaïque ou fichier de couche faisant référence à un jeu de données raster ou mosaïque</td>
</tr>
</tbody>
</table>


## Utiliser des ressources ArcGIS ##

* Services exposés via 4 protocoles
	* REST
		* `http://server_name:6080/arcgis/rest/services/service_name`
	* SOAP
	* KML
	* OGC


## Options de déploiement ##

* Client léger
	* Application web *clé en main*
	* Application mobile
	* ...
* Client lourd compatibles
	* ArcMap, ArcGIS Pro
* Développement d'un client riche avec les APIs web


## Architecture ArcGIS for Server ##

![Architecture ArcGIS for Server](img/cours/AcrGIS_Server_architecture.png)


## Portal for ArcGIS ##

* Intermédiaire entre le serveur et les clients
	* Administrer
	* Partager
	* Créer des cartes
	* Créer des applications


## Portal for ArcGIS ##

![Architecture Portal for ArcGIS](img/cours/portal_for_arcgis-2.png)


## ArcGIS Online ##

* <http://www.arcgis.com>
* Un SIG dans le cloud
	* gestion collaborative de cartes et services géographiques
	* serveur SIG sur le web


## ArcGIS Online ##

![Carte ArcGIS Online](img/cours/arcgis_online.png)


## Les solutions mobiles ##

* Gammes d'outils du professionnel au grand public
	* ArcPad
	* ArcGIS Mobile
	* ArcGIS for Smartphones
	* Collector for ArcGIS


## Les générateurs d'applications ##

![AppStudio for ArcGIS](img/cours/AppStudio_for_ArcGIS-2.png)

![Web AppBuilder](img/cours/web_appbuilder_process.png)


## Des applications clés en main ##

*


## Coût des licences ##

* ArcMap :
    * Advanced : 7000€
    * Standard : 5000€
    * Basic : 1000€
* ArcGIS Entreprise (Workgroup) :
	* Basic : 1000€
* ArcGIS Entreprise (Entreprise) :
	* Advanced : 20000-30000€
* ArcGIS Online :
	* 10 jetons = 1€
	* Feature Service Storage : 10MB = 2,4 jetons
	* Tile and data storage : 1GB = 1,2 jetons
* plus la maintenance...



# ArcGIS pour le développeur #

## Familles d'APIs et SDKs ##

* 4 grandes familles
	* APIs Python
	* ArcGIS Runtime  et API ArcObjects
	* APIs web
	* APIs mobiles


## APIs Python ##

* ArcGIS API for Python
	* faire des carte, de l'analyse spatiale
* Arcpy
	* automatiser des géotraitements
	* étendre les applications bureautiques


## L'API ArcObjects ##

* API fondamentale d'ArcGIS
	* ArcObjects = composants de base d'ArcGIS (*composants COM*)
	* Création d'extensions ou d'applications autonomes
	* Consomable via différents SDKs

![Diagramme ArcObjects](img/cours/api_arcobjects.png)


## ArcGIS Runtime ##

* Remplaçant des ArcObjects
* Indépendant des composants COM
* Noyau d'exécution et différentes API/SDK pour développer

![Le noyau Runtime](img/cours/arcgis_runtime-2.png)


## ArcGIS Runtime ##

![Possibilités d'applications natives ArcGIS Runtime](img/cours/arcgis_runtime-1.png)


## APIs web ##

* Générateurs d'applications (Web AppBuilder)
* Templates d'applications (Flex et Silverlight)
* 3 API web
	* ArcGIS for Javascript
	* ArcGIS for Flex
	* ArcGIS for Silverlight
* *Toutes basées sur l'API REST d'ArcGIS for Server*


## APIs web ##

![Web AppBuilder](img/cours/web_appbuilder.png)


## APIs web ##

![API Javascript](img/cours/api_javascript.png)
