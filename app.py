import asyncio

from jutsu import JutSu, get_link_and_download


async def main():
    slug = input("Отправь ссылку или имя(для вставки ctrl+v): ")

    if slug.startswith("http"):
        slug = slug.split("/")[3]

    res = input("Выбери разрешение(1080, 720, 480, 360): ")

    download_type = "1"

    if res not in ("1080", "720", "480", "360"):
        return print("Выбери правильноек разрешение")

    jutsu = JutSu(slug)

    episodes = await jutsu.get_all_episodes()

    if download_type == "1":
        for episode in episodes:
            await get_link_and_download(jutsu, episode, res)

    # elif download_type == "2":
    #     coros = [
    #         asyncio.create_task(get_link_and_download(jutsu, episode, res))
    #         for episode in episodes
    #     ]
    #     await asyncio.gather(*coros)

    else:
        print(":/")

    await jutsu.close()


if __name__ == "__main__":
    asyncio.run(main())
