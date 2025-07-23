import asyncio


async def play(track):
    await asyncio.sleep(300)
    print(f"🎵 Finished: {track}")


async def album(name, tracks):
    async with asyncio.TaskGroup() as tg:
        for track in tracks:
            tg.create_task(play(track), name=track)


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(album("Sundowning", ["TNDNBTG", "Levitate"]), name="Sundowning")
        tg.create_task(album("TMBTE", ["DYWTYLM", "Aqua Regia"]), name="TMBTE")


if __name__ == "__main__":
    asyncio.run(main())

# python3.14 _05_asyncio_introspection.py &
# python3.14 -m asyncio ps PID
# python3.14 -m asyncio pstree PID
# docker run -it --rm -v $(pwd):/data  python:3.14-rc-bookworm bash
