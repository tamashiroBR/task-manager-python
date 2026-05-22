#!/usr/bin/env python3
"""
Gerenciador de Tarefas CLI
Um aplicativo simples de linha de comando para gerenciar tarefas com persistência em JSON.
"""

import json
import os
from datetime import datetime
from typing import List, Dict

TASKS_FILE = "tasks.json"


def load_tasks() -> List[Dict]:
    """Carrega tarefas do arquivo JSON."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_tasks(tasks: List[Dict]) -> None:
    """Salva tarefas no arquivo JSON."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(title: str, description: str = "") -> None:
    """Adiciona uma nova tarefa."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "completed": False,
        "created_at": datetime.now().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✓ Tarefa '{title}' adicionada com sucesso!")


def list_tasks() -> None:
    """Lista todas as tarefas."""
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return

    print("\n" + "=" * 60)
    print("SUAS TAREFAS".center(60))
    print("=" * 60)
    for task in tasks:
        status = "✓" if task["completed"] else "○"
        print(f"{status} [{task['id']}] {task['title']}")
        if task["description"]:
            print(f"   └─ {task['description']}")
    print("=" * 60 + "\n")


def complete_task(task_id: int) -> None:
    """Marca uma tarefa como concluída."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"✓ Tarefa {task_id} marcada como concluída!")
            return
    print(f"✗ Tarefa {task_id} não encontrada.")


def delete_task(task_id: int) -> None:
    """Deleta uma tarefa."""
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print(f"✓ Tarefa {task_id} deletada!")


def show_menu() -> None:
    """Exibe o menu principal."""
    print("\n" + "=" * 40)
    print("GERENCIADOR DE TAREFAS".center(40))
    print("=" * 40)
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar como concluída")
    print("4. Deletar tarefa")
    print("5. Sair")
    print("=" * 40)


def main() -> None:
    """Função principal."""
    while True:
        show_menu()
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            title = input("Título da tarefa: ").strip()
            description = input("Descrição (opcional): ").strip()
            add_task(title, description)

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            try:
                task_id = int(input("ID da tarefa a marcar como concluída: "))
                complete_task(task_id)
            except ValueError:
                print("✗ ID inválido!")

        elif choice == "4":
            try:
                task_id = int(input("ID da tarefa a deletar: "))
                delete_task(task_id)
            except ValueError:
                print("✗ ID inválido!")

        elif choice == "5":
            print("Até logo!")
            break

        else:
            print("✗ Opção inválida!")


if __name__ == "__main__":
    main()
