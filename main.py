import runDJ30, runNas100, runFTSE100, runFTSE250, runFutures, runCurrencyFutures, runSPX500

fetch_symbols_latest_DJ30 = True
fetch_symbols_latest_SPX500 = True
fetch_symbols_latest_Nas100 = True
fetch_symbols_latest_FTSE100 = True
fetch_symbols_latest_FTSE250 = True
fetch_symbols_latest_Futures = True
fetch_symbols_latest_CurrencyFutures = True

fetch_DJ30_1H = True
fetch_SPX500_1H = True
fetch_Nas100_1H = True
fetch_FTSE100_1H = True
fetch_FTSE250_1H = True
fetch_Futures_1H = True
fetch_CurrencyFutures_1H = True

fetch_DJ30_D = True
fetch_SPX500_D = True
fetch_Nas100_D = True
fetch_FTSE100_D = True
fetch_FTSE250_D = True
fetch_Futures_D = True
fetch_CurrencyFutures_D = True

fetch_DJ30_W = True
fetch_SPX500_W = True
fetch_Nas100_W = True
fetch_FTSE100_W = True
fetch_FTSE250_W = True
fetch_Futures_W = True
fetch_CurrencyFutures_W = True

fetch_DJ30_M = True
fetch_SPX500_M = True
fetch_Nas100_M = True
fetch_FTSE100_M = True
fetch_FTSE250_M = True
fetch_Futures_M = True
fetch_CurrencyFutures_M = True

run_Multi_TimeFrame_Merger_DJ30 = True
run_Multi_TimeFrame_Merger_SPX500 = True
run_Multi_TimeFrame_Merger_Nas100 = True
run_Multi_TimeFrame_Merger_FTSE100 = True
run_Multi_TimeFrame_Merger_FTSE250 = True
run_Multi_TimeFrame_Merger_Futures = True
run_Multi_TimeFrame_Merger_CurrencyFutures = True

fetch_kijun_analysis = False

# Use "Datetime" for Yahoo intraday data,
# "Date" for D, W, M data.
# Use "Datetime" for all Oanda data.
fetch_Kicker_use_datetime_format = False


def main():
    # Stop script being auto-run by Replit or Gitpod
    # return

    # ---------------- Dow Jones 30 ----------------

    _runDJ30 = runDJ30
    _runDJ30.main(
        fetch_symbols_latest_DJ30,
        fetch_DJ30_1H,
        fetch_DJ30_D,
        fetch_DJ30_W,
        fetch_DJ30_M,
        fetch_kijun_analysis,
        fetch_Kicker_use_datetime_format,
        run_Multi_TimeFrame_Merger_DJ30,
    )

    # ---------------- Nasdaq 100 ----------------

    _runNas100 = runNas100
    _runNas100.main(
        fetch_symbols_latest_Nas100,
        fetch_Nas100_1H,
        fetch_Nas100_D,
        fetch_Nas100_W,
        fetch_Nas100_M,
        fetch_kijun_analysis,
        fetch_Kicker_use_datetime_format,
        run_Multi_TimeFrame_Merger_Nas100,
    )

    # ---------------- FTSE 100 ----------------

    _runFTSE100 = runFTSE100
    _runFTSE100.main(
        fetch_symbols_latest_FTSE100,
        fetch_FTSE100_1H,
        fetch_FTSE100_D,
        fetch_FTSE100_W,
        fetch_FTSE100_M,
        fetch_Kicker_use_datetime_format,
        run_Multi_TimeFrame_Merger_FTSE100,
    )

    # ---------------- FTSE 250 ----------------

    _runFTSE250 = runFTSE250
    _runFTSE250.main(
        fetch_symbols_latest_FTSE250,
        fetch_FTSE250_1H,
        fetch_FTSE250_D,
        fetch_FTSE250_W,
        fetch_FTSE250_M,
        fetch_Kicker_use_datetime_format,
        run_Multi_TimeFrame_Merger_FTSE250,
    )

    # ---------------- Futures ----------------

    _runFutures = runFutures
    _runFutures.main(
        fetch_symbols_latest_Futures,
        fetch_Futures_1H,
        fetch_Futures_D,
        fetch_Futures_W,
        fetch_Futures_M,
        fetch_Kicker_use_datetime_format,
        run_Multi_TimeFrame_Merger_Futures,
    )

    # ---------------- Futures Currency ----------------

    _runCurrencyFutures = runCurrencyFutures
    _runCurrencyFutures.main(
        fetch_symbols_latest_CurrencyFutures,
        fetch_CurrencyFutures_1H,
        fetch_CurrencyFutures_D,
        fetch_CurrencyFutures_W,
        fetch_CurrencyFutures_M,
        fetch_Kicker_use_datetime_format,
        run_Multi_TimeFrame_Merger_CurrencyFutures,
    )

    # ---------------- S&P 500 ----------------

    _runSPX500 = runSPX500
    _runSPX500.main(
        fetch_SPX500_1H,
        fetch_SPX500_D,
        fetch_SPX500_W,
        fetch_SPX500_M,
        fetch_Kicker_use_datetime_format,
        run_Multi_TimeFrame_Merger_SPX500,
    )

    print("\nTasks completed.")


if __name__ == "__main__":
    main()
