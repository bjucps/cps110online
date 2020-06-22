import csv

with open("produceSales2.csv") as produceFile:
  produceFile.readline()                # discard first line

  csvReader = csv.reader(produceFile)
  lines = list(csvReader)

  produceTotals = {}
  for csvLine in lines:
    # Extract data from current line
    # [produceType, _, _, total] = csvLine
    produceType = csvLine[0]  # produce type is in position 0 of list
    total = csvLine[3]        # produce total is in position 3 of list
    
    produceTotals[produceType] = produceTotals.get(produceType, 0) + float(total)

for produceType in sorted(produceTotals):
  print("{} - ${:.2f}".format(produceType, produceTotals[produceType]))
  
