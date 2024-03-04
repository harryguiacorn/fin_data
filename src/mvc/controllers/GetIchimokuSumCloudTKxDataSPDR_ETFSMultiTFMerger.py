from src.mvc.core.DataSumCloudTKxSignalMultiTimeframeMerger import (
    Control,
    Model,
    View,
)


def main(run_merger=True):
    if run_merger:
        _model = Model(
            [
                "output/cloud/SPDR_ETFS-cloud-merged.csv",
                "output/tkx/SPDR_ETFS-tkx-merged.csv",
            ],
            "output/sum/SPDR_ETFS-sum-cloud-tkx-merged.csv",
            [
                "Cloud Score Sum",
                "TKx Score Sum",
            ],
            [
                "Total Score Sum",
            ],
            "All Sector SPDR ETFs Cloud Scan",
        )
        _control = Control(_model, View())
        _control.main()


if __name__ == "__main__":
    main()
