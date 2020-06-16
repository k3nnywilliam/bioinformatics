from modules import AnalyzePattern as ap

def main():
    file = "data/dataset_3_2_2.txt"
    result = 'data/answer.txt'
    
    with open(file, "r") as f:
        pattern = f.read()
        ap.reverse_complement(pattern, result)
        
    ap.check_file_length(file)
    ap.check_file_length(result)


if __name__ == "__main__":
    main()