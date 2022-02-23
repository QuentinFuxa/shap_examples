def mad_score(points):
    m = np.median(points)
    ad = np.abs(points - m)
    mad = np.median(ad)
    return 0.6745 * ad / mad

THRESHOLD = 3
z_scores = mad_score(df_error_rec)
outliers = z_scores > THRESHOLD
