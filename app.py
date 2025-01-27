import asyncio
from pydantic_ai import Agent
from pydantic import BaseModel
import yfinance as yf
import gradio as gr


class StockPriceResult(BaseModel):
    symbol: str
    price: float
    currency: str = "USD"
    low_price: float
    high_price: float
    volume: int
    sentiment: str
    message: str


class SectorResult(BaseModel):
    sector_name: str
    growth_rate: float
    revenue: float
    key_statistics: str
    companies: list[str]


stock_info_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    result_type=StockPriceResult,
    system_prompt="You are a helpful financial assistant that can look up stock prices. Use the get_stock_info_async tool to fetch current financial information from the stock.",
)

sector_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    result_type=SectorResult,
    system_prompt="You are a helpful financial assistant that can analyze the sector of the stock picked. Use the get_sector_info tool to fetch current financial information from the stock.",
)


@sector_agent.tool_plain
async def get_sector_info(query):
    try:
        result = await sector_agent.run(query)
        print(f"SECTOR DATA: {result.data}")
        sector = yf.Sector(result.data.sector_name)
        response = f"Sector Information for {sector}\n"
        response += f" Sector: ${result.data.key_statistics}\n"
        response += f" Growth Rate: ${result.data.growth_rate}\n"
        response += f" Revenue: ${result.data.revenue}\n"
        response += f" Sector Companies: ${result.data.companies}\n"
        return response
    except Exception as e:
        return f"Error: {str(e)}"


@stock_info_agent.tool_plain
async def get_stock_info_async(query):
    try:
        result = await stock_info_agent.run(query)
        print(f"Stock DATA: {result.data}")
        symbol = result.data.symbol
        ticker = yf.Ticker(symbol)
        price = ticker.fast_info.last_price
        response = f" Price: ${price:.2f} {result.data.currency}\n"
        response += f" Low: ${result.data.low_price:.2f} {result.data.currency}\n"
        response += f" High: ${result.data.high_price:.2f} {result.data.currency}\n"
        response += f" Sentiment: ${result.data.sentiment}\n"
        response += f" Volume: {result.data.volume}\n"
        response += f"\n{result.data.message}"
        return response
    except Exception as e:
        return f"Error: {str(e)}"


async def get_stock_info(query):
    stock_info = await get_stock_info_async(query)
    sector_info = await get_sector_info(query)
    return stock_info + sector_info


demo = gr.Interface(
    fn=get_stock_info,
    inputs=gr.Textbox(
        label="Ask about any stock",
        placeholder="Tell me about Tesla?",
    ),
    outputs=gr.Textbox(label="Stock Information"),
    title="Stock Price AI Assistant",
    description="Ask me about any stock price and I'll fetch the latest information for you!",
)

if __name__ == "__main__":
    demo.launch()
