#1
'''
import asyncio
import time


async def calculate(x, delay):
    await asyncio.sleep(delay)
    result = x * x
    print(f"Вычислено: {x}^2 через {delay} сек. = {result}")
    return result


async def main():
    start_time = time.time()


    tasks = [
        calculate(2, 1),
        calculate(3, 2),
        calculate(4, 1)
    ]


    print("Запуск параллельных вычислений...")
    results = await asyncio.gather(*tasks)

    end_time = time.time()

    print("\nИтоговые результаты ")
    print(f"Список результатов: {results}")
    print(f"Общее время выполнения: {end_time - start_time:} секунд")
asyncio.run(main())
'''

#2
'''
import asyncio
async def long_task():
    print("Начинаю долгую загрузку на пять минут...")
    await asyncio.sleep(5)
    print("Задача выполнена !")
   # except asyncio.CancelledError:
   # print("Отмена задачи") #не получается отменить 

async def main():
    task = asyncio.create_task(long_task())
    print("жду 2 сеунды ...")
    await asyncio.sleep(2)

    print(" Время вышло, отменяю задачу...")
    task.cancel()
    await task
    #except syncio.Cancelled:
    #print(" задача была успешно отменена.") # тут тоже
asyncio.run(main())
'''

#3
'''
import asyncio
import time


async def fetch_data(api_name, delay):
    print(f"[{api_name}] запрос, задержка: {delay} сек")
    await asyncio.sleep(delay)
    result = f"Данные из {api_name}"
    print(f"[{api_name}] Запрос завершен")
    return result
async def main():
    start_time = time.time()
    requests = [
        ("API_A", 1),  
        ("API_B", 2), 
        ("API_C", 1.5), 
        ("API_D", 0.5)  
    ]
    awaitab = [fetch_data(api_name, delay) for api_name, delay in requests]
    print("Запуск всех запросов...")
    all_results = await asyncio.gather(*awaitab)
    end_time = time.time()
    print("\nВсе запросы завершены ")
    print("Полученные результаты:")
    for result_item in all_results:
        print(f"{result_item}")
    print(f"\nОбщее время выполнения: {end_time - start_time:.} секунд")
    asyncio.run(main())
'''
#не выводится почему-то