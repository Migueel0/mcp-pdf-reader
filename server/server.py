from mcp.server import FastMCP

server = FastMCP("pdf-reader")

@server.tool("read_pdf", description="Reads and extracts text from a PDF file.")
async def read_pdf(file_path: str) -> str:
    """Reads and extracts text from a PDF file.

    Args:
        file_path (str): The path to the PDF file."""
    
    ...


def main():
    server.run()

if __name__ == "__main__":
    main()