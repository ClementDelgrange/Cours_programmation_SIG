#-*- coding: utf-8 -*-

import arcpy
import pythonaddins
import os


FL_ALL_STATIONS = "Layer_stations"
FC_ALL_STATIONS = "Stations"


class ButtonClass1(object):
    """Implementation for addinmetro_addin.button1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        """Calcul de l'itineraire entre deux stations"""
        gdb = "D:\\ProgSIG\\data\\TD_itinearaire.gdb"
        arcpy.env.workspace = gdb
        mxd = arcpy.mapping.MapDocument("CURRENT")

        # On teste l'existance d'une classe d'entités Stations
        if not arcpy.Exists(FC_ALL_STATIONS):
            pythonaddins.MessageBox(
                u"Les stations doivent exister dans le document !",
                u"Calcul d'itinéraires")
            return -1

        # On compte le nombre d'entités sélectionnés dans la couche
        fl_stations = get_layer(mxd, FL_ALL_STATIONS)
        nb = int(arcpy.GetCount_management(fl_stations)[0])
        if nb != 2:
            # Nombre de stations sélectionnées différent de 2
            pythonaddins.MessageBox(
                u"Nombre de stations sélectionnées : {}\nSélectionnez 2 stations !".format(nb),
                u"Calcul d'itinéraires")
            return -1


        pythonaddins.MessageBox(
            u"Nombre de stations sélectionnées : 2.\nCalcul de l'itinéraire...",
            u"Calcul d'itinéraires")

        # C'est tout bon : on peu calculer l'itinéraire !
        calcule_itineraire(mxd, fl_stations)


class ButtonClass3(object):
    """Implementation for addinmetro_addin.button3 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        """Construction du reseau (lignes et stations) et ajout au document"""
        rep_data = "D:\\ProgSIG\\data"
        gdb = os.path.join(rep_data + "TD_itinearaire.gdb")
        arcpy.env.workspace = gdb
        layer_stations = "Layer_stations_ligne_"
        fc_stations = "Stations_ligne_"
        fc_line = "Ligne_"

        # Construction des stations et lignes pour chacun des fichiers texte du répertoire
        txt_files = [f for f in os.listdir(rep_data) if f.endswith(".txt")]
        for txt_file in txt_files:
            num_line = txt_file[1:-4]  # on supprime la première lettre et les 4 dernières
            arcpy.MakeXYEventLayer_management(txt_file, "x", "y", layer_stations + num_line, "PROJCS['RGF_1993_Lambert_93',GEOGCS['GCS_RGF_1993',DATUM['D_RGF_1993',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',700000.0],PARAMETER['False_Northing',6600000.0],PARAMETER['Central_Meridian',3.0],PARAMETER['Standard_Parallel_1',44.0],PARAMETER['Standard_Parallel_2',49.0],PARAMETER['Latitude_Of_Origin',46.5],UNIT['Meter',1.0]];-35597500 -23641900 10000;-100000 10000;-100000 10000;0,001;0,001;0,001;IsHighPrecision", "")
            arcpy.FeatureClassToFeatureClass_conversion(layer_stations + num_line, gdb, fc_stations_name + num_line, "", "x \"x\" true true false 8 Double 0 0 ,First,#,stations_layer,x,-1,-1;y \"y\" true true false 8 Double 0 0 ,First,#,stations_layer,y,-1,-1;nom \"nom\" true true false 8000 Text 0 0 ,First,#,stations_layer,nom,-1,-1", "")
            arcpy.PointsToLine_management(fc_stations_name + num_line, fc_line + num_line, "", "", "NO_CLOSE")

        # Fusion de toutes les stations dans une unique classe d'entités
        fcs_stations = []
        fcs = arcpy.ListFeatureClasses()
        for fc in fcs:
            if fc_stations in fc:
                fcs_stations.append(fc)

        arcpy.Merge_management(fcs_stations, FC_ALL_STATIONS)
        arcpy.DeleteIdentical_management(FC_ALL_STATIONS, "Shape")
        
        # On l'ajoute au document
        add_layer(mxd, FL_ALL_STATIONS)


class ButtonClass2(object):
    """Implementation for addinmetro_addin.button2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.MessageBox("Aide de l'extension Metro...", "Aide")


class ExtensionClass(object):
    """Implementation for addinmetro_addin.extension (Extension)"""
    def __init__(self):
        # For performance considerations, please remove all unused methods in this class.
        self.enabled = True
    def activeViewChanged(self):
        print("activeView changed")


def get_layer(mxd, layer_name):
    """Retourne si elle existe dans le mxd la couche du nom passé en paramètre."""
    layers = arcpy.mapping.ListLayers(mxd)
    for layer in layers:
        if layer.name == layer_name:
            return layer


def add_layer(mxd, fc):
    """Ajout d'une classe d'entités à un document"""
    # Récupère le 1er bloc de données
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    # Création d'une nouvelle couche pointant vers la classe d'entités
    layer = arcpy.mapping.Layer(fc)
    # Ajout de la couche au bloc de données
    arcpy.mapping.AddLayer(df, layer, "AUTO_ARRANGE")
    # Rafraichit la vue et la table des matière
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()


def calcule_itineraire(mxd, fl_stations):
    """
    Fonction pour calculer un itinéraire sur le réseau de métro
    à partir d'une station de départ et d'une arrivée.

    LE JEU DE DONNEES RESEAU DOIT AVOIR ETE CREE A LA MAIN AUPRAVENT
    """
    arcpy.env.overwriteOutput = True
    # Définition des constantes
    ds_network = "Reseau/Reseau_ND"
    layer_group_na_name = "Metro"
    field_cost = "Minutes"
    layer_trajet_name = "Trajet"

    # Construction du réseau
    arcpy.na.BuildNetwork(ds_network)

    # Construction de la couche d'itinéraires
    layer_group_na = arcpy.na.MakeRouteLayer(ds_network, layer_group_na_name, field_cost).getOutput(0)
    sublayer_names = arcpy.na.GetNAClassNames(layer_group_na)
    stops_layer_name = sublayer_names["Stops"]
    route_layer_name = sublayer_names["Routes"]
    route_layer = arcpy.mapping.ListLayers(layer_group_na, route_layer_name)[0]

    # Ajout des stations sélectionnées aux arrêts de la couche d'itinéraire
    arcpy.na.AddLocations(layer_group_na, stops_layer_name, fl_stations)

    # Calcul de l'itinéraire
    arcpy.na.Solve(layer_group_na)

    # Copie du résultat dans une classe d'entité et ajout au document
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    arcpy.CopyFeatures_management(route_layer, layer_trajet_name)
    if not get_layer(mxd, layer_trajet_name):
        add_layer(mxd, layer_trajet_name)
    pythonaddins.MessageBox(u"Itinéraire calculé.", u"Calcul d'itinéraires")
