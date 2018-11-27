# Information Engineering Project

## Hypothese

Durch streichen von Wörter, die nicht relevant sind, werden die Resultate relevanter.

## Forschungsfrage

Kann ich durch Eliminierung von vermeindlich Tehemenirrelevanten Wörtern doe Hypothese verifizieren?

## Vorgehen

for each document:
    eliminate stop words
    for each search_query_term:
        find out distance to other words in text (excluding)
        
