import json
import sqlite3
import csv


conexao = sqlite3.connect("db\\db.sqlite3")
cur = conexao.cursor()


def openJSON(path):
    with open(path, "r") as f:
        return json.load(f)


def popularClasses():
    classes = openJSON(path="db\\job.json")
    for level in classes:
        for classe in classes[level]:
            idClasse = int(classe['id'])
            nome = classe['name_en']
            img_path = classe['img_path']
            try:
                cur.execute("INSERT INTO classes VALUES (?, ?, ?, ?)",
                            (None, idClasse, nome, img_path))
                conexao.commit()
                print(f"{classe['name_en']} salvo no banco")
            except Exception as e:
                pass
                # print(e)


def popularItens():
    arquivos = ["acessorio", "arma", "calcado",
                "capa", "cabeca", "escudo", "sombrio"]
    for arquivo in arquivos:
        tipo = arquivo
        with open(f"db\\{arquivo}.csv", "r", encoding="utf8") as f:
            data = csv.reader(f)
            next(f)
            for row in data:
                try:
                    idItem = row[0]
                    nome = row[1]
                    descricao = row[5]
                    cur.execute("INSERT INTO itens VALUES (?,?,?,?,?)",
                                (None, idItem, nome, descricao, tipo))
                    conexao.commit()
                    print(f"Item {nome} salvo")
                except Exception as e:
                    pass


popularClasses()
popularItens()
