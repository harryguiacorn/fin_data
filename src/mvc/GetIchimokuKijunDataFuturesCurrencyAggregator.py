from src.mvc.DataKijunSignalAggregatorMVC import Control, Model, View


def main(fetch1HData=False, fetchDailyData=True, fetchWeeklyData=False):
    if fetch1HData:
        _model = Model(
            "data/futurescurrency/d/", "asset_list/FuturesCurrency-kijun-1H.csv", True
        )
        _control = Control(_model, View())
        _control.main()
    if fetchDailyData:
        _model = Model(
            "data/futurescurrency/d/",
            "asset_list/FuturesCurrency.csv",
            "output/",
            "FuturesCurrency-kijun-D",
        )
        _control = Control(_model, View())
        _control.main()
    if fetchWeeklyData:
        _model = Model(
            "data/futurescurrency/w/",
            "asset_list/FuturesCurrency.csv",
            "output/",
            "FuturesCurrency-kijun-W",
        )
        _control = Control(_model, View())
        _control.main()


if __name__ == "__main__":
    main()