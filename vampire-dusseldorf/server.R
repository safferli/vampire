
shinyServer(function(input, output) {

  ## VAMPIRES output
  output$plot_clans <- renderPlot({
    vampires %>% 
      ggplot()+
      geom_bar(aes(x=get(input$i_clan), fill = get(choices_i_clan[choices_i_clan != input$i_clan])))+
      labs(x = paste("Vampire population census by", input$i_clan), fill = choices_i_clan[choices_i_clan != input$i_clan])
  })
  
  ## RAW DATA output
  output$DT_vampires <- renderDataTable({
    vampires
  })
  output$DT_connections <- renderDataTable({
    connections
  })

})
