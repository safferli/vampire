library(shiny)
library(shinydashboard)
library(googlesheets)
library(dplyr)
library(ggplot2)
library(markdown)

# https://docs.google.com/spreadsheets/d/1Gruo1DnElwTIAs42l-jK5JH5ckT_lKWR3goFx4W6XIs/pubhtml
# register the "Vampire Düsseldorf" sheet
gd <- gs_key("1Gruo1DnElwTIAs42l-jK5JH5ckT_lKWR3goFx4W6XIs")

# pull data
vampires <- gs_read(gd, ws = "vampires", range = cell_cols(1:8))
connections <- gs_read(gd, ws = "connections", range = cell_cols(1:9))

# choices
choices_i_clan <- c("Clan", "Covenant")
