from workers import Response


async def on_fetch(request, env):
    return Response("hello world in python")
