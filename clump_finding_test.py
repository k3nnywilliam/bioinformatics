from modules import AnalyzePattern as ap

def main():
    
    genome = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    k = 5
    L = 50
    t = 4
    
    print(ap.pattern_to_number("GT"))
    print(ap.number_to_pattern(11))
    #print(ap.clump_finding(genome, k, L, t))
    

if __name__ == "__main__":
    main()