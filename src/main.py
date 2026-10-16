"""
Калькулятор личных финансов
Приложение для учета доходов и расходов
"""

import json
import os
from datetime import datetime

DATA_FILE = "data.json"


def load_data():
    """Загружает данные из файла"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_data(data):
    """Сохраняет данные в файл"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_operation():
    """Добавляет новую операцию (доход/расход)"""
    print("\n=== Добавление операции ===")
    op_type = input("Тип операции (доход/расход): ").strip().lower()
    
    if op_type not in ("доход", "расход"):
        print(" Неверный тип операции!")
        return
    
    try:
        amount = float(input("Сумма: "))
        if amount <= 0:
            print("❌ Сумма должна быть положительной!")
            return
    except ValueError:
        print("❌ Неверная сумма!")
        return
    
    category = input("Категория: ").strip()
    date = input("Дата (ГГГГ-ММ-ДД) или Enter для сегодня: ").strip()
    
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    operation = {
        "type": op_type,
        "amount": amount,
        "category": category,
        "date": date
    }
    
    data = load_data()
    data.append(operation)
    save_data(data)
    print("✅ Операция успешно добавлена!")


def show_operations():
    """Показывает все операции"""
    print("\n=== Все операции ===")
    data = load_data()
    
    if not data:
        print("📭 Нет операций.")
        return
    
    print(f"{'Дата':<12} {'Тип':<8} {'Категория':<15} {'Сумма':<10}")
    print("-" * 50)
    
    for op in data:
        print(f"{op['date']:<12} {op['type']:<8} {op['category']:<15} {op['amount']:<10.2f}")


def show_balance():
    """Показывает текущий баланс"""
    print("\n=== Баланс ===")
    data = load_data()
    
    income = sum(op["amount"] for op in data if op["type"] == "доход")
    expense = sum(op["amount"] for op in data if op["type"] == "расход")
    balance = income - expense
    
    print(f" Доходы: {income:.2f}")
    print(f"💸 Расходы: {expense:.2f}")
    print(f" Баланс: {balance:.2f}")


def menu():
    """Главное меню приложения"""
    while True:
        print("\n" + "=" * 40)
        print("🏦 КАЛЬКУЛЯТОР ЛИЧНЫХ ФИНАНСОВ")
        print("=" * 40)
        print("1. ➕ Добавить операцию")
        print("2. 📋 Просмотреть все операции")
        print("3. 📊 Показать баланс")
        print("4.  Выход")
        print("=" * 40)
        
        choice = input("Выбор: ").strip()
        
        if choice == "1":
            add_operation()
        elif choice == "2":
            show_operations()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            print("\n👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    menu()
