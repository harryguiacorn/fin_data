import pandas as pd
from abc import abstractclassmethod, ABC


class DataOHLC(ABC):
    @abstractclassmethod
    def readLocalCsvData(self, symbols, __csvPath):
        pass


class DataCloudSignal(DataOHLC):
    def __init__(self, __symbol, __csvPath, __use_datetime_format=False):
        self.symbol = __symbol
        self.csvPath = __csvPath
        self.use_datetime_format = __use_datetime_format

    def setupPd_use_datetime_format(
        self, csvSuffix="_cloud.csv", folderPath="data/"
    ):
        # pd.set_option("display.max_rows", None)  # print every row for debug
        # pd.set_option(
        #     "display.max_columns", None
        # )  # print every column for debug

        # print(
        #     "------- setupPd_use_datetime_format csvSuffix -------", csvSuffix
        # )

        try:
            __path = self.csvPath + self.symbol + csvSuffix
            __data = pd.read_csv(__path)

            # print(
            #     "---------- setupPd_use_datetime_format -------------", __path
            # )

            if __data.empty:  # Check if the DataFrame is empty
                print("CSV file is empty", __path)
            else:
                # print(__path, __data.Datetime)
                __data.index = __data.Datetime
                __data["Cloud Signal"] = self.getCloudDirection(
                    __data["Close"],
                    __data["senkou_span_a"],
                    __data["senkou_span_b"],
                )
                __data["Cloud Signal Count"] = self.getCloudSignalCount(
                    __data["Cloud Signal"]
                )
                __data["Return"] = self.getReturn(
                    __data["Close"], __data["Cloud Signal"]
                ).round(4)
                __data["Cumulative Return"] = (
                    (1 + __data["Return"]).cumprod() - 1
                ).round(4)

                # drop chikou_span because it creates na values
                # for 26 periods from last date
                __data.drop("chikou_span", axis=1, inplace=True)
                __data = __data.dropna()

                # convert float64 to int64
                __data["Cloud Signal"] = __data["Cloud Signal"].astype("int64")
                __data["Cloud Signal Count"] = __data[
                    "Cloud Signal Count"
                ].astype("int64")

                self.setColumnsSaveCsv_use_datetime_format(__data)
                # print(__data)
        except pd.errors.EmptyDataError:
            print("CSV file is empty", __path)
        except FileNotFoundError:
            print(f"Error: {__path} not found")

    def setupPd(self, csvSuffix="_cloud.csv", folderPath="data/"):
        # pd.set_option("display.max_rows", None)  # print every row for debug
        # pd.set_option(
        #     "display.max_columns", None
        # )  # print every column for debug

        # print("------- setupPd csvSuffix -------", csvSuffix)

        try:
            __path = self.csvPath + self.symbol + csvSuffix
            __data = pd.read_csv(__path)
            # print("---------- setupPd -------------", __path)
            if __data.empty:  # Check if the DataFrame is empty
                print("CSV file is empty: ", __path)
            else:
                # print(__data.Date)
                __data.index = __data.Date
                __data["Cloud Signal"] = self.getCloudDirection(
                    __data["Close"],
                    __data["senkou_span_a"],
                    __data["senkou_span_b"],
                )
                __data["Cloud Signal Count"] = self.getCloudSignalCount(
                    __data["Cloud Signal"]
                )

                # __data["Return"] = self.getReturn(
                #     __data["Close"], __data["Cloud Signal"]
                # )
                # __data["Cumulative Return"] = (
                #     1 + __data["Return"]
                # ).cumprod() - 1

                # drop chikou_span because it creates na values for
                # 26 periods from last date
                __data.drop("chikou_span", axis=1, inplace=True)
                __data = __data.dropna()

                # convert float64 to int64
                __data["Cloud Signal"] = __data["Cloud Signal"].astype("int64")
                __data["Cloud Signal Count"] = __data[
                    "Cloud Signal Count"
                ].astype("int64")

                self.setColumnsSaveCsv(__data)
        except pd.errors.EmptyDataError:
            print("CSV file is empty: ", __path)
        except FileNotFoundError:
            print(f"Error: {__path} not found")

    def addPercentageSuffix(self, __series: pd.DataFrame):
        return (__series * 100).round(2).astype(str) + "%"

    def getReturn(
        self, __curClose: pd.DataFrame, __signal: int
    ) -> pd.DataFrame:
        pct_change = __curClose.pct_change().round(4) * __signal.shift(1)
        pct_change = pct_change
        # print(__curClose.pct_change())
        return pct_change

    def getCloudSignalCount(self, __cloudDirectionList):
        __newList = []
        __cloudDirectionCount = None
        __curCloudDirection = None
        for __i in range(len(__cloudDirectionList)):
            if pd.isna(__cloudDirectionList.iloc[__i]):
                __cloudDirectionCount = __cloudDirectionList.iloc[__i]
            elif __curCloudDirection is None:
                __curCloudDirection = __cloudDirectionList.iloc[__i]
                __cloudDirectionCount = 1
            elif not __cloudDirectionList.iloc[__i] == __curCloudDirection:
                __curCloudDirection = __cloudDirectionList.iloc[__i]
                __cloudDirectionCount = 1
            else:
                __cloudDirectionCount += 1

            __newList.append(__cloudDirectionCount)
        return __newList

    def getCloudDirection(self, __close, __senkou_span_a, __senkou_span_b):
        __data = []
        __curDirection = None
        # print(__senkou_span_a)
        for __i in range(len(__senkou_span_b)):
            if pd.isna(__senkou_span_b.iloc[__i]):
                # pass alone senkou span b NaN back to column
                __data.append(__senkou_span_b.iloc[__i])
            elif pd.isna(__senkou_span_a.iloc[__i]):
                __data.append(__senkou_span_b.iloc[__i])
            elif (
                # Close is above the cloud
                __close.iloc[__i] > __senkou_span_a.iloc[__i]
                and __close.iloc[__i] > __senkou_span_b.iloc[__i]
            ):
                __curDirection = 1
                __data.append(__curDirection)
            elif (
                # Close is below the cloud
                __close.iloc[__i] < __senkou_span_a.iloc[__i]
                and __close.iloc[__i] < __senkou_span_b.iloc[__i]
            ):
                __curDirection = -1
                __data.append(__curDirection)
            else:
                # Close is within cloud
                __curDirection = 0
                __data.append(__curDirection)
        # print(__data)
        return __data

    def setColumnsSaveCsv(
        self, __data: pd.DataFrame, csvSuffix="_cloudCount.csv"
    ):
        header = [
            "Date",
            "Close",
            "Cloud Signal",
            "Cloud Signal Count",
            # "Return",
            # "Cumulative Return",
            # "Current Return",
        ]
        __data.to_csv(
            self.csvPath + self.symbol + csvSuffix, columns=header, index=False
        )

    def setColumnsSaveCsv_use_datetime_format(
        self, __data, csvSuffix="_cloudCount.csv"
    ):
        header = [
            "Datetime",
            "Cloud Signal",
            "Cloud Signal Count",
            # "Return",
            # "Cumulative Return",
            # "Current Return",
        ]
        __data.to_csv(
            self.csvPath + self.symbol + csvSuffix, columns=header, index=False
        )

    def readLocalCsvData(self, symbols, __csvPath):
        pass

    def main(self):
        # print(
        #     "----------- main::use_datetime_format------------",
        #     self.use_datetime_format,
        # )
        if self.use_datetime_format is False:
            self.setupPd(
                "_ichimokuTapy.csv"
            )  # _ichimokuPlotly _ichimokuTapy _ichimokuFinta
        else:
            self.setupPd_use_datetime_format(
                "_ichimokuTapy.csv"
            )  # _ichimokuPlotly _ichimokuTapy _ichimokuFinta


