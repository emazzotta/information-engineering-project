# Information Engineering Project

## Hypothese

Durch streichen von Wörter, die nicht relevant sind, werden die Resultate relevanter.

## Forschungsfrage

Kann ich durch Eliminierung von vermeindlich Tehemenirrelevanten Wörtern doe Hypothese verifizieren?

## Vorgehen

for each document:
    eliminate stop words
    for each word in text:
        if word in search_terms
            next word
        else
            count distance to nearest word in searchterms
            map.put(word, min_distance)

map.crop bottom 10% of total_word_count

TF-IDF            

            

        
