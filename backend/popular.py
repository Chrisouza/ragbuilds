import json
import os
import requests
import time
import sqlite3


conexao = sqlite3.connect("db\\db.sqlite3")
cur = conexao.cursor()


def popular_classes():
    with open("db\\classes.json") as f:
        data = json.load(f)
        for classe in data:
            try:
                sql_verifica = f"SELECT * FROM classes WHERE nome='{
                    classe['nome']}'"
                verifica = cur.execute(sql_verifica)
                sql_insert = "INSERT INTO classes VALUES (?, ?)"
                cur.execute(sql_insert, (None, classe['nome']))
                conexao.commit()
            except:
                pass


def pega_dados_itens():
    chars = ["¶", "¸", "£", "½", "º", "°", "©", "¿",
             "Ê", 'Ç', 'û', '³', 'ª', 'Ò', 'Ä', '«', '°', '©']
    error = ""
    apiKey = os.environ.get('API_KEY')
    start, max = (501, 16685)

    with open("db\\itens.json", "w") as f:
        f.write(f"[\n")

    for i in range(start, max):
        try:
            url = "https://www.divine-pride.net/api/database/Item/"
            url += f"{i}?apiKey={apiKey}&server=bRO"
            response = requests.get(url)
            response = response.json()

            for char in chars:
                if char in response['name']:
                    error += char

            if error == "":
                data = {"idItem": response['id'], "nome": response['name']}
                data = json.dumps(data)
                with open("db\\itens.json", "a+") as f:
                    f.write(f"{data},\n")
                    print(f"{response['name']} salvo no json")
            else:
                print(f"Erro com letras estranhas {error}")
            error = ""
        except Exception as e:
            print(f"Erro {e}")
        time.sleep(1)

    with open("db\\itens.json", "a+") as f:
        f.write(f"]")


def popular_itens():
    with open("db\\itens.json") as f:
        data = json.load(f)
        for item in data:
            try:
                sql_insert = "INSERT INTO itens VALUES (?,?,?)"
                cur.execute(
                    sql_insert, (None, item['idItem'], item['nome']))
                conexao.commit()
            except Exception as e:
                print(e)


def main():
    print("Populando classes")
    popular_classes()


    if not os.path.exists("db\\itens.json"):
        print("Pegando dados de itens")
        pega_dados_itens()

    input("Aguardando corrigir json")

    print("Populando itens")
    popular_itens()


if __name__ == "__main__":
    main()
#
