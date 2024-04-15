import asyncio
import time

async def transform():
    print(f"inicou transformação ás: {time.strftime('%X')}")
    await asyncio.sleep(2)
    print(f"finalizou transformação ás: {time.strftime('%X')}")
    

async def extract():
    print(f"iniciou extracao ás: {time.strftime('%X')}")
    transformacao_task = asyncio.create_task(transform())
    ## Sem o await a função transform() é chamada mas não espera que ela termine para concluir a extração
    await transformacao_task
    print(f"finalizou extracao ás: {time.strftime('%X')}")
    
asyncio.run(extract())


################################################################################################################################################################

import asyncio

async def async_function():
    print("Iniciando operação assíncrona...")
    await asyncio.sleep(2)  # Simula uma operação assíncrona, como uma requisição de rede
    print("Operação assíncrona concluída!")

async def main():
    print("Chamando função assíncrona...")
    await async_function()
    print("Programa finalizado.")

# Executa o loop de evento asyncio
asyncio.run(main())

################################################################################################################################################################

import asyncio
import time

async def async_function(num):
    print(f"{time.strftime('%X')} Iniciando operação assíncrona {num}...")
    await asyncio.sleep(num)  # Simula uma operação assíncrona, como uma requisição de rede
    print(f"Operação assíncrona {num} concluída!")

async def main():
    tasks = []
    for i in range(1, 4):
        tasks.append(asyncio.create_task(async_function(i)))
    
    print("Tarefas assíncronas iniciadas.")
    await asyncio.gather(*tasks)
    print("Todas as tarefas assíncronas concluídas.")

# Executa o loop de evento asyncio
asyncio.run(main())

################################################################################################################################################################
