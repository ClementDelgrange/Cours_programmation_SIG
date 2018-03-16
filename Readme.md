# Cours de programmation SIG

Cours d'introduction à la programmation sour SIG.


## Pré-requis

Avoir déjà un pratiqué un minimum les SIG semble être indispensable avant d'aborder ce cours.
Quelques notions en programmation sont également requises.
La préférence se portera sur le langage de programmation Python, qui sera le langage le plus souvent utilisé lors des différentes séquences du cours.


## Ce que ce cours contient

L'ensemble du cours est constitué de différentes leçons abordant chacune des points particuliers de la programmation SIG. Les objectifs de chacune des séquences sont énoncés en début de celles-ci.

Notre premier jalon sera de redéfinir ce que nous entendons par SIG et d'établir l'intérêt et les différentes familles de programmation SIG. Puis nous apprendrons à manipuler avec le langage de programmation Python les différentes primitives géométriques, à lire le contenu de fichiers géographiques, à effectuer des opérations sur des données géolocalisées. Nous apprendrons également à réaliser des plugins pour les principaux SIG du marché (ArcGIS et QGIS), permettant ainsi d'étendre les fonctionnalités de ces derniers.


## Regénérer les slides et pdf par vous même
Les supports de cours sont rédigés en markdown. La génération des documents finaux (cours et TP en pdf, présentations en HTML) fait appel à l'utilitaire [pandoc](https://pandoc.org/). Pour les présentations la libraire [reveal.js](https://revealjs.com/#/) doit avoir été téléchargée pour bénéficier de la mise en page correcte.

Les lignes de commande permettant de générer les documents à partir des sources sont listées ci-dessous :

* Le support de cours général :
```
pandoc -s -N --listings --template=template/template.latex -o Cours_BDD.pdf Cours_BDD.md
```

* Les présentations :
```
pandoc -s -t html5 --template=template/ign-ensg-revealjs.html --section-divs -o Presentation_BDD.html Presentation_BDD.md

pandoc -s -t html5 --template=template/ign-ensg-revealjs.html --section-divs -o Presentation_SQL.html Presentation_SQL.md
```

* Les exercices :
```
pandoc -s -N --listings --template=template/template_tp.latex -o Exercices/Exercices_modelisation.pdf Exercices/Exercices_modelisation.md
```
