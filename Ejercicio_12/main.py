from Estructura import EstructuraArqueologica, SubEstructura

# Ejemplo de uso
estructura1 = SubEstructura("E001", "1000 AC", ["piedra", "madera"])
estructura2 = SubEstructura("E002", "500 AC", ["ladrillo", "madera"], [estructura1])
estructura3 = SubEstructura("E003", "200 AC", ["piedra"], [estructura2])

print(estructura1)
print(estructura2)
print(estructura3)