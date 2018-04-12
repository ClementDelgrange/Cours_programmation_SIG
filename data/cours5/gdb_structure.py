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
