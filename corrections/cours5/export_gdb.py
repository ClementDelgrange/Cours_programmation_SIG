# -*- coding: utf-8 -*-
import arcpy


def make_feature_layer(fc):
    """
    Ajoute une classe d'entité à ArcMap et retourne la couche créée.

    :param fc: nom de la classe d'entités à ajouter
    :return: couche d'entités
    """
    fl = "fl_{}".format(fc)
    arcpy.MakeFeatureLayer_management(fc, fl)
    return fl


def export_fc_by_location(fc, fl_ref, out_rep):
    """
    Exporte les entités d'une classe d'entités qui intersectent les entités
    sélectionnées d'une couche de référence.

    :param fc: classe d'entités où se trouvent les entités à exporter
    :param fl_ref: couche de référence contenant les entités sélectionnées
    :param out_rep: répertoire d'export
    """
    fl = make_feature_layer(fc)
    shp = "{}.shp".format(fc)

    arcpy.SelectLayerByLocation_management(fl, "INTERSECT", fl_ref, "", "NEW_SELECTION")
    arcpy.FeatureClassToFeatureClass_conversion(fl, out_rep, shp)
    print("{} exportée".format(fc))


def export_data(insee, gdb, out_rep):
    arcpy.env.workspace = gdb

    # Chargement des communes dans ArcMap
    fc_commune = "COMMUNE"
    fl_commune = make_feature_layer(fc_commune)
    shp_commune = "{}.shp".format(fc_commune)

    # Export de la commune
    req = "CODE_INSEE = {}".format(insee)
    arcpy.SelectLayerByAttribute_management(fl_commune, "NEW_SELECTION", req)
    arcpy.FeatureClassToFeatureClass_conversion(fl_commune, out_rep, shp_commune)
    print("COMMUNE exportée")

    # Export des autres couches
    fcs = ["COURS_D_EAU", "HYDROGRAPHIE_SURFACIQUE", "TRONCON_HYDROGRAPHIE"]
    for fc in fcs:
        export_fc_by_location(fc, fl_commune, out_rep)


if __name__ == '__main__':
    rep = r"D:\ProgSIG\TD_arcpy"
    gdb = rep + r"\data\BaseHydro_ok.gdb"

    insee = int(input("Code INSEE de la commune à extraire ? "))

    export_data(insee, gdb, rep)
