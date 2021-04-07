import pickle


class Reader:
    def __init__(self, path):
        self.path = path

    @staticmethod
    def sort_by_freq(csv_parsed):
        return [word for word, freq in sorted(csv_parsed, key=lambda a: a[1])][::-1][:20000]

    def __read_file(self):
        csv_parsed = []
        with open(self.path, encoding="utf-8") as csv:
            for line in csv:
                splitted = line.split("\t")
                if splitted[1] == "s" and 4 <= len(splitted[0]) < 10:
                    csv_parsed.append((splitted[0], float(splitted[2])))

        return Reader.sort_by_freq(csv_parsed)

    def write_pickle(self):
        easy_data = self.__read_file()[:10000]
        middle_data = self.__read_file()[10000:15000]
        hard_data = self.__read_file()[15000:20000]
        with open("./words/easy.pickle", "wb") as file:
            pickle.dump(easy_data, file)
        with open("./words/med.pickle", "wb") as file:
            pickle.dump(middle_data, file)
        with open("./words/hard.pickle", "wb") as file:
            pickle.dump(hard_data, file)


if __name__ == "__main__":
    Reader("freqrnc2011.csv").write_pickle()
