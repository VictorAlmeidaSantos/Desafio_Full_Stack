from fastapi import APIRouter, Body, HTTPException
from app.models.cat_question import lista_gatos, datas_nascimento

router = APIRouter()

# Método que recebe um ID e retorna os dados do gato e sua data de nascimento
@router.get("/gato/{id}")
def get_gato_por_id(id: int):
    try:
        # Tratando os erros caso o id não exista ou o id seja diferente de int
        gato = next((g for g in lista_gatos if g.id == id), None)
        if gato is None:
            # Se o id do gato não existir, retorna o corpo especificado em README.md,
            # não uma mensagem de aviso.
            return {
                "id": id,
                "nome": "Qualquer",
                "raca": "Qualquer",
                "idade": 0,
                "data_nascimento": "0000-00-00"
            }

        # Tratando o erro para caso a data de nascimento não exista ou o iterador passar por erros
        data_nascimento = next((d['data_nascimento'] for d in datas_nascimento if isinstance(d, dict) and d['id'] == id), None)
        if data_nascimento is None:
            # Se a data de nascimento do gato não existir (ou estiver errada),
            # retorna o corpo especificado em README.md, não uma mensagem de aviso.
            data_nascimento = "0000-00-00"
        else:
            data_nascimento = data_nascimento.strftime('%Y-%m-%d')
        
        return {
            'id': gato.id,
            'nome': gato.nome,
            'raca': gato.raca,
            'idade': int(gato.idade), # int() para ter a certeza de idade ser um int
            'data_nascimento': data_nascimento
        }
    except Exception as e:
        # Retorna uma exceção genérica caso algum erro desconhecido ocorra.
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
# Método que retorna a lista de gatos sem data de nascimento e sem idade
@router.get("/gato")
def get_gatos():
    """_summary_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """

    '''Como o método descreve que é pra retornar os gatos sem data de nascimento "e" sem idade,
    decidi que deveria retornar os gatos sem data e com idade que seja diferente de inteiro,
    assim satisfaria o não ter data e nem idade.
    '''

    try:
        gatos_sem_data_nascimento_e_idade = []
        for gato in lista_gatos:
            # Usando isintance para verificar se d é um dicionário, assim evitar erros ao percorrer a lista.
            if not isinstance(gato.idade, int) and  not any(d['id'] == gato.id for d in datas_nascimento if isinstance(d, dict)):
                gatos_sem_data_nascimento_e_idade.append({
                    'id': gato.id,
                    'nome': gato.nome,
                    'raca': gato.raca
                })

        return gatos_sem_data_nascimento_e_idade
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Método que retorna uma lista de todos os gatos mais velhos com a mesma idade
@router.post("/gatos-mais-velhos")
def get_gatos_mais_velhos():
    # Assim como o método anterior, decidi que os gatos com idade != int não deveriam ser considerados.
    try:
        # Encontra a idade máxima entre todos os gatos
        # Usando isinstance() para impedir max() de comparar idades != int 
        idade_maxima = max(gato.idade for gato in lista_gatos if isinstance(gato.idade, int))
        
        # Lista para armazenar todos os gatos mais velhos com a mesma idade máxima
        gatos_mais_velhos = []
        for gato in lista_gatos:
            # Usando isinstance() para lidar apenas com objetos de idade == int
            if gato.idade == idade_maxima and isinstance(gato.idade, int):
                # Encontra a data de nascimento do gato
                data_nascimento_gato = next((d['data_nascimento'] for d in datas_nascimento if isinstance(d, dict) and d['id'] == gato.id), None)

                # Tratando a possibilidade de data de nascimento não existir (ou estiver errada)
                # retorna o corpo especificado em README.md, não uma mensagem de aviso.
                if data_nascimento_gato is None:
                    data_nascimento_gato = "0000-00-00"
                else:
                    data_nascimento_gato = data_nascimento_gato.strftime('%Y-%m-%d')
                
                # Adiciona o gato à lista com sua data de nascimento
                gatos_mais_velhos.append({
                    'id': gato.id,
                    'nome': gato.nome,
                    'raca': gato.raca,
                    'idade': gato.idade,
                    'data_nascimento': data_nascimento_gato
                })
        
        return gatos_mais_velhos
    except Exception as e:
        return HTTPException(status_code=500, detail="Internal Server Error")

# Método que busca gatos por um termo de busca no nome
@router.post("/buscar-gatos")
def buscar_gatos_por_nome(termo_busca: str = Body(...)):
    try:
        # Transforma a lista de gatos em um dicionário onde as chaves são os IDs
        # Usando isinstance() para pegar apenas os objetos com id == int
        dict_gatos = {gato.id: gato for gato in lista_gatos if isinstance(gato.id, int)}
        
        gatos_encontrados = []
        for gato_id, gato in dict_gatos.items():
            if termo_busca.lower() in gato.nome.lower():
                data_nascimento_gato = next((d['data_nascimento'] for d in datas_nascimento if isinstance(d, dict) and d['id'] == gato_id), None)
                # Tratando a possibilidade de data de nascimento não existir (ou estiver errada)
                # retorna o corpo especificado em README.md, não uma mensagem de aviso.
                if data_nascimento_gato is None:
                    data_nascimento_gato = "0000-00-00"
                else:
                    data_nascimento_gato = data_nascimento_gato.strftime('%Y-%m-%d')

                gatos_encontrados.append({
                    'id': gato.id,
                    'nome': gato.nome,
                    'raca': gato.raca,
                    'idade': gato.idade,
                    'data_nascimento': data_nascimento_gato
                })
        
        # retorna o corpo especificado em README.md caso não tenha encontrado nenhum gato com termo_busca
        if gatos_encontrados == []:
            gatos_encontrados.append({
                "id": 0,
                "nome": "Qualquer",
                "raca": "Qualquer",
                "idade": 0,
                "data_nascimento": "0000-00-00"
            })
            
        return {'gatos_encontrados': gatos_encontrados}
    except Exception as e:
        raise HTTPException(status_code=200, detail="Internal Server Error")


# Método que busca gatos por raça
@router.get("/buscar-raca")
def buscar_gatos_por_raca(termo_busca: str = Body(...)):
    try:
        gatos_encontrados = [gato.__dict__ for gato in lista_gatos if gato.raca.lower() == termo_busca.lower()]

        for gato in gatos_encontrados:
            # Tratando data de nascimento e depois inserindo nos dicionários de gatos_encontrados
            data_nascimento_gato = next((d['data_nascimento'] for d in datas_nascimento if isinstance(d, dict) and d['id'] == gato['id']), None)
            if data_nascimento_gato is None:
                gato['data_nascimento'] = "0000-00-00"
            else:
                gato['data_nascimento'] = data_nascimento_gato.strftime('%Y-%m-%d')

        return {'gatos_encontrados': gatos_encontrados}
    except Exception as e:
        return HTTPException(status_code=500, detail="Internal Server Error")