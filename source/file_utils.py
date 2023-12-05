class FileUtilities:

    @staticmethod
    def store(data, file_path) -> None:
        with open(file=file_path, mode="a") as file:
            file.write(data + "\n")
