import pandas as pd
from src.mvc import Util


class Model(object):
    def __init__(
        self,
        __outputPathList: str = "",
        __outputMergePath: str = "",
        __list_direction_count_names: list = [],
        __list_score_names: list = [],
    ) -> None:
        self.outputPathList = __outputPathList
        self.outputMergePath = __outputMergePath
        self.list_direction_count_names = __list_direction_count_names
        self.list_score_names = __list_score_names

    def merge(self) -> pd.DataFrame:
        print(
            "\n------------- Merging Multi Timeframe Cloud and TKx Sum -------------"
        )

        list_pd = self.outputPathList

        print("Check files for merging: ", list_pd)

        # check to see if files exist before parsing to Pandas
        list_pd_exist = iter([x for x in list_pd if Util.file_exists(x)])

        # print(list_pd_exist)
        combined_csv = pd.DataFrame()

        for x in list_pd_exist:
            # print("path", x)
            df_csv1 = pd.read_csv(x)
            # Drop the "Date" column
            if "Date" in df_csv1.columns:
                df_csv1 = df_csv1.drop(columns=["Date"])
            elif "Datetime" in df_csv1.columns:
                df_csv1 = df_csv1.drop(columns=["Datetime"])

            if combined_csv.empty:
                combined_csv = df_csv1
            else:
                # Combine the two dataframes
                combined_csv = pd.merge(
                    combined_csv, df_csv1, on=["Symbol", "Name"]
                )

        print(
            "Multi Timeframe Cloud and TKx Signals Merged",
            end="\n\n",
        )

        # print(combined_csv)

        return combined_csv

    def exportResult(self, list_result):
        df_result = pd.DataFrame(list_result, columns=self.getColumns())

        Util.create_folder(self.outputPath)
        df_result.to_csv(
            self.outputPath + self.assetClassName.replace(" ", "") + ".csv",
            index=False,
        )
        self.resultDataFrame = df_result
        return df_result

    def saveData(self, __df: pd.DataFrame) -> pd.DataFrame:
        if self.list_score_names[0] in __df:
            __df.sort_values(
                by=[self.list_score_names[0]], ascending=False, inplace=True
            )
        # print("------ Cleaning columns ------")

        __df.to_csv(
            f"{self.outputMergePath}",
            # columns=__filter_list_column,
            index=False,
        )

        __df.to_html(f"{self.outputMergePath}.html", index=False)

        print(
            f"Saved data to: {self.outputMergePath} {self.outputMergePath}.html\n"
        )
        print(
            "----------- Cloud and TKx Sum Score Multi Timeframe Final View -----------\n",
            __df,
        )
        return __df

    def create_sum_column(self, df: pd.DataFrame):
        # print(
        #     "\ncreate_sum_column self.list_direction_count_names: ",
        #     self.list_direction_count_names,
        #     "\ncreate_sum_column self.list_score_names: ",
        #     self.list_score_names,
        #     "\ncreate_sum_column df.columns",
        #     df.columns,
        # )

        __sum = 0
        for __name in self.list_direction_count_names:
            if __name in df.columns:
                __sum += df[__name]
                # print(__name, __sum)
        df[self.list_score_names[0]] = __sum

        # print("create_sum_column df\n", df)
        return df


class Control(object):
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def main(self):
        df = self.merge()
        self.create_sum_column(df)

        self.saveData(df)

    def merge(self):
        return self.model.merge()

    def create_sum_column(self, df):
        return self.model.create_sum_column(df)

    def saveData(self, df):
        self.model.saveData(df)


class View(object):
    def __init__(self) -> None:
        pass

    pass


if __name__ == "__main__":
    _model = Model(
        [
            "output/Oanda-cloud-merged.csv",
            "output/Oanda-tkx-merged.csv",
        ],
        "output/Oanda-sum-cloud-tkx-merged.csv",
        [
            "Cloud Score Sum",
            "TKx Score Sum",
        ],
        [
            "Total Score Sum",
        ],
    )
    _control = Control(_model, View())
    _control.main()
