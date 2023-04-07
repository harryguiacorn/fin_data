from src.mvc.DataKickerSignalAggregatorMVC import Control, Model, View


def main(
    fetch1HData=True,
    fetchDailyData=True,
    fetchWeeklyData=False,
    fetchMonthlyData=False,
):
    if fetch1HData:
        _model = Model(
            "data/futurescurrency/1h/",
            "asset_list/FuturesCurrency.csv",
            "output/",
            "FuturesCurrency-1H",
        )
        _control = Control(_model, View())
        _control.main()
    if fetchDailyData:
        _model = Model(
            "data/futurescurrency/d/",
            "asset_list/FuturesCurrency.csv",
            "output/",
            "FuturesCurrency-D",
        )
        _control = Control(_model, View())
        _control.main()
    if fetchWeeklyData:
        _model = Model(
            "data/futurescurrency/w/",
            "asset_list/FuturesCurrency.csv",
            "output/",
            "FuturesCurrency-W",
        )
        _control = Control(_model, View())
        _control.main()


if __name__ == "__main__":
    main()
