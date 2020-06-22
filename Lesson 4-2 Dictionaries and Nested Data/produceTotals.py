

with open("produceSales.csv") as produceFile:
  produceFile.readline()  # discard first line

  produceTotals = {}
  for line in produceFile:
    [produceType, _, _, total] = line.strip().split(',')
    
    produceTotals[produceType] = produceTotals.get(produceType, 0) + float(total)

for produceType in sorted(produceTotals):
  total = produceTotals[produceType]
  print(f"{produceType} - ${total:.2f}")
