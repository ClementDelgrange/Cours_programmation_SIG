# -*- coding: utf-8 -*-

import arcpy

# Script arguments
line_number = arcpy.GetParameterAsText(0)
if line_number == '#' or not line_number:
    line_number = "3"

ws = arcpy.GetParameterAsText(1)
if ws == "#" or not ws:
    ws = "D:\\ArcGIS"

# Local variables:
line_txt = ws + "\\l" + line_number + ".txt"
gdb = ws + "\\TD3.gdb\\"
fc_line = gdb + "\\Reseau\\Ligne" + line_number
layer_stations = "Stations_layer" + line_number
fc_stations_name = "Stations_ligne" + line_number
fc_stations = gdb + fc_stations_name


# Process: Générer une couche d’événements XY
arcpy.MakeXYEventLayer_management(line_txt, "x", "y", layer_stations, "PROJCS['RGF_1993_Lambert_93',GEOGCS['GCS_RGF_1993',DATUM['D_RGF_1993',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',700000.0],PARAMETER['False_Northing',6600000.0],PARAMETER['Central_Meridian',3.0],PARAMETER['Standard_Parallel_1',44.0],PARAMETER['Standard_Parallel_2',49.0],PARAMETER['Latitude_Of_Origin',46.5],UNIT['Meter',1.0]];-35597500 -23641900 10000;-100000 10000;-100000 10000;0,001;0,001;0,001;IsHighPrecision", "")

# Process: Classe d’entités vers classe d’entités
arcpy.FeatureClassToFeatureClass_conversion(layer_stations, gdb, fc_stations_name, "", "x \"x\" true true false 8 Double 0 0 ,First,#,stations_layer,x,-1,-1;y \"y\" true true false 8 Double 0 0 ,First,#,stations_layer,y,-1,-1;nom \"nom\" true true false 8000 Text 0 0 ,First,#,stations_layer,nom,-1,-1", "")

# Process: Points vers lignes
arcpy.PointsToLine_management(fc_stations, fc_line, "", "", "NO_CLOSE")
