# 📝 Gerenciador de Tarefas CLI (Python)

Um aplicativo simples de linha de comando para gerenciar tarefas com persistência em JSON, construído usando apenas a biblioteca padrão do Python.

## 🚀 Funcionalidades

- Adicionar novas tarefas com título e descrição
- Listar todas as tarefas com status visual
- Marcar tarefas como concluídas
- Deletar tarefas
- Persistência de dados em arquivo JSON (`tasks.json`)

## 🛠️ Tecnologias

- Python 3.x
- Módulos built-in: `json`, `os`, `datetime`

## 📦 Como executar

1. Clone o repositório
2. Navegue até o diretório do projeto:
   ```bash
   cd 1-task-manager-python
   ```
3. Execute o script:
   ```bash
   python3 tasks.py
   ```

## 📝 Estrutura do JSON

As tarefas são salvas no formato:
```json
[
  {
    "id": 1,
    "title": "Aprender Python",
    "description": "Estudar a biblioteca padrão",
    "completed": false,
    "created_at": "2023-10-25T10:30:00.000000"
  }
]
```

## 📄 Licença

Este projeto está sob a licença MIT.
