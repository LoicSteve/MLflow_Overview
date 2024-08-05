from mlflow import log_metric, log_param, log_artifact

if __name__ == "__main__":
    # Log a parameter (key-value pair)
    log_param("threshlod", 5)
    log_param("verbosity", "DEBUG")

    log_metric("timestap", 10000)
    log_metric("TTC", 33)

    # Log an artifact (output file)
    log_artifact("produced-dataset.csv")
