import asyncio
from preloaded import send_request


async def request_manager(n: int) -> str:
    responses = []
    tasks = []
    sem = asyncio.Semaphore(150)

    async def fetch(sem, response):
        async with sem:
            response.append(await send_request())

    for i in range(n):
        response = []
        tasks.append(fetch(sem, response))
        responses.append(response)

    await asyncio.gather(*tasks)

    return ''.join([r[0] for r in responses])
