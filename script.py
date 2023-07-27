def calculate_ticket_cost(age):
    if age < 18:
        return 0
    elif 18 <= age < 25:
        return 990
    else:
        return 1390

def main():
    num_tickets = int(input("Введите количество билетов: "))
    total_cost = 0

    for _ in range(num_tickets):
        age = int(input("Введите возраст посетителя: "))
        ticket_cost = calculate_ticket_cost(age)
        total_cost += ticket_cost

    if num_tickets > 3:
        total_cost *= 0.9  

    print("Общая стоимость билетов:", total_cost, "руб.")

if __name__ == "__main__":
    main()