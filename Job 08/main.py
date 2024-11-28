def function(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaud, aubergine, navet")
    else: 
        print("Je ne sais pas.")

function("fruits", "hiver")  
function("fruits", "été")  
function("légume", "hiver")  
function("légume", "été")    
function("fruits", "printemps")  