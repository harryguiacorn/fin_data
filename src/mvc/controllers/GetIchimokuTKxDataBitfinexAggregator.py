from src.mvc.core.DataTKxSignalAggregatorMVC import Control, Model, View


def main(
    fetch1HData=False,
    fetch4HData=False,
    fetchDailyData=True,
    fetchWeeklyData=False,
    fetchMonthlyData=False,
):
    if fetch1HData:
        _model = Model(
            "data/bitfinex/1h/",
            "asset_list/Bitfinex.csv",
            "output/tkx/",
            "bitfinex-tkx-1H",
            "1H",
            True,
        )
        _control = Control(_model, View())
        _control.main()
    if fetch4HData:
        _model = Model(
            "data/bitfinex/4h/",
            "asset_list/Bitfinex.csv",
            "output/tkx/",
            "bitfinex-tkx-4H",
            "4H",
            True,
        )
        _control = Control(_model, View())
        _control.main()
    if fetchDailyData:
        _model = Model(
            "data/bitfinex/d/",
            "asset_list/Bitfinex.csv",
            "output/tkx/",
            "bitfinex-tkx-D",
            "1D",
            True,
        )
        _control = Control(_model, View())
        _control.main()
    if fetchWeeklyData:
        _model = Model(
            "data/bitfinex/w/",
            "asset_list/Bitfinex.csv",
            "output/tkx/",
            "bitfinex-tkx-W",
            "1W",
            True,
        )
        _control = Control(_model, View())
        _control.main()
    if fetchMonthlyData:
        _model = Model(
            "data/bitfinex/m/",
            "asset_list/Bitfinex.csv",
            "output/tkx/",
            "bitfinex-tkx-M",
            "1M",
            True,
        )
        _control = Control(_model, View())
        _control.main()


if __name__ == "__main__":
    main()
