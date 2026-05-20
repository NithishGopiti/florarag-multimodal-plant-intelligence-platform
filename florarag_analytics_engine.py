import pandas as pd

def generate_analytics(records):

    dataframe = pd.DataFrame(records)

    analytics = dataframe.groupby(
        "disease_name"
    ).size().reset_index(name="total_cases")

    analytics.to_csv(
        "florarag_analytics.csv",
        index=False
    )

    return analytics
