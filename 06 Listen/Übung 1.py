
einkaufsliste = ["Apfel", "Brot", "Milch"]

# Füge "Banane" und "Käse" hinzu.
einkaufsliste.append("Banane")
einkaufsliste.append("Käse")

# Sortiere die Liste alphabetisch
einkaufsliste.sort()

# Falls "Gurken" noch nicht in der Liste ist (im Code prüfen!), füge es hinzu.
if "Gurken" not in einkaufsliste:
    einkaufsliste.append("Gurken")

# Gib aus, wie lang die Liste ist
print(len(einkaufsliste))

# Dein Partner wünscht sich auch noch Dinge, die du in dein Skript kopierst:
wuensche = ["Pfirsich", "Ananas", "Schokolade"]
# Füge die Wünsche deiner Liste hinzu.
einkaufsliste.extend(wuensche)

# 6. Lösche das letzte Element deiner Liste.
einkaufsliste.pop()
#del einkaufsliste[-1]

# 7. Gib die komplette Liste aus.
print(einkaufsliste)


