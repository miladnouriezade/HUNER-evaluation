
def tokenize(data):
    import csv
    """
    tokenize .tsv labeled data
    remove labels and tokenize sentences with whitespace and write them to .txt file
    
    E.g.
    Torsade de pointes ventricular tachycardia during low dose intermittent dobutamine treatment
     in a patient with dilated cardiomyopathy and congestive heart failure .
    """

    with open(data,'r') as f:
        tokens = []
        r = csv.reader(f, delimiter='\t', quotechar=None)
        lines = list(r)

        for line in lines:
            if len(line) > 0:
                print(line[0])
                tokens.append(line[0])

        f = open('tokenized_test.txt','w')
        for token in tokens:
            f.write(token + ' ')

