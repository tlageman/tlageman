layer = iface.addVectorLayer("/Users/tjleggz/Desktop/GES 687/Project2_Lageman/shapefiles/HousingCitationsProj.shp", '', 'ogr')

y = 0
year = 2008
while y < 11:
    strYear = str(year)
    layer.selectByExpression(" \"Year\" = '{}' ".format(strYear), QgsVectorLayer.SetSelection)
    year = year + 1
    y = y + 1
    QgsVectorFileWriter.writeAsVectorFormat(layer, r'/Users/tjleggz/Desktop/GES 687/Project2_Lageman/shapefiles/' + strYear + '.GPKG', 'utf-8', layer.crs(),'GPKG', True)