% Visualiser des données géographiques
% Clément Delgrange
% 03/2018


# Objectifs

* Apprendre à manipuler des raster avec Python



# L'information géographique raster
Un raster est une image (photographie, plan, modèle numérique de terrain, etc.) géoréférencée.
L'information représentée dans le raster est stockée sous forme de matrices où chacune des cellules est associée à une valeur chiffrée représentant la valeur de l'information.

Le traitement et l'analyse des rasters est souvent pus complexe que celle des vecteurs.

GDAL = librairie fondamentale de gestion des rasters (écrite en C). Supportée par l'OSGeo.
Binding Python existant : `osgeo`

Avec PROJ.4, pour les reprojections, GEOS, pour la manipulation de géométries vecteur, GDAL est la troisième librairie fondamentale de la géomatique.

Exemple : ouvrir un raster et obtenir ses métadonnées
```
from osgeo import gdal
gtif = gdal.Open( "INPUT.tif" )
print gtif.GetMetadata()
```

Effectuer des statistiques sur l'ensemble des bandes du raster :
```
from osgeo import gdal
import sys

src_ds = gdal.Open( "INPUT.tif" )
if src_ds is None:
    print 'Unable to open INPUT.tif'
    sys.exit(1)

print "[ RASTER BAND COUNT ]: ", src_ds.RasterCount
for band in range( src_ds.RasterCount ):
    band += 1
    print "[ GETTING BAND ]: ", band
    srcband = src_ds.GetRasterBand(band)
    if srcband is None:
        continue

    stats = srcband.GetStatistics( True, True )
    if stats is None:
        continue

    print "[ STATS ] =  Minimum=%.3f, Maximum=%.3f, Mean=%.3f, StdDev=%.3f" % ( \
                stats[0], stats[1], stats[2], stats[3] )
```


## Exercices



# Exercice final
Consignes :

* Les données (...) représentent des polygones;
* Le raster (....) est un MNT;
* Pour chacun des polygones, il s’agit de calculer l'altitude moyenne du MNT sous son emprise.
* Le résultat est inscrit dans la données d'entrée.
