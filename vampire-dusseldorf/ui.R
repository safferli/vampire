## header content
header <- dashboardHeader(title = "Vampire Düsseldorf")

## Sidebar content
sidebar <-   dashboardSidebar(
  sidebarMenu(
    menuItem("Overview", tabName = "tab_overview", icon = icon("list")),
    menuItem("Vampires", tabName = "tab_vampires", icon = icon("sunglasses", lib = "glyphicon")),
    menuItem("Politics", tabName = "tab_politics", icon = icon("king", lib = "glyphicon")),
    menuItem("Domain", tabName = "tab_domain", icon = icon("map-o")),
    menuItem("Raw data", icon = icon("database"),
             menuSubItem("vampires", tabName = "tab_data1"),
             menuSubItem("connections", tabName = "tab_data2")
             )
  )
)

## Body content
body <-   dashboardBody(
  tabItems(
    
    # OVERVIEW tab content
    tabItem(tabName = "tab_overview",
            h2("overview tab content")
    ),
    
    # VAMPIRES tab content
    tabItem(tabName = "tab_vampires",
            fluidRow(
              box(
                title = "Vampire population census", 
                status = "primary",
                plotOutput("plot_clans"), 
                width = 8
              ),
              box(
                selectInput("i_clan", label = "x-axis is: ", choices = choices_i_clan, selected = "Clan"),
                width = 2
              )
            )
    ),
    
    # POLITICS tab content
    tabItem(tabName = "tab_politics",
            h2("politics tab content")
    ),
    
    # DOMAIN tab content
    tabItem(tabName = "tab_domain",
            h2("domain tab content")
    ),
    
    # DATA tab content
    tabItem(tabName = "tab_data1",
            h2("Vampires in Düsseldorf"),
            dataTableOutput("DT_vampires")
    ),
    tabItem(tabName = "tab_data2",
            h2("Connections between vampires"),
            dataTableOutput("DT_connections")
    )
  )
)

# put everything together now! 
ui <- dashboardPage(header, sidebar, body)
