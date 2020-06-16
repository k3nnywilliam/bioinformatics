
def patternCounter(genome, pattern):
    count = 0 
    gen_len = len(genome)
    pattern_len = len(pattern)
    
    for i in range(0, gen_len - pattern_len+1):
        if genome[i:i+pattern_len] == pattern:
            count+=1
    return count


def frequentWords(genome, k):
    frequent_patterns = set()
    genome_len = len(genome)
    count = []
    
    for i in range(0, genome_len - k):
        pattern = genome[i:i+k]
        count.append(patternCounter(genome, pattern))
        
    maxCount = max(count)
    for i in range(0, genome_len - k):
        if count[i] == maxCount:
            frequent_patterns.add(genome[i:i+k])
            
    return frequent_patterns


def reverse_complement(pattern, result):
    complements = {"A":"T", "C":"G", "G":"C", "T":"A"}
    rc = []
    
    for i in pattern:
        if i in complements:
            rc.append(complements[i][0])
        else:
            print("We have an invalid genome data.")        
    result = rc[::-1]
    
    with open(result, 'w') as filehandle:
        filehandle.writelines("%s" % c for c in result)
    
    return result


def pattern_matching(genome, pattern):
    gen_len = len(genome)
    pattern_len = len(pattern)
    starting_pos = []
    
    for i in range(0, gen_len - pattern_len+1):
        if genome[i:i+pattern_len] == pattern:
            starting_pos.append(i)
    return starting_pos


def pattern_to_number(pattern):
    pass


def number_to_pattern(idx):
    pass
    

def computing_frequencies(genome, k):
    arr = [None] * (4**k)
    
    for i in range(len(arr) - 1):
        arr.append(0)
        
    for i in range(len(genome) - k):
        pattern = genome[i:i+k]
        j = pattern_to_number(pattern)
        
    return arr


def clump_finding(genome, k, L, t):
    frequent_patterns = set()
    genome_len = len(genome)
    clump = []
    freq_array = []
    arr = [None] * (4**k)
    
    for i in range(0, len(arr) - 1):
        clump.append(0)
    
    for i in range(0, genome_len - L):
        freq_array.append(frequentWords(genome, k))
        for j in range(0, len(arr) - 1):
            if freq_array[j] >= t:
                clump[j].append(1)
    
    for i in range(0, len(arr) - 1):
        if clump[i] == 1:
            pass
            
    return frequent_patterns
            

def check_file_length(file):
    with open(file, 'r') as f:
        data = f.read().strip()
        char_nums = len(data)
        print(f"char_nums: {char_nums}")