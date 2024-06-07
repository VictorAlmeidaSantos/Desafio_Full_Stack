from fastapi import APIRouter, Body, HTTPException
from app.models.cat_question import lista_gatos, datas_nascimento

router = APIRouter()

# Método que recebe um ID e retorna os dados do gato e sua data de nascimento
@router.get("/gato/{id}")
def get_gato_por_id(id: int):
    try:
        gato = next((g for g in lista_gatos if g.id == id), None)
        data_nascimento = next((d['data_nascimento'] for d in datas_nascimento if d['id'] == id), None)
        return {
            'id': gato.id,
            'nome': gato.nome,
            'raca': gato.raca,
            'idade': gato.idade,
            'data_nascimento': data_nascimento.strftime('%Y-%m-%d')
        }
    except Exception as e:
        return HTTPException(status_code=500, detail="Internal Server Error")
    
# Método que retorna a lista de gatos sem data de nascimento e sem idade
@router.get("/gato")
def get_gatos():
    """_summary_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    try:
        gatos_sem_data_nascimento = []
        for gato in lista_gatos:
            return lista_gatos
            if not any(d['id'] == gato.id for d in datas_nascimento):
                gatos_sem_data_nascimento.append({
                    'id': gato.id,
                    'nome': gato.nome,
                    'raca': gato.raca
                })
        return gatos_sem_data_nascimento
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Método que retorna uma lista de todos os gatos mais velhos com a mesma idade
@router.post("/gatos-mais-velhos")
def get_gatos_mais_velhos():
    try:
        # Encontra a idade máxima entre todos os gatos
        idade_maxima = max(gato.idade for gato in lista_gatos)
        
        # Lista para armazenar todos os gatos mais velhos com a mesma idade máxima
        gatos_mais_velhos = []
        for gato in lista_gatos:
            if gato.idade == idade_maxima:
                # Encontra a data de nascimento do gato
                data_nascimento_gato = next((d['data_nascimento'] for d in datas_nascimento if d['id'] == gato.id), None)
                
                # Adiciona o gato à lista com sua data de nascimento
                gatos_mais_velhos.append({
                    'id': gato.id,
                    'nome': gato.nome,
                    'raca': gato.raca,
                    'idade': gato.idade,
                    'data_nascimento': data_nascimento_gato.strftime('%Y-%m-%d')
                })
        
        return gatos_mais_velhos
    except Exception as e:
        return HTTPException(status_code=500, detail="Internal Server Error")

# Método que busca gatos por um termo de busca no nome
@router.post("/buscar-gatos")
def buscar_gatos_por_nome(termo_busca: str = Body(...)):
    try:
        # Transforma a lista de gatos em um dicionário onde as chaves são os IDs
        dict_gatos = {gato.id: gato for gato in lista_gatos}
        
        gatos_encontrados = []
        for gato_id, gato in dict_gatos.items():
            if termo_busca.lower() in gato.nome.lower():
                
                # Adiciona o gato encontrado ao resultado, excluindo o atributo idade
                gatos_encontrados.append(gato)
        
        return {'gatos_encontrados': gatos_encontrados}
    except Exception as e:
        raise HTTPException(status_code=200, detail="Internal Server Error")


# Método que busca gatos por raça
@router.get("/buscar-raca")
def buscar_gatos_por_raca(termo_busca: str = Body(...)):
    try:
        gatos_encontrados = [gato.__dict__ for gato in lista_gatos if gato.raca.lower() == termo_busca.lower()]
        return {'gatos_encontrados': gatos_encontrados}
    except Exception as e:
        return HTTPException(status_code=500, detail="Internal Server Error")