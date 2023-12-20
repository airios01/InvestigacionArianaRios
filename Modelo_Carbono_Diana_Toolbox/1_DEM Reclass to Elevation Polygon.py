# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-12-14 14:39:59
"""
import arcpy
from sys import argv

Watershed_Elevation=r"C:\Users\taller\Documents\ArcGIS\Projects\PythonModels\PythonModels.gdb\Elevation_RioHondo"

Study_Area_DEM=r"C:\Users\taller\Desktop\ArianaRiosArcGIS\PythonModels\Modelo_Carbono_Diana_Data\Landslides_SLM_Red_2018_N\Insumos_Red_2018_N15m\dem15aff" 

def Model3(Watershed_Elevation, Study_Area_DEM):  # 1_DEM Reclass to Elevation Polygon

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("3D")
    arcpy.CheckOutExtension("spatial")

    # Model Environment settings
    with arcpy.EnvManager(cellSize="MAXOF", extent="526570.079847613 1644641.67664025 661135.079847613 1714721.67664025", mask=r"C:\Users\taller\Desktop\ArianaRiosArcGIS\PythonModels\Modelo_Carbono_Diana_Data\Landslides_SLM_Red_2018_N\Insumos_Red_2018_N15m\dem15aff", 
                          snapRaster=r"C:\Users\taller\Desktop\ArianaRiosArcGIS\PythonModels\Modelo_Carbono_Diana_Data\Landslides_SLM_Red_2018_N\Insumos_Red_2018_N15m\dem15aff"):
        dem_reclass_table75m = r"C:\Users\taller\Desktop\ArianaRiosArcGIS\PythonModels\Modelo_Carbono_Diana_Data\Landslides_SLM_Red_2018_N\Insumos_Red_2018_N15m\archivos.gdb\dem_reclass_table75m"
        Chosen_Watershed = r"C:\Users\taller\Desktop\ArianaRiosArcGIS\PythonModels\Modelo_Carbono_Diana_Data\Landslides_SLM_Red_2018_N\Insumos_Red_2018_N15m\Watershed.shp"

        # Process: Reclass by Table (Reclass by Table) (sa)
        DEM_Reclass = r"C:\Users\taller\Documents\ArcGIS\Projects\PythonModels\PythonModels.gdb\Model1Output\RioHondo_elevation_75m"
        Reclass_by_Table = DEM_Reclass
        DEM_Reclass = arcpy.sa.ReclassByTable(in_raster=Study_Area_DEM, in_remap_table=dem_reclass_table75m, from_value_field="FROM_", to_value_field="TO", output_value_field="OUT", missing_values="DATA")
        DEM_Reclass.save(Reclass_by_Table)


        # Process: Raster to Polygon (Raster to Polygon) (conversion)
        DEM_Polygon_Shapefile = r"C:\Users\taller\Documents\ArcGIS\Projects\PythonModels\PythonModels.gdb\Model1Output\DEM_poly"
        arcpy.conversion.RasterToPolygon(in_raster=DEM_Reclass, out_polygon_features=DEM_Polygon_Shapefile, simplify="SIMPLIFY", raster_field="VALUE", create_multipart_features="SINGLE_OUTER_PART", max_vertices_per_feature=None)

        # Process: Clip (Clip) (analysis)
        arcpy.analysis.Clip(in_features=DEM_Polygon_Shapefile, clip_features=Chosen_Watershed, out_feature_class=Watershed_Elevation, cluster_tolerance="")

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\taller\Documents\ArcGIS\Projects\PythonModels\PythonModels.gdb\Model1Output", workspace=r"C:\Users\taller\Documents\ArcGIS\Projects\PythonModels\PythonModels.gdb\Model1Output"):
        Model3(Watershed_Elevation, Study_Area_DEM)
