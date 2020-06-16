import time
from modules import AnalyzePattern as ap


def test1(sample_genome, sample_pattern):
    start_time = time.time()
    print(f"K-mer pattern count: {ap.patternCounter(sample_genome, sample_pattern)}")
    print(f"Processing time took: {time.time() - start_time}s")

def test2(sample_genome, sample_pattern):
    start_time = time.time()
    print(f"K-mer pattern count: {ap.patternCounter2(sample_genome, sample_pattern)}")
    print(f"Processing time took: {time.time() - start_time}s")
    

def main():
   with open("data/dataset_2_7.txt", "r") as f:
        lines = f.read().splitlines()
        genome = lines[0]
        pattern = lines[-1]
        
        start_time = time.time()
        print(f"K-mer pattern count: {ap.patternCounter(genome, pattern)}")
        print(f"Processing time took: {time.time() - start_time}s")
    
    
if __name__ == "__main__":
    main()