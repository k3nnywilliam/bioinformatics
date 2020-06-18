
def test_read(file):
   with open(file, "r") as f:
       lines = f.read().splitlines()
       genome = lines[0]
       pattern = lines[-1]#the pattern is on the last line of text file
       print(f"Genome: {genome}")
       print(f"K-mer pattern: {pattern}")
       
test_read("data/dataset_2_7.txt")
