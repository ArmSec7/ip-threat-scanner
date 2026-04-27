# 🛡️ Threat Intelligence IP Scanner (VirusTotal API)

Este projeto é um script de automação em Python desenvolvido para auxiliar analistas de Cibersegurança e SOC na triagem rápida de **Indicadores de Comprometimento (IoCs)**. 

O script consulta uma lista de endereços IP na API do VirusTotal, verifica sua reputação em mais de 70 motores de análise e exporta um relatório detalhado em CSV.

## 🚀 Funcionalidades
- **Análise em lote:** Processa múltiplos IPs de uma vez através de um arquivo `.txt`.
- **Segurança de Credenciais:** Utiliza variáveis de ambiente (`.env`) para proteger a API Key.
- **Rate Limiting:** Controle automático de requisições para respeitar os limites da API gratuita.
- **Relatório Automático:** Gera um arquivo `.csv` com o veredito de cada IP (Malicioso, Suspeito, Limpo).

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- Requests (Manipulação de APIs HTTP)
- Python-dotenv (Gestão de variáveis de ambiente)
- CSV (Estruturação de dados de saída)

## 📖 Como usar
1. Clone este repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Crie um arquivo `.env` e adicione sua `VT_API_KEY`.
4. Coloque os IPs desejados em `ips.txt`.
5. Execute: `python vt_scanner.py`.

---
*Projeto desenvolvido como parte dos meus estudos para a certificação CompTIA Security+.*