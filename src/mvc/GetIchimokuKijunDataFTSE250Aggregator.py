from src.mvc.DataKijunSignalAggregatorMVC import Control, Model, View


def main(fetch1HData=False, fetchDailyData=True, fetchWeeklyData=False):
    if fetch1HData:
        _model = Model(
            "data/ftse250/1h/",
            "asset_list/FTSE250.csv",
            "output/",
            "FTSE250-kijun-1H",
            True,
        )
        _control = Control(_model, View())
        _control.main()
    if fetchDailyData:
        _model = Model(
            "data/ftse250/d/",
            "asset_list/FTSE250.csv",
            "output/",
            "FTSE250-kijun-D",
        )
        _control = Control(_model, View())
        _control.main()
    if fetchWeeklyData:
        _model = Model(
            "data/ftse250/w/",
            "asset_list/FTSE250.csv",
            "output/",
            "FTSE250-kijun-W",
        )
        _control = Control(_model, View())
        _control.main()


if __name__ == "__main__":
    main()
