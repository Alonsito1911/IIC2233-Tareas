
def combate(client_socket1, client_socket2, lista : dict):
    carta_cliente1 = lista[client_socket1]["carta"]

    carta_cliente2 = lista[client_socket2]["carta"]

    dic_ = {}

    if carta_cliente1["elemento"] == "fuego" and carta_cliente2["elemento"] == "agua":
        dic_[client_socket1] = {"resultado": "perdedor", "carta": carta_cliente1}

        return dic_

    elif carta_cliente1["elemento"] == "fuego" and carta_cliente2["elemento"] == "nieve":

        dic_[client_socket1] = {"resultado": "ganador", "carta": carta_cliente1}
        return dic_

    elif carta_cliente1["elemento"] == "nieve" and carta_cliente2["elemento"] == "agua":
        dic_[client_socket1] = {"resultado": "ganador", "carta":  carta_cliente1}
        return dic_


    elif carta_cliente1["elemento"] == "nieve" and carta_cliente2["elemento"] == "fuego":
        dic_[client_socket1] = {"resultado": "perdedor", "carta": carta_cliente1}
        return dic_


    elif carta_cliente1["elemento"] == "agua" and carta_cliente2["elemento"] == "nieve":
        dic_[client_socket1] = {"resultado": "perdedor", "carta": carta_cliente1}
        return dic_


    elif carta_cliente1["elemento"] == "agua" and carta_cliente2["elemento"] == "fuego":
        dic_[client_socket1] = {"resultado": "ganador", "carta": carta_cliente1}
        return dic_
    #######3

    #####3
    elif carta_cliente1["elemento"] == "nieve" and carta_cliente2["elemento"] == "nieve":
        if int(carta_cliente1["puntos"]) > int(carta_cliente2["puntos"]):
            dic_[client_socket1] = {"resultado": "ganador", "carta": carta_cliente1}
            return dic_
        elif int(carta_cliente1["puntos"]) < int(carta_cliente2["puntos"]):
            dic_[client_socket1] = {"resultado": "perdedor","carta": carta_cliente1}
            return dic_
        else:
            dic_[client_socket1] = {"resultado": "empate","carta": carta_cliente1}
            return dic_

    elif carta_cliente1["elemento"] == "fuego" and carta_cliente2["elemento"] == "fuego":
        if int(carta_cliente1["puntos"]) > int(carta_cliente2["puntos"]):
            dic_[client_socket1] = {"resultado": "ganador", "carta": carta_cliente1}
            return dic_
        elif int(carta_cliente1["puntos"]) < int(carta_cliente2["puntos"]):
            dic_[client_socket1] = {"resultado": "perdedor", "carta": carta_cliente1}
            return dic_
        else:
            dic_[client_socket1] = {"resultado": "empate","carta": carta_cliente1}
            return dic_
    elif carta_cliente1["elemento"] == "agua" and carta_cliente2["elemento"] == "agua":
        if int(carta_cliente1["puntos"]) > int(carta_cliente2["puntos"]):
            dic_[client_socket1] = {"resultado":"ganador", "carta": carta_cliente1}
            return dic_
        elif int(carta_cliente1["puntos"]) < int(carta_cliente2["puntos"]):
            dic_[client_socket1] = {"resultado": "perdedor", "carta": carta_cliente1}
            return dic_
        else:
            dic_[client_socket1] = {"resultado": "empate", "carta": carta_cliente1}
            return dic_

    else:
        print("ERRORR")
        dic_[client_socket1] = {"resultado": "erroneo", "carta": carta_cliente1}
        return dic_
