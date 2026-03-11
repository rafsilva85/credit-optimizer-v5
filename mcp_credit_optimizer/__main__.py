"""Allow running as python -m mcp_credit_optimizer"""
from .server import mcp

if __name__ == "__main__":
    mcp.run()
