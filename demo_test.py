import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run():
    server_params = StdioServerParameters(command="python", args=["weather_Israel.py"])
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("--- מריץ הדגמת כלים ---")
            await session.call_tool("open_weather_forecast_israel")
            await session.call_tool("enter_weather_forecast_city_israel", arguments={"city_name": "ירושלים"})
            await session.call_tool("select_weather_forecast_city_israel")
            result = await session.call_tool("get_weather_forecast_data_israel")
            print("\nתחזית ירושלים שנשלפה מהדפדפן:")
            print(result)

if __name__ == "__main__":
    asyncio.run(run())