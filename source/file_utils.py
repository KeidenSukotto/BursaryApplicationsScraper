class FileUtilities:

    @staticmethod
    def store(data) -> None:
        with open(file="../data/open_bursaries_links", mode="a") as file:
            file.write(data + "\n")
