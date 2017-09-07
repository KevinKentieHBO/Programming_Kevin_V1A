cijferICOR = 7.0
cijferPROG = 7.5
cijferCSN = 6.5

gemiddelde = (cijferCSN + cijferICOR + cijferPROG)/3
beloning = cijferPROG * 30 + cijferICOR * 30 + cijferCSN * 30
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van € ' + str(beloning) + ' op!'

print(overzicht)