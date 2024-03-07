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


def popular_itens():
    apiKey = os.environ.get('API_KEY')
    start, max = (501, 16685)
    for i in range(start, max):
        try:
            url = "https://www.divine-pride.net/api/database/Item/"
            url += f"{i}?apiKey={apiKey}&server=bRO"
            response = requests.get(url)
            response = response.json()
            sql_insert = "INSERT INTO itens VALUES (?,?,?)"
            cur.execute(
                sql_insert, (None, response['id'], response['name']))
            conexao.commit()
            time.sleep(3)
        except:
            pass


def main():
    print("Populando classes")
    popular_classes()
    # print("Populando itens")
    # popular_itens()


if __name__ == "__main__":
    main()
