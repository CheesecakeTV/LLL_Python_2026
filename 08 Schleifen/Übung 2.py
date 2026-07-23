import random

namen = ["Anna", "Ben", "Carla", "Hans", "Martin", "Mira"]
namen = random.sample(namen, len(namen))
partner = namen[1:] + [namen[0]]

# def getPartnerListe(namenListe: list[str]) -> list[str]:
#     return random.sample(namenListe, len(namenListe))

# def getPartnerListe(namenListe: list[str]) -> list[str]:
#     ruckgabe = []
#     urne = namenListe.copy()
#
#     for name in namenListe:
#         while True:
#             pick = random.choice(urne)
#
#             if name != pick:
#                 break
#
#             if len(urne) == 1:
#                 return getPartnerListe(namenListe)
#
#         ruckgabe.append(pick)
#         urne.remove(pick)
#         #del urne[urne.index(pick)]
#
#     return ruckgabe
#
def printPartner(namenListe: list[str], partnerListe: list[str]):
    for n, p in zip(namenListe, partnerListe):
        print(n, "-", p)

# def ist_alles_richtig(namenListe: list[str], partnerListe: list[str]) -> bool:
#     for n, p in zip(namenListe, partnerListe):
#         if n == p:
#             return False
#
#     return True
#
# while True:
#     partner = getPartnerListe(namen)
#
#     if ist_alles_richtig(namen, partner):
#         break

# partner = getPartnerListe(namen)
printPartner(namen, partner)


