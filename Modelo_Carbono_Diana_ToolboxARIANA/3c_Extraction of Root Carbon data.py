# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2024-01-02 12:12:50
"""
import arcpy
from arcpy.sa import *
from sys import argv

# output_directory = r"C:\Users\taller\Documents\ArcGIS\Projects\PythonModels\PythonModels.gdb\Model3cOutput"
# output_directory_raster = r"C:\Users\taller\Documents\ArcGIS\Projects\PythonModels\PythonModels.gdb"

# roots_C_hf_log_final=r"C:\Users\taller\Desktop\ArianaRiosArcGIS\PythonModels\Modelo_Carbono_Diana_Data\Datos_Carbono\BioclimClipPRSLM_V1_sa_units800.gdb\roots_C_hf_log_final"
# StrmHillElev=r"C:\Users\taller\Documents\ArcGIS\Projects\PythonModels\PythonModels.gdb\Model2Output\StrmHillElev"

def Model6(roots_C_hf_log_final, StrmHillElev, output_directory, output_directory_raster):  # 3c_Extraction of Root Carbon data

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("3D")
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")
    arcpy.CheckOutExtension("ImageExt")

    # Model Environment settings
    with arcpy.EnvManager(cellSize="MAXOF", extent="526570.079847613 1644641.67664025 661135.079847613 1714721.67664025", mask=r"C:\Users\taller\Desktop\ArianaRiosArcGIS\PythonModels\Modelo_Carbono_Diana_Data\Landslides_SLM_Red_2018_N\Insumos_Red_2018_N15m\dem15aff", 
                          snapRaster=r"C:\Users\taller\Desktop\ArianaRiosArcGIS\PythonModels\Modelo_Carbono_Diana_Data\Landslides_SLM_Red_2018_N\Insumos_Red_2018_N15m\dem15aff"):

        # Process: Make Feature Layer (Make Feature Layer) (management)
        StrmHillElev_Layer = "StrmHillElev_Layer2"
        arcpy.management.MakeFeatureLayer(in_features=StrmHillElev, out_layer=StrmHillElev_Layer, where_clause="", workspace="", field_info="OBJECTID OBJECTID VISIBLE NONE;Shape Shape VISIBLE NONE;FID_Elevation_RioHondo FID_Elevation_RioHondo VISIBLE NONE;Id Id VISIBLE NONE;gridcode gridcode VISIBLE NONE;HydroID HydroID VISIBLE NONE;GridID GridID VISIBLE NONE;NextDownID NextDownID VISIBLE NONE;OBJECTID_1 OBJECTID_1 VISIBLE NONE;arcid arcid VISIBLE NONE;grid_code grid_code VISIBLE NONE;from_node from_node VISIBLE NONE;to_node to_node VISIBLE NONE;DrainID DrainID VISIBLE NONE;Shape_Leng Shape_Leng VISIBLE NONE;StrOrder StrOrder VISIBLE NONE;Shape_Length Shape_Length VISIBLE NONE;Shape_Area Shape_Area VISIBLE NONE")

        # Process: Raster Calculator (Raster Calculator) (sa)
        RootCarbon100 = output_directory_raster + r"\RootCarbon100"
        Raster_Calculator = RootCarbon100
        roots_C_hf_log_final_raster = Raster(roots_C_hf_log_final)
        RootCarbon100 = roots_C_hf_log_final_raster * 100
        RootCarbon100.save(Raster_Calculator)


        # Process: Int (Int) (sa)
        RootCarbon100Int = output_directory_raster + r"\RootCarbon100Int"
        Int = RootCarbon100Int
        RootCarbon100Int = arcpy.sa.Int(in_raster_or_constant=RootCarbon100)
        RootCarbon100Int.save(Int)


        # Process: Build Raster Attribute Table (Build Raster Attribute Table) (management)
        RootCarbon_clip_ha_int_2_ = arcpy.management.BuildRasterAttributeTable(in_raster=RootCarbon100Int, overwrite="NONE")[0]

        # Process: Zonal Statistics as Table (Zonal Statistics as Table) (sa)
        RootCarb_table = output_directory_raster + r"\RootCarb_table"
        Zonal_Statistics_as_Table_Result = arcpy.sa.ZonalStatisticsAsTable(in_zone_data=StrmHillElev, zone_field="gridcode", in_value_raster=RootCarbon_clip_ha_int_2_, out_table=RootCarb_table, ignore_nodata="DATA", statistics_type="MEAN", process_as_multidimensional="CURRENT_SLICE", percentile_values=[])
    


        # Process: Add Join (Add Join) (management)
        StrmHillElev_Layer_3_ = arcpy.management.AddJoin(in_layer_or_view=StrmHillElev_Layer, in_field="gridcode", join_table=RootCarb_table, join_field="gridcode", join_type="KEEP_ALL")[0]

        # Process: Select (Select) (analysis)
        RootCarbon = output_directory + r"\RootCarbon"
        arcpy.analysis.Select(in_features=StrmHillElev_Layer_3_, out_feature_class=RootCarbon, where_clause="")

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\taller\Documents\ArcGIS\Projects\PythonModels\PythonModels.gdb", workspace=r"C:\Users\taller\Documents\ArcGIS\Projects\PythonModels\PythonModels.gdb"):
        Model6(*argv[1:])
