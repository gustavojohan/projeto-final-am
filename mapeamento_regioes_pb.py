# Mapeamento completo: município → mesorregião (IBGE)
# Fonte: IBGE - Divisão Regional do Brasil em Mesorregiões (1989-2017)
# Paraíba possui 223 municípios divididos em 4 mesorregiões
import unicodedata

MUNICIPIOS_POR_REGIAO = {

    "Sertão Paraibano": [
        # Catolé do Rocha
        "Belém do Brejo do Cruz","Bom Sucesso","Brejo do Cruz","Brejo dos Santos",
        "Catolé do Rocha","Jericó","Lagoa","Mato Grosso","Riacho dos Cavalos",
        "São Bento","São José do Brejo do Cruz",

        # Cajazeiras
        "Bernardino Batista","Bom Jesus","Bonito de Santa Fé","Cachoeira dos Índios",
        "Cajazeiras","Carrapateira","Joca Claudino","Monte Horebe",
        "Poço Dantas","Poço de José de Moura","Santa Helena",
        "São João do Rio do Peixe","São José de Piranhas","Triunfo","Uiraúna",

        # Sousa
        "Aparecida","Cajazeirinhas","Condado","Lastro", "Malta", "Marizópolis","Nazarezinho",
        "Paulista","Pombal","Santa Cruz","São Bentinho","São Domingos",
        "São Francisco","São José da Lagoa Tapada","Sousa","Vieirópolis","Vista Serrana",

        # Patos
        "Areia de Baraúnas","Cacimba de Areia","Mãe d'Água","Passagem","Patos",
        "Quixaba","Santa Teresinha","São José de Espinharas","São José do Bonfim",

        # Piancó
        "Aguiar","Catingueira","Coremas","Emas","Igaracy","Nova Olinda",
        "Olho d'Água","Piancó","Santana dos Garrotes",

        # Itaporanga
        "Boa Ventura","Conceição","Curral Velho","Diamante","Ibiara",
        "Itaporanga","Pedra Branca","Santa Inês","Santana de Mangueira",
        "São José de Caiana","Serra Grande",

        # Serra do Teixeira
        "Água Branca","Cacimbas","Desterro","Imaculada","Juru","Manaíra",
        "Maturéia","Princesa Isabel","São José de Princesa","Tavares","Teixeira",
    ],

    "Borborema": [
        # Seridó Ocidental
        "Junco do Seridó","Salgadinho","Santa Luzia","São José do Sabugi",
        "São Mamede","Várzea",

        # Seridó Oriental
        "Baraúna","Cubati","Frei Martinho","Juazeirinho","Nova Palmeira",
        "Pedra Lavrada","Picuí","São Vicente do Seridó","Tenório",

        # Cariri Ocidental
        "Amparo","Assunção","Camalaú","Congo","Coxixola","Livramento",
        "Monteiro","Ouro Velho","Parari","Prata","São João do Tigre",
        "São José dos Cordeiros","São Sebastião do Umbuzeiro",
        "Serra Branca","Sumé","Taperoá","Zabelê",

        # Cariri Oriental
        "Alcantil","Barra de Santana","Barra de São Miguel","Boqueirão",
        "Cabaceiras","Caraúbas","Caturité","Gurjão","Riacho de Santo Antônio",
        "Santo André","São Domingos do Cariri","São João do Cariri",
    ],

    "Agreste Paraibano": [
        # Curimataú Ocidental
        "Algodão de Jandaíra","Arara","Barra de Santa Rosa","Cuité",
        "Damião","Nova Floresta","Olivedos","Pocinhos","Remígio",
        "Soledade","Sossego",

        # Curimataú Oriental
        "Araruna","Cacimba de Dentro","Casserengue","Dona Inês",
        "Riachão","Solânea","Tacima",

        # Esperança
        "Areial","Esperança","Montadas","São Sebastião de Lagoa de Roça",

        # Brejo
        "Alagoa Grande","Alagoa Nova","Areia","Bananeiras","Borborema",
        "Matinhas","Pilões","Serraria",

        # Guarabira
        "Alagoinha","Araçagi","Belém","Caiçara","Cuitegi","Duas Estradas",
        "Guarabira","Lagoa de Dentro","Logradouro","Mulungu",
        "Pilõezinhos","Pirpirituba","Serra da Raiz","Sertãozinho",

        # Campina Grande
        "Boa Vista","Campina Grande","Fagundes","Lagoa Seca",
        "Massaranduba","Puxinanã","Queimadas","Serra Redonda",

        # Itabaiana
        "Caldas Brandão","Gurinhém","Ingá","Itabaiana","Itatuba",
        "Juarez Távora","Mogeiro","Riachão do Bacamarte",
        "Salgado de São Félix",

        # Umbuzeiro
        "Aroeiras","Gado Bravo","Natuba","Santa Cecília","Umbuzeiro",
    ],

    "Mata Paraibana": [
        # Litoral Norte
        "Baía da Traição","Capim","Cuité de Mamanguape","Curral de Cima",
        "Itapororoca","Jacaraú","Mamanguape","Marcação","Mataraca",
        "Pedro Régis","Rio Tinto",

        # Sapé
        "Cruz do Espírito Santo","Juripiranga","Mari","Pilar",
        "Riachão do Poço","São José dos Ramos","São Miguel de Taipu",
        "Sapé","Sobrado",

        # João Pessoa
        "Bayeux","Cabedelo","Conde","João Pessoa","Lucena","Santa Rita",

        # Litoral Sul
        "Alhandra","Caaporã","Pedras de Fogo","Pitimbu",
    ],
}

