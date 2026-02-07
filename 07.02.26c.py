#1
'''
import sys
sys.setrecursionlimit(100000)
from functools import lru_cache
@lru_cache(maxsize=None)
'''
import asyncio

from pip._internal.utils import urls

'''
def hanoi(n, sourse, auxiliary, target, moves = []):
    if n == 1:
        moves.append(f"переместить диск 1 с {sourse} на {target}")
        return moves
    hanoi(n - 1, sourse, auxiliary, target, moves)
    moves.append(f"переместить дсик {n} с {sourse} на {target}")
    hanoi(n-1, auxiliary, auxiliary, target, moves)

moves = hanoi(3, 'a', 'b', 'c')
for i in moves:
    print(i)
print(f'всего ходов {len(moves)}')
'''

#синхрон
'''
def a():
    print('hello')
    
a()
print('world')
'''

#процессы (ресурсы, файлы, соединения, память) -> queue []
#потоки - > (ресурсы от процессы / быстрее создаются и переключаются/ могут обмениваться данными)

#важность процессов - >
# сварить макароны - 4 минуты
# пожарить мясо - 4 минуты
#8 ммнут

#варить макароны - 2 мнуты
# пожарить мясо в течение макарон -> (3 мин)
# параллелизм
# 2 мин - > ядра процессора

# конкурентность
#asyncio -
'''
import asyncio
#async for async with
async def f(n):
    print('hello')
    await asyncio.sleep(1)
    print('world')
    
asyncio.run("имя функции")
'''
'''
def sync_f():
    return 'result'

async def async_f():
    data = [1, 2, 3]
    print(sum(data))
    return 'result'

#print(sync_f())
#print(async_f())
asyncio.run()
'''
'''
async def one(num):
    print("f_1 start")
    await asyncio.sleep(num)
    print("f_1 end")

async def two(num):
    print("f_2 start")
    await asyncio.sleep(num)
    print("f_2 end")

async def main():
    result = await asyncio.gather(one(10), two(1))
   # task1 = asyncio.create_task(two())
   # task2 = asyncio.create_task(one())
    while True:
        await asyncio.sleep(2)
        if task1.cancelled():
          print("hello")
    result = await task1
    result = await task2
asyncio.run(
    main())
    '''




'''
async def download_page(url):
    print(f"загружаю{url}")
    await asyncio.sleep(10)
    return f"содержимое {url}"
async def main():
    urls = [
        "https://www.python.org/about/",
        "https://www.python.org/about/",
        "https://www.python.org/about/",
        "https://www.python.org/about/",
    ]
task = asyncio.create_task(download_page(urls[0]))
await asyncio.gather(task)
pages = await asyncio.gather(*[download_page(url) for url in urls])
print(f"агружено {len(pages)} страниц")
for content in pages:
    print(content)
asyncio.run(main())
'''

'''
async def make_coffee():
    print("загружаю")
    await asyncio.sleep(2)
    print("первое готово")

async def make_toast():
    print("загружаю")
    await asyncio.sleep(2)
    print(" второе готово")
from time import time
time()
async def main():
    start = time()
    await make_coffee()
    await make_toast()
    print(time() - start)
asyncio.run(main())
'''