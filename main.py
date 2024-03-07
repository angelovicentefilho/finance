import yfinance as yf


def sample():
    gol_df = yf.download("GOLL4.SA", start="2020-01-01", end="2023-01-01")["Adj Close"]
    print(gol_df)


if __name__ == "__main__":
    sample()