# ── Inverter o dicionário: município → região ──────────────────────────────────
MUNICIPIO_PARA_REGIAO = {}
for regiao, municipios in MUNICIPIOS_POR_REGIAO.items():
    for municipio in municipios:
        MUNICIPIO_PARA_REGIAO[municipio.upper()] = regiao


def normalizar(texto: str) -> str:
    """Remove acentos e converte para maiúsculas."""
    return unicodedata.normalize('NFKD', texto) \
        .encode('ASCII', 'ignore') \
        .decode('ASCII') \
        .upper() \
        .strip()


# Dicionário com chaves normalizadas (sem acento, maiúsculas)
MUNICIPIO_PARA_REGIAO_NORM = {
    normalizar(k): v for k, v in MUNICIPIO_PARA_REGIAO.items()
}


def mapear_regiao(nome_municipio: str) -> str:
    """
    Recebe o nome do município (string) e retorna a mesorregião.
    Normaliza acentos e maiúsculas automaticamente.
    Retorna 'Não identificado' se não encontrar.
    """
    if not isinstance(nome_municipio, str):
        return "Não identificado"
    return MUNICIPIO_PARA_REGIAO_NORM.get(normalizar(nome_municipio), "Não identificado")


# ── Como usar no seu notebook ──────────────────────────────────────────────────
# from mapeamento_regioes_pb import mapear_regiao
#
# df['regiao'] = df['NO_MUNICIPIO'].apply(mapear_regiao)
#
# # Verificar municípios não mapeados (para completar o dicionário)
# nao_mapeados = df[df['regiao'] == 'Não identificado']['NO_MUNICIPIO'].unique()
# print(f"Municípios não mapeados ({len(nao_mapeados)}):")
# print(sorted(nao_mapeados))
#
# # Distribuição por região
# print(df['regiao'].value_counts())


if __name__ == "__main__":
    # Teste rápido
    testes = ["João Pessoa", "Campina Grande", "Patos", "Sousa", "Guarabira", "XYZ"]
    for m in testes:
        print(f"{m:30} → {mapear_regiao(m)}")

    total = sum(len(v) for v in MUNICIPIOS_POR_REGIAO.values())
    print(f"\nTotal de municípios mapeados: {total} / 223")
