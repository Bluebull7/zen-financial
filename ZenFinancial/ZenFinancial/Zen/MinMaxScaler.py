def min_max_scaler(data, feature_range=(-1, 1)):
    min_val = np.min(data)
    max_val = np.max(data)
    scale = (feature_range[1] - feature_range[0]) / (max_val - min_val)
    return feature_range[0] + (data - min_val) * scale

