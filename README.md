1. Installation de pandoc : <http://pandoc.org/installing.html>

2. commandes à exécuter depuis le répertoire `Analyse_informatique_UML` pour générer les différents supports de cours :
    * Pour générer les slides :

    pandoc -s -t html5 --template=template\ign-ensg-revealjs.html --section-divs -o Presentation_prog_SIG.html Presentation_prog_SIG.md

    * Pour générer les pdf de cours :

    pandoc -s -N --listings --template=template\template.latex -o Analyse_informatique.pdf Analyse_informatique.md 
	
    * Pour générer les pdf des TD :

    pandoc -s -N --listings --template=template\template_tp.latex -o TD_xxx.pdf TD_xxx.md 

