# -*- coding: utf-8 -*-
import os
import datetime
import arcpy


DICO_GDB_STRUCT = {
    "ADMINISTRATIF": {
        "COMMUNE": {
            "Shape": ["Geometry", 0],
            "OBJECTID": ["OID", 4],
            "NOM": ["String", 50],
            "CODE_INSEE": ["Integer", 4],
            "STATUT": ["String", 200],
            "Shape_Length": ["Double", 8],
            "Shape_Area": ["Double", 8]
        }
    },
    "HYDROGRAPHIE": {
        "HYDROGRAPHIE_SURFACIQUE": {
            "Shape": ["Geometry", 0],
            "OBJECTID": ["OID", 4],
            "NATURE": ["String", 25],
            "TYPE": ["String", 30],
            "TOPONYME": ["String", 127],
            "Shape_Length": ["Double", 8],
            "Shape_Area": ["Double", 8]
        },
        "TRONCON_HYDROGRAPHIE": {
            "Shape": ["Geometry", 0],
            "OBJECTID": ["OID", 4],
            "ETAT": ["String", 25],
            "SENS": ["String", 25],
            "LARGEUR": ["String", 25],
            "NATURE": ["String", 25],
            "TOPONYME": ["String", 127],
            "Shape_Length": ["Double", 8]
        },
        "COURS_D_EAU": {
            "Shape": ["Geometry", 0],
            "OBJECTID": ["OID", 4],
            "CODE_HYDRO": ["String", 8],
            "CLASSE": ["String", 1],
            "TOPONYME": ["String", 127],
            "REGIME": ["String", 50],
            "Shape_Length": ["Double", 8]
        }
    }
}


def check_gdb(gdb, gdb_structure, flog):
    """
    Fonction de contrôle de la structure d'une géodatabase comparativement à une
    structure attendue.
    Un fichier de log du contrôle est écrit dans un fichier texte.
    Le nombre total d'erreurs rencontrées lors des contrôles est calculé et
    retourné à la fin.

    :param gdb: chemin de la géodatabase à contrôler
    :param gdb_structure: dictionnaire décrivant la structure attendue de la géodatabase
    :param flog: fichier de log où écrire les résultats des contrôles
    :return: nombre d'erreurs rencontrées
    """
    arcpy.env.workspace = gdb
    nb_erreurs = 0

    for dataset in gdb_structure:
        if not arcpy.Exists(dataset):
            write_log("Jeu de classes d'entités {} absent de la géodatabase".format(dataset), flog, 3)
            nb_erreurs += 1
            continue

        write_log("Jeu de classes d'entités {} présent dans la géodatabase".format(dataset), flog, 1)
        for table in gdb_structure[dataset]:
            if not arcpy.Exists(dataset + "\\" + table):
                write_log("Classe d'entités {} absente du jeu de classes d'entités {}".format(table, dataset), flog, 3)
                nb_erreurs += 1
                continue

            write_log("Classe d'entités {} présente dans le jeu de classes d'entités {}".format(table, dataset), flog, 1)
            nb_erreurs += check_table(table, dataset, gdb_structure[dataset][table], flog)

    for dataset in arcpy.ListDatasets():
        if dataset not in gdb_structure:
            write_log("Jeu de classes d'entités {} non requis dans la géodatabase".format(dataset), flog, 2)
            continue

        for fc in arcpy.ListFeatureClasses(feature_dataset=dataset):
            if fc not in gdb_structure[dataset]:
                write_log("Classes d'entités {} non requise dans le jeu de classes d'entités {}".format(fc, dataset), flog, 2)


    return nb_erreurs


def check_table(table, dataset, table_structure, flog):
    """
    Fonction de contrôle les champs d'une classe d'entités comparativement
    à une structure attendue (nom des champs, type et précision).
    Un fichier de log du contrôle est écrit dans un fichier texte.
    Le nombre total d'erreurs rencontrées lors des contrôles est calculé et
    retourné à la fin.

    :param table: nom de la table à contrôler
    :param dataset: nom du jeu de classes d'entités contenant la table
    :param table_structure: dictionnaire décrivant la structure attendue de la table
    :param flog: fichier de log où écrire les résultats des contrôles
    :return: nombre d'erreurs rencontrées
    """
    chemin_table = dataset + "\\" + table
    nb_erreurs = 0

    champs_presents = arcpy.ListFields(chemin_table)
    noms_champs_presents = [c.name for c in champs_presents]

    for champ in table_structure:
        if champ not in noms_champs_presents:
            write_log("Champ {} absent de la table {}".format(champ, table), flog, 3)
            nb_erreurs += 1
            continue

    for c in champs_presents:
        if c.name not in table_structure:
            write_log("Champ {} ({}, {}) non requis dans la table {}".format(c.name, c.type, c.length, table), flog, 2)
            continue

        write_log("Champ {} présent dans la table {}".format(c.name, table), flog, 1)
        if c.type != table_structure[c.name][0]:
            msg = "Type du champ {} de la table {} incorrect (attendu : {}, obtenu : {})".format(c.name, table, table_structure[c.name][0], c.type)
            write_log(msg, flog, 3)
            nb_erreurs += 1

        if c.length != table_structure[c.name][1]:
            msg = "Longueur du champ {} de la table {} incorrect (attendu : {}, obtenu : {})".format(c.name, table, table_structure[c.name][1], c.length)
            write_log(msg, flog, 3)
            nb_erreurs += 1

    return nb_erreurs


def write_log(msg, flog, importance=0):
    """
    Fonction d'écriture d'un message dans un fichier log.
    L'écriture du message peut être précédée d'une balise indiquant le type de
    message : [Info] pour un message d'information simple (importance=1),
    [Attention] pour une erreur non critique ou [ERREUR] pour signaler une
    erreur grave (importance=3).

    :param msg: la chaine de caractère à écrire dans le log
    :param flog: fichier de log où écrire les résultats des contrôles
    :param importance: code représentant l'importance du message
    """
    if not flog is None:
        if importance == 1:
            msg = "[Info]\t\t" + msg
        elif importance == 2:
            msg = "[Attention]\t" + msg
        elif importance == 3:
            msg = "[ERREUR]\t" + msg
        flog.writelines(msg + "\n")
        print(msg)


if __name__ == '__main__':
    rep = r"D:\ProgSIG\TD4"
    gdb = rep + r"\data\BaseHydro.gdb"

    # Initialisation d'un fichier de log flog
    pathlog = os.path.join(rep, "controle_gdb.log")
    date_debut = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
    flog = open(pathlog, "w")
    txt = "{} : Début des contrôles\n"\
          "Chemin de la géodatabase : {}\n".format(date_debut, gdb)
    write_log(txt, flog)

    # Contrôle de la gdb
    nb_err = check_gdb(gdb, DICO_GDB_STRUCT, flog)

    # Fin des contrôles
    date_fin = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
    txt = "\n{} Fin des contrôles\n"\
          "Nombre d'erreurs : {}".format(date_fin, nb_err)
    write_log(txt, flog)

    # Fermeture du fichier log
    if not flog is None:
        flog.close()
