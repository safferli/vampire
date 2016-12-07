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
#gs_ls("Vampire")

# https://docs.google.com/spreadsheets/d/1Gruo1DnElwTIAs42l-jK5JH5ckT_lKWR3goFx4W6XIs/pubhtml
# register the "Vampire Düsseldorf" sheet
gd <- gs_key("1Gruo1DnElwTIAs42l-jK5JH5ckT_lKWR3goFx4W6XIs")

# list all worksheets
gs_ws_ls(gd)

# pull data
vampires <- gs_read(gd, ws = "vampires", range = cell_cols(1:8))
connections <- gs_read(gd, ws = "connections")


# clans
vampires %>% 
  ggplot()+
  geom_bar(aes(x=Clan, fill=Covenant))

# covenants
vampires %>% 
  ggplot()+
  geom_bar(aes(x=Covenant, fill=Clan))



### network analysis

library(igraph)
library(networkD3)

# connections %>% 
#   simpleNetwork(Source = "from_id", Target = "to_id")

MisLinks <- MisLinks
MisNodes <- tibble::as_tibble(MisNodes) %>% mutate(nameChr = as.character(name))

forceNetwork(Links = MisLinks, Nodes = MisNodes,
             Source = "source", Target = "target",
             Value = "value", NodeID = "nameChr",
             Group = "group",
             zoom = TRUE)


gVamps <- connections %>% 
  # self-join bi-directional rows in reverse direction to get full directed network
  dplyr::bind_rows(
    connections %>% 
      filter(bi_directional == 1) %>% 
      mutate(
        tmp_id = from_id,
        from_id = to_id,
        to_id = tmp_id
      ) %>% 
      select(-tmp_id)
  ) %>% 
  mutate(
    from_id = from_id-1,
    to_id = to_id-1
  ) %>% 
  #graph.data.frame(vertices = vampires %>% mutate(FullName = paste0(Firstname, "'", Nickname, "'", Lastname), id = Id-1)) %>% 
  graph.data.frame() %>% 
  simplify()

nodeVamps <- vampires %>% 
  mutate(
    FullName = paste0(Firstname, "'", Nickname, "'", Lastname), 
    id = Id-1
  ) %>% 
  select(
    id, everything(), -Id
  )



forceNetwork(Links = gVamps, Nodes = nodeVamps,
             Source = "from_id", Target = "to_id",
             NodeID = "FullName", Group = "Covenant",
             zoom = TRUE)




# https://christophergandrud.github.io/networkD3/
# https://github.com/christophergandrud/networkD3/blob/master/inst/examples/examples.R
# http://igraph.org/r/
# http://kateto.net/networks-r-igraph
# http://www.vesnam.com/Rblog/viznets6/

