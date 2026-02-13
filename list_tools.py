import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run():
    server_params = StdioServerParameters(
        command=r"C:\Python314\Scripts\notebooklm-mcp.exe",
        args=[],
        env=None
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(f"Total tools: {len(tools.tools)}")
            
            print("Listing notebooks...")
            try:
                result = await session.call_tool("notebook_list", {})
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error calling notebook_list: {e}")

if __name__ == "__main__":
    asyncio.run(run())
