# Information Engineering Project

## Hypothese

Durch streichen von Wörter, die nicht relevant sind, werden die Resultate relevanter.

## Forschungsfrage

Kann ich durch Eliminierung von vermeindlich Themenirrelevanten Wörtern die Hypothese verifizieren?

## Vorgehen

```bash
# Psuedocode
eliminate stop words
for each query
    for each document
        calculate distance from words in document to closest query word
        remove n-percentile most distant words
        return TF-IDF
```
