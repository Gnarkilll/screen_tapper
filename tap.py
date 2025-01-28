# import pyautogui
# import time
#
# print("Наведите мышь на нужное место. Координаты будут отображаться каждые 2 секунды.")
# try:
#     while True:
#         x, y = pyautogui.position()  # Получаем текущие координаты мыши
#         print(f"Текущие координаты: X={x}, Y={y}")
#         time.sleep(2)  # Задержка для обновления
# except KeyboardInterrupt:
#     print("Выход из программы.")

import pyautogui
import random
import time

def random_move_and_click(region, multi_clicks=False):
    """
    Выполняет случайное перемещение и клик внутри указанной области.
    :param region: Кортеж (x, y, ширина, высота) для области кликов.
    :param multi_clicks: Если True, выполняет несколько кликов в одной точке.
    """
    x_start, y_start, width, height = region

    # Генерация случайной точки внутри области
    x = random.randint(x_start, x_start + width)
    y = random.randint(y_start, y_start + height)

    # Перемещение мыши
    move_duration = random.uniform(0.1, 0.5)  # Ускоренное движение
    pyautogui.moveTo(x, y, duration=move_duration)

    if multi_clicks:
        # Выполнение нескольких кликов в одной точке
        num_clicks = random.randint(2, 5)  # Количество кликов
        for i in range(num_clicks):
            pyautogui.click()
            print(f"Клик #{i + 1} в точке: ({x}, {y})")
            time.sleep(random.uniform(0.05, 0.2))  # Минимальная задержка между кликами
    else:
        # Одиночный клик
        pyautogui.click()
        print(f"Клик выполнен в точке: ({x}, {y})")

    # Уменьшенная задержка после действия
    post_click_delay = random.uniform(0.1, 0.3)
    time.sleep(post_click_delay)


def random_scroll_chance():
    """
    Иногда выполняет случайную прокрутку вверх или вниз.
    """
    if random.random() < 0.1:  # 10% шанс прокрутки
        scroll_amount = random.randint(-100, 100)  # Меньший диапазон прокрутки
        pyautogui.scroll(scroll_amount)
        print(f"Прокрутка на {scroll_amount} пикселей")


def main():
    region = (383, 423, 937, 636)  # Область для кликов
    num_clicks = 500  # Увеличено количество кликов за один запуск

    print(f"Старт. Запланировано {num_clicks} кликов.")
    for i in range(num_clicks):
        print(f"Цикл {i + 1}/{num_clicks}")

        # Выполнение случайного перемещения и клика
        multi_click_chance = random.random() < 0.3  # 30% шанс на несколько кликов
        random_move_and_click(region, multi_clicks=multi_click_chance)

        # Возможная прокрутка
        random_scroll_chance()

        # Минимальная задержка между циклами
        delay = random.uniform(0.1, 0.5)  # Сокращённая пауза
        print(f"Задержка: {delay:.2f} секунд")
        time.sleep(delay)

    print("Автоматизация завершена.")


if __name__ == "__main__":
    main()


