from modules import AnalyzePattern as ap

def main():
    
    file = "data/Vibrio_cholerae.txt"
    custom_pattern = "CTTGATCAT"
    
    with open(file, "r") as f:
        lines = f.read().splitlines()
        pattern = lines[0]
        genome = lines[-1]
        
        print(*ap.pattern_matching(genome, custom_pattern))
    

if __name__ == "__main__":
    main()