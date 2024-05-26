def format_orders_summary(orders):
    if orders:
        summary = "Список заявок:\n\n"
        for order in orders:
            summary += f"Заявка #{order['id']}\n"
            summary += f"📦 Товар: {order['product']['name']}\n"
            summary += f"📍 Адрес: {order['address']['city']}, {order['address']['street']} {order['address']['house']}\n"
            summary += f"👤 Клиент: {order['client']['first_name']} {order['client']['last_name']}\n"
            summary += "\n"
    else:
        summary = "Вам пока еще не поступали заявки :("
    return summary
