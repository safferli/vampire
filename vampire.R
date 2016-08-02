rm(list = ls()); gc(); gc()
# options(java.parameters = "-Xmx4096m")#8192
# options(java.parameters = "-XX:-UseConcMarkSweepGC")
# options(java.parameters = "-XX:-UseGCOverheadLimit")
options(bitmapType='cairo')
options(scipen = 999)

library(googlesheets)
library(dplyr)
#library(tidyr)
library(ggplot2)

# Define your workspace: "X:/xxx/"
#wd <- "D:/github/statistics101/"
wd <- path.expand("~/Documents/github/vampire")
setwd(wd)

# list all sheets, which include "Vampire"
gs_ls("Vampire")

# register the "Vampire Düsseldorf" sheet
gd <- gs_key("1Gruo1DnElwTIAs42l-jK5JH5ckT_lKWR3goFx4W6XIs")

# list all worksheets
gs_ws_ls(gd)

# pull data
vampires <- gs_read(gd, ws = "vampires", range = cell_cols(1:8))
connections <- gs_read(gd, ws = "connections")
