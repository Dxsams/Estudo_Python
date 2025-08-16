# Módulo 6 – Tratamento de Erros e Exceções em Python

## Objetivo

Aprender a lidar com erros no Python de forma segura usando:

- `try` → tentar executar código
- `except` → capturar erros
- `else` → executar se não houver erro
- `finally` → sempre executar
- `raise` → gerar exceções manualmente

---

## Atividades

### Atividade 1 – Divisão Segura

- Captura `ValueError` e `ZeroDivisionError`
- Exibe resultado apenas se não houver erro
- Usa `finally` para mensagem final

### Atividade 2 – Manipulação de Arquivos

- Verifica se arquivo existe
- Cria arquivo se não existir
- Trata `FileNotFoundError` e outros erros

### Atividade 3 – Calculadora com Loop

- Solicita dois números e operação
- Trata entradas inválidas e divisão por zero
- Loop contínuo até usuário digitar "sair"
- Usa `finally` para indicar fim de cada operação

---

## Desafios Extras

1. Calculadora avançada com tratamento de erros
2. Leitura e criação de arquivos de forma segura
3. Lista de números: maior, menor e média com validação de entradas

---

## Observações

- Use `try/except` em entradas de usuário e operações críticas
- `finally` garante execução de ações finais
- `raise` pode ser usado para gerar erros personalizados
