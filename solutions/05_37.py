df = df.merge(languages, how="left", left_on="country", right_on="Country")