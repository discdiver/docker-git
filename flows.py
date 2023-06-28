from prefect import flow


@flow(log_prints=True)
def hi():
    print("waz up")


if __name__ == "__main__":
    hi()
