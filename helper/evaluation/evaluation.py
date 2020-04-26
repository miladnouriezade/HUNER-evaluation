
def evaluate(ground_truth, prediction):
    from seqeval.metrics import classification_report
    import csv
    """
    Read prediction and ground_truth labels and pass labels to
    classification_report
    """

    y_pred = []
    y_true = []
    with open(ground_truth, 'r') as f:
        r = csv.reader(f, delimiter='\t', quotechar=None)
        lines = list(r)
        for line in lines:
            if len(line) > 0:
                y_pred.append(line[2])

    with open(prediction, 'r') as f2:
        reader = csv.reader(f2, delimiter='\t', quotechar=None)
        for row in reader:
            if any(field.strip() for field in row):
                y_true.append(row[1])

    print('y_true count :', len(y_true))
    print('y_pred count :', len(y_pred))
    print(classification_report(y_true, y_pred))


evaluate('OUTPUT.tsv', 'test.tsv')