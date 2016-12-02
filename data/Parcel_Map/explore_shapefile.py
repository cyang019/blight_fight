# Import the necessary modules
from  osgeo import ogr, osr

driver = ogr.GetDriverByName('ESRI Shapefile')
shp = driver.Open('./parcels.shp')

# Get Projection from layer
layer = shp.GetLayer()
spatialRef = layer.GetSpatialRef()
print spatialRef

# Get Shapefile Fields and Types
layerDefinition = layer.GetLayerDefn()

print "Name  -  Type  Width  Precision"
for i in range(layerDefinition.GetFieldCount()):
    fieldName =  layerDefinition.GetFieldDefn(i).GetName()
    fieldTypeCode = layerDefinition.GetFieldDefn(i).GetType()
    fieldType = layerDefinition.GetFieldDefn(i).GetFieldTypeName(fieldTypeCode)
    fieldWidth = layerDefinition.GetFieldDefn(i).GetWidth()
    GetPrecision = layerDefinition.GetFieldDefn(i).GetPrecision()
    print fieldName + " - " + fieldType+ " " + str(fieldWidth) + " " + str(GetPrecision)

# Check if rows in attribute table meet some condition
inFeature = layer.GetNextFeature()
while inFeature:

    # get the cover attribute for the input feature
    cover = inFeature.GetField('cover')

    # check to see if cover == grass
    if cover == 'trees':
        print "Do some action..."

    # destroy the input feature and get a new one
    inFeature.Destroy()
    inFeature = inLayer.GetNextFeature()

