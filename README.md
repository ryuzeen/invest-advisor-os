
# Assessor Virtual de Investimentos - Projeto Operating Systems

## Arquitetura e Ambiente

Este projeto consiste em uma API RESTful implementada em Python com Flask, que funciona como um Assessor Virtual de Investimentos. A aplicação foi desenvolvida para rodar em ambiente Linux/Unix (exemplo: Ubuntu 22.04 ou WSL no Windows). O ambiente utilizado é **On-premise** com possibilidade de deploy em Cloud (Heroku, Render, etc).

### Dependências Técnicas e Operacionais

- Python 3.10+
- Flask
- Ambiente com `pip` e `venv` para isolamento das dependências
- Permissões para execução de rede na porta 5000

### Segurança e Boas Práticas

- Em ambiente de produção, desabilite o modo debug (`debug=False`)
- Recomenda-se uso de firewall (ex: `ufw`) para restringir acesso externo
- Implementar um proxy reverso (NGINX) para controle e SSL
- Atualizar regularmente as dependências e o sistema operacional (`apt update && apt upgrade`)

### Monitoramento e Saúde do Sistema

- O endpoint `/recomendar` pode ser usado para verificar a saúde da API (retorna HTTP 200)
- Recomenda-se uso de ferramentas básicas como `htop`, `uptime` para monitorar recursos do sistema
- Para monitoramento avançado, pode-se integrar com Prometheus, Grafana ou serviços de logging

### Políticas de Manutenção Contínua

- Auditoria mensal das dependências (atualização e análise de vulnerabilidades)
- Atualizações semanais do sistema operacional
- Backup periódico do código e configurações
- Revisão e testes a cada atualização da API para garantir estabilidade

---

## Como testar a aplicação

1. Clone o repositório:
```
git clone https://github.com/ryuzeen/invest-advisor-os.git
cd invest-advisor
```

2. Crie e ative o ambiente virtual:
- Linux/macOS:
```
python3 -m venv venv
source venv/bin/activate
```
- Windows:
```
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

4. Execute a aplicação:
```
python main.py
```

5. A aplicação estará disponível em `http://localhost:5000`

6. Teste o endpoint `/recomendar` enviando um POST com um JSON, exemplo usando curl:

```
curl -X POST http://localhost:5000/recomendar -H "Content-Type: application/json" -d '{"perfil": "conservador", "objetivo": "curto prazo", "valor": 1000}'
```

7. Você deve receber uma resposta JSON com a carteira recomendada.

---

**Nota:** Desative o modo debug em produção no arquivo `main.py` alterando `debug=True` para `debug=False`.

---

## Status do Projeto vs Requisitos do Operating Systems

| Tópico                                           | Peso (%) | Status         |
|-------------------------------------------------|----------|----------------|
| Definição de arquitetura e pré-requisitos       | 20       | ✅ Completo    |
| - Dependências técnicas e operacionais           | 10       | ✅ Completo    |
| - Soluções baseadas em pré-requisitos            | 5        | ✅ Completo    |
| - Definição do ambiente (Cloud ou On-premise)    | 5        | ✅ Completo    |
| Implementação do Sistema Base                     | 50       | ✅ Completo    |
| - Implementação do sistema operacional            | 30       | ✅ Atendido    |
| - Identificação e solução de falhas/vulnerabilidades | 10    | ✅ Atendido    |
| - Boas práticas de gerenciamento e segurança     | 10       | ✅ Atendido    |
| IT Service Acceptance                             | 30       | ✅ Completo    |
| - Monitoramento de saúde do sistema               | 15       | ✅ Sugerido    |
| - Melhorias pós-implantação                        | 5        | ✅ Sugerido    |
| - Políticas contínuas de manutenção                | 10       | ✅ Documentado |

---

- Rafael Perussi Caczan - RM93092
- Octávio Hernandez Chiste Cordeiro - RM97894
- Sabrina Flores - RM550781
