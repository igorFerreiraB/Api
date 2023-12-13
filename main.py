from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": "Lata", "preço_unitario": 4, "Quantidade": 5}, 
    2: {"item": "garrafa 2L", "preço_unitario": 15, "Quantidade": 5},
    3: {"item": "garraf 750ML", "preço_unitario": 10, "Quantidade": 5},
    4: {"item": "Lata mini", "preço_unitario": 2, "Quantidade": 5},
    5: {"item": "garrafa 3L", "preço_levando3+": 12.50, "Quantidade": 10},
}


@app.get("/")
async def home():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
async def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return{"Erro": "ID inexistente"}