class Model(object):
    def __init__(
        self, __csvPath, __assetListPath, __use_datetime_format=False
    ):
        self.csvPath = __csvPath
        self.assetListPath = __assetListPath
        self.use_datetime_format = __use_datetime_format
        self.symbols = None
        self.dataOHLC = None

    @property
    def use_datetime_format(self):
        return self.__use_datetime_format

    @use_datetime_format.setter
    def use_datetime_format(self, __use_datetime_format):
        self.__use_datetime_format = __use_datetime_format

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, __symbol):
        self.__symbol = __symbol

    @property
    def csvPath(self):
        return self.__csvPath

    @csvPath.setter
    def csvPath(self, __csvPath):
        self.__csvPath = __csvPath

    @property
    def assetListPath(self):
        return self.__assetListPath

    @assetListPath.setter
    def assetListPath(self, __assetListPath):
        self.__assetListPath = __assetListPath

    def readAssetList(self, __csvPath, __colName="symbol"):
        df = pd.read_csv(__csvPath)
        # print("------ readAssetList --------", df.to_string())
        l_symbol = df[__colName].tolist()
        self.symbols = l_symbol
        return l_symbol

    def readLocalCsvData(self, symbols, __csvPath):
        __dict_df = {}
        for __symbol in symbols:
            try:
                __filePath = __csvPath + __symbol + ".csv"
                __df = pd.read_csv(__filePath)
                __dict_df[__symbol] = __df
            except FileNotFoundError:
                print(f"Error: {__filePath} not found")
                continue
        # print("------------ readLocalCsvData ----------", __dict_df)
        return __dict_df

    def getBatchLocalData(self):
        self.dataOHLC = self.readLocalCsvData(self.symbols, self.csvPath)

    def getIndividualSymbolData(self):
        for __symbol, __value in self.dataOHLC.items():
            # print("getIndividualSymbolData:", __symbol, self.csvPath, end=", ")
            dataP = DataCloudSignal(
                __symbol, self.csvPath, self.use_datetime_format
            )
            dataP.main()
        print("Cloud signal count csv files are created\n")


class Control(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def getAssetList(self):
        self.model.readAssetList(self.model.assetListPath)

    def showAssetList(self):
        __dict_symbols = self.model.readAssetList(self.model.assetListPath)
        self.view.showAssetList(__dict_symbols)

    def getDataOHLC(self):
        self.model.getDataOHLC()

    def getBatchLocalData(self):
        self.model.getBatchLocalData()

    def getIndividualSymbolData(self):
        self.model.getIndividualSymbolData()

    def main(self):
        print(
            f"----------- Generating Cloud Signals: {self.model.csvPath} -----------"
        )
        self.getAssetList()
        # print("----------- Generating Cloud Signals getBatchLocalData-----------")
        self.getBatchLocalData()
        # print("----------- Generating Cloud Signals getIndividualSymbolData-----------")
        self.getIndividualSymbolData()


class View(object):
    def __init__(self):
        pass


if __name__ == "__main__":
    _model = Model("data/futurescurrency/w/", "asset_list/FuturesCurrency.csv")
    _control = Control(_model, View())
    _control.main()
