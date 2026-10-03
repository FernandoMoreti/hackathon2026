import io
import json
import xmltodict

def read_xml_file(file_content: bytes):
    data = xmltodict.parse(file_content)

    nfe_root = data.get("nfeProc", {}).get("NFe", {}).get("infNFe", {})

    if not nfe_root:
        # Caso o XML não tenha a tag nfeProc (ex: XML avulso)
        nfe_root = data.get("NFe", {}).get("infNFe", {})

    # 1. Extraindo dados gerais da nota (Cabeçalho)
    ide = nfe_root.get("ide", {})
    dados_gerais = {
        "chave_acesso": nfe_root.get("@Id", "").replace("NFe", ""),
        "numero_nf": ide.get("nNF"),
        "serie": ide.get("serie"),
        "data_emissao": ide.get("dhEmi"),
        "natureza_operacao": ide.get("natOp"),
    }

    # 2. Extraindo Emitente
    emit = nfe_root.get("emit", {})
    emitente = {
        "cnpj": emit.get("CNPJ"),
        "nome": emit.get("xNome"),
        "fantasia": emit.get("xFant"),
    }

    # 4. Transporte e Pesos (<transp> e <vol>)
    transp = nfe_root.get("transp", {})
    vol_raw = transp.get("vol", [])
    if isinstance(vol_raw, dict):
        vol_raw = [vol_raw]

    peso_liquido_total = 0.0
    peso_bruto_total = 0.0
    volumes = []

    for vol in vol_raw:
        p_liq = float(vol.get("pesoL", 0) or 0)
        p_bru = float(vol.get("pesoB", 0) or 0)
        peso_liquido_total += p_liq
        peso_bruto_total += p_bru

        volumes.append(
            {
                "quantidade_volumes": vol.get("qVol"),
                "especie": vol.get("esp"),
                "peso_liquido": p_liq,
                "peso_bruto": p_bru,
            }
        )

    transporte = {
        "modalidade_frete": transp.get("modFrete"),
        "peso_liquido_total": peso_liquido_total,
        "peso_bruto_total": peso_bruto_total,
        "detalhes_volumes": volumes,
    }

    dest = nfe_root.get("dest", {})
    destinatario = {
        "cnpj_cpf": dest.get("CNPJ") or dest.get("CPF"),
        "nome": dest.get("xNome"),
    }

    det_raw = nfe_root.get("det", [])
    if isinstance(det_raw, dict):
        det_raw = [det_raw]

    itens = []
    for item in det_raw:
        prod = item.get("prod", {})
        rastro = prod.get("rastro", {}) # Se houver lote/validade

        itens.append({
            "n_item": item.get("@nItem"),
            "codigo": prod.get("cProd"),
            "ean": prod.get("cEAN"),
            "descricao": prod.get("xProd"),
            "ncm": prod.get("NCM"),
            "cfop": prod.get("CFOP"),
            "unidade": prod.get("uCom"),
            "quantidade": float(prod.get("qCom", 0)),
            "valor_unitario": float(prod.get("vUnCom", 0)),
            "valor_total": float(prod.get("vProd", 0)),
            "lote": rastro.get("nLote") if isinstance(rastro, dict) else None,
            "validade": rastro.get("dVal") if isinstance(rastro, dict) else None,
        })

    nfe_estruturada = {
        "geral": dados_gerais,
        "emitente": emitente,
        "destinatario": destinatario,
        "transporte": transporte,
        "itens": itens
    }

    json_formatado = json.dumps(
        nfe_estruturada, indent=4, ensure_ascii=False
    )
    print("\n--- JSON DA NFE EXTRAÍDA ---")
    print(json_formatado)

    return nfe_estruturada