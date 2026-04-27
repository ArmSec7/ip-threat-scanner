# 🛡️ IP Threat Intelligence Scanner

> Automação em Python para triagem massiva de Indicadores de Comprometimento (IoC) via VirusTotal API v3.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Security+](https://img.shields.io/badge/CompTIA-Security%2B-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Desenvolvimento-green?style=for-the-badge)

Em operações de **SOC (Security Operations Center)**, a análise manual de centenas de logs é inviável. Este script automatiza a consulta de reputação de IPs, permitindo que o analista foque na resposta ao incidente, não na coleta de dados.

---

## 🛠️ Funcionalidades
- **Triagem em Lote:** Processa múltiplos endereços IPv4 simultaneamente.
- **Veredito em Tempo Real:** Consulta mais de 70 motores de análise (Kaspersky, Sophos, CrowdStrike, etc).
- **Gestão de Rate Limit:** Algoritmo de espera inteligente para usuários da API gratuita (4 requisições/min).
- **Relatórios Estruturados:** Exportação direta para CSV, pronto para ingestão em SIEMs ou Excel.
- **Segurança de Credenciais:** Implementação de variáveis de ambiente para proteção de API Keys.

---

## 📂 Estrutura do Projeto
```text
ip-threat-scanner/
├── .env                # Chaves de API (não incluído no repositório)
├── .env.example        # Modelo para configuração de chaves
├── .gitignore          # Proteção de arquivos sensíveis
├── README.md           # Documentação técnica
├── requirements.txt    # Dependências do projeto
├── ips.txt             # Lista de IPs para scan
└── vt_scanner.py       # Script principal