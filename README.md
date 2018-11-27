# Information Engineering Project

## Hypothese

Durch streichen von Wörter, die nicht relevant sind, werden die Resultate relevanter.

## Forschungsfrage

Kann ich durch Eliminierung von vermeindlich Tehemenirrelevanten Wörtern doe Hypothese verifizieren?

## Vorgehen

```bash
eliminate stop words
for each query
    for each document
        calculate distance from words in document to closest query word
        remove bottom 10% most distant words
        return TF-IDF
```

