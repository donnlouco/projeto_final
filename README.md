# Gerenciador de Eventos

Este projeto é um sistema de gerenciamento de eventos acadêmicos, desenvolvido em Python. Ele permite o cadastro, atualização, remoção e listagem de eventos e participantes, além de fornecer estatísticas e filtros avançados.

## Funcionalidades

- **Cadastro de Eventos:** Crie novos eventos informando nome, data, tema e local.
- **Gerenciamento de Participantes:** Cadastre, atualize, remova e busque participantes por CPF.
- **Listagem:** Veja participantes de cada evento e eventos em que um participante está inscrito.
- **Estatísticas:** 
  - Média de participantes por evento
  - Temas mais frequentes
  - Participantes mais ativos
  - Eventos por tema ou por data
  - Eventos com possibilidade de cancelamento (menos de 2 participantes)

## Estrutura do Projeto

```
projeto_final/
├── Estatisticas.py
├── Eventos.py
├── Main.py
├── Menu.py
├── Participantes.py
├── Util.py
├── testes.py
└── __pycache__/
```

- [`Main.py`](projeto_final/Main.py): Arquivo principal, executa o menu principal do sistema.
- [`Menu.py`](projeto_final/Menu.py): Implementa os menus de navegação.
- [`Eventos.py`](projeto_final/Eventos.py): Funções para cadastro, alteração, remoção e listagem de eventos.
- [`Participantes.py`](projeto_final/Participantes.py): Funções para gerenciar participantes.
- [`Estatisticas.py`](projeto_final/Estatisticas.py): Funções para estatísticas e filtragens.
- [`Util.py`](projeto_final/Util.py): Funções utilitárias (limpar tela, validação de data, etc).
- [`testes.py`](projeto_final/testes.py): Dados e funções de teste.

## Como Instalar

1. Clone o repositorio
   ``` sh
   git clone https://github.com/donnlouco/projeto_final.git
   ```


## Como Executar

1. Execute o arquivo principal:
   ```sh
   python Main.py
   ```

## Observações

- O sistema é totalmente interativo via **TERMINAL**.
- **Os dados são mantidos em memória enquanto o programa está em execução**.
- Para adicionar novos recursos, edite os arquivos correspondentes conforme a estrutura acima.

