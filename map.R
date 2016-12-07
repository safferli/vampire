rm(list = ls()); gc(); gc()
# options(java.parameters = "-Xmx4096m")#8192
# options(java.parameters = "-XX:-UseConcMarkSweepGC")
# options(java.parameters = "-XX:-UseGCOverheadLimit")
options(bitmapType='cairo')
options(scipen = 999)

#library(googlesheets)
library(dplyr)
#library(tidyr)
#library(ggplot2)
library(leaflet)

# Define your workspace: "X:/xxx/"
#wd <- "D:/github/statistics101/"
wd <- path.expand("~/Documents/github/vampire")
setwd(wd)

# # list all sheets, which include "Vampire"
# #gs_ls("Vampire")
# 
# # https://docs.google.com/spreadsheets/d/1Gruo1DnElwTIAs42l-jK5JH5ckT_lKWR3goFx4W6XIs/pubhtml
# # register the "Vampire Düsseldorf" sheet
# gd <- gs_key("1Gruo1DnElwTIAs42l-jK5JH5ckT_lKWR3goFx4W6XIs")
# 
# # list all worksheets
# gs_ws_ls(gd)
# 
# # pull data
# vampires <- gs_read(gd, ws = "vampires", range = cell_cols(1:8))
# connections <- gs_read(gd, ws = "connections")


### maps

# http://maps.duesseldorf.de/Gesamt/

# Coordinates of Dusseldorf in decimal degrees
# Latitude: 51.2217200°
# Longitude: 6.7761600°
# Coordinates of Dusseldorf in degrees and decimal minutes
# Latitude: 51°13.3032′ N
# Longitude: 6°46.5696′ E


dus <- leaflet() %>% 
  setView(lng = 6.77616, lat = 51.22172, zoom = 13) %>% 
  addTiles() %>% 
  addWMSTiles(
    "http://maps.duesseldorf.de/Gebietsgrenzen_WMS/service.svc/get",
    layers = "Stadtgrenze,Stadtbezirke,Stadtteile,Beschriftung_Stadtbezirke", 
    options = WMSTileOptions(
      service = "WMS",
      request = "GetMap",
      #format = "image/%2Fpng",
      transparent = TRUE,
      #crs = "EPSG%3A25832",
      #height = "758",
      #width = "1283",
      #bbox = "315554.9183536442,5657847.100243192,385497.898041144,5699197.860919056",
      styles = ",,,",
      version = "1.3.0"
      ),
    attribution = "Stadt- und Bezirksgrenzen Daten © Landeshauptstadt Düsseldorf 2016"
    )

dus

# WMS: get map image renderings from server
# WFS: get data from server (web feature service)

# https://www.citypopulation.de/php/germany-dusseldorf.php


