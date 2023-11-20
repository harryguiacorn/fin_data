from src.mvc.DataTKxSignalAggregatorMVC import Control, Model, View


def main(
    fetch1HData=False,
    fetchDailyData=True,
    fetchWeeklyData=False,
    fetchMonthlyData=False,
):
    if fetch1HData:
        _model = Model(
            "data/futures/1h/",
            "asset_list/Futures.csv",
            "output/",
            "Futures-tkx-1H",
            True,
        )
        _control = Control(_model, View())
        _control.main()
    if fetchDailyData:
        _model = Model(
            "data/futures/d/",
            "asset_list/Futures.csv",
            "output/",
            "Futures-tkx-D",
        )
        _control = Control(_model, View())
        _control.main()
    if fetchWeeklyData:
        _model = Model(
            "data/futures/w/",
            "asset_list/Futures.csv",
            "output/",
            "Futures-tkx-W",
        )
        _control = Control(_model, View())
        _control.main()
    if fetchMonthlyData:
        _model = Model(
            "data/futures/m/",
            "asset_list/Futures.csv",
            "output/",
            "Futures-tkx-M",
        )
        _control = Control(_model, View())
        _control.main()


if __name__ == "__main__":
    main()
