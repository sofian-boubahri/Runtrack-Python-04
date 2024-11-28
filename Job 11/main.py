def time_to_text(nombre_entier):
    heures = nombre_entier // 60
    minutes_restant = nombre_entier % 60

    print(heures, "heures et", minutes_restant, "minutes")
time_to_text(1000)