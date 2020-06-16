from modules import AnalyzePattern as ap

def main():
    sample_input = "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT"
    k = 3
    print(ap.frequentWords(sample_input, k))


if __name__ == "__main__":
    main()