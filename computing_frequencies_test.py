from modules import AnalyzePattern as ap

def main():
    genome = "ACGCGGCTCTGAAA"
    k = 5
    
    print(ap.computing_frequencies(genome, k))
    
    

if __name__ == "__main__":
    main()