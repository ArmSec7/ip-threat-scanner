import requests
import time
import csv
import os
from dotenv import load_dotenv

# 1. Configurações Iniciais
load_dotenv()  # Carrega a API Key do arquivo .env
API_KEY = os.getenv('VT_API_KEY')
URL = 'https://www.virustotal.com/api/v3/ip_addresses/'

# Verificação de segurança da Chave
if not API_KEY:
    print("[!] ERRO: API_KEY não encontrada. Verifique o seu arquivo .env")
    exit()

def consultar_ip(ip):
    """Consulta um IP no VirusTotal e retorna os resultados formatados."""
    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }
    
    try:
        response = requests.get(URL + ip, headers=headers)
        
        if response.status_code == 200:
            dados = response.json()
            # Extrai estatísticas de análise
            stats = dados['data']['attributes']['last_analysis_stats']
            malicioso = stats['malicious']
            suspeito = stats['suspicious']
            limpo = stats['harmless']
            
            return [ip, "Sucesso", malicioso, suspeito, limpo]
            
        elif response.status_code == 429:
            return [ip, "Erro 429: Limite de taxa excedido", 0, 0, 0]
        else:
            return [ip, f"Erro {response.status_code}", 0, 0, 0]
            
    except Exception as e:
        return [ip, f"Falha na conexão: {str(e)}", 0, 0, 0]

# 2. Execução Principal
def main():
    arquivo_entrada = 'ips.txt'
    arquivo_saida = 'relatorio_ips.csv'
    
    try:
        # Lê a lista de IPs
        with open(arquivo_entrada, 'r') as f:
            lista_ips = [line.strip() for line in f if line.strip()]

        if not lista_ips:
            print("[!] O arquivo ips.txt está vazio.")
            return

        print(f"[*] Iniciando varredura de {len(lista_ips)} IPs...")
        print("-" * 50)

        # Prepara o arquivo CSV de saída
        with open(arquivo_saida, 'w', newline='') as f_csv:
            writer = csv.writer(f_csv)
            # Cabeçalho do relatório
            writer.writerow(['IP', 'Status_Conexao', 'Malicioso', 'Suspeito', 'Limpo'])

            for ip in lista_ips:
                resultado = consultar_ip(ip)
                writer.writerow(resultado)
                
                # Feedback visual no terminal
                status_msg = "PERIGO" if resultado[2] > 0 else "LIMPO"
                print(f"[+] {ip} -> {status_msg} (Maliciosos: {resultado[2]})")
                
                # Pausa obrigatória para API gratuita (4 requisições por minuto)
                # Se tiver apenas 1 IP na lista, ele termina rápido. Se tiver vários, ele aguarda.
                if len(lista_ips) > 1:
                    time.sleep(15)

        print("-" * 50)
        print(f"[!] Varredura concluída! Resultados salvos em: {arquivo_saida}")

    except FileNotFoundError:
        print(f"[!] ERRO: O arquivo '{arquivo_entrada}' não foi encontrado na pasta.")

if __name__ == "__main__":
    main()