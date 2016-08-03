## header content
header <- dashboardHeader(title = "Vampire Düsseldorf")

## Sidebar content
sidebar <-   dashboardSidebar(
  sidebarMenu(
    menuItem("Overview", tabName = "tab_overview", icon = icon("list")),
    menuItem("Vampires", tabName = "tab_vampires", icon = icon("sunglasses", lib = "glyphicon")),
    menuItem("Politics", tabName = "tab_politics", icon = icon("king", lib = "glyphicon")),
    menuItem("Domain", tabName = "tab_domain", icon = icon("map-o")),
    menuItem("Raw data", tabName = "tab_data", icon = icon("database"))
  )
)

## Body content
body <-   dashboardBody(
  tabItems(
    # First tab content
    tabItem(tabName = "tab_overview",
            fluidRow(
              box(plotOutput("distPlot", height = 250)),
              
              box(
                title = "Controls",
                sliderInput("bins", "Number of observations:", 1, 100, 50)
              )
            )
    ),
    
    # Second tab content
    tabItem(tabName = "tab_vampires",
            h2("vampires tab content")
    ), 
    
    # third tab content
    tabItem(tabName = "tab_politics",
            h2("politics tab content")
    ),
    
    # fourth tab content
    tabItem(tabName = "tab_domain",
            h2("domain tab content")
    ),
    
    # fifth tab content
    tabItem(tabName = "tab_data",
            h2("data tab content")
    )
  )
)

# put everything together now! 
ui <- dashboardPage(header, sidebar, body)
