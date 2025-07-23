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

# python -m asyncio ps PID
# python -m asyncio pstree PID
