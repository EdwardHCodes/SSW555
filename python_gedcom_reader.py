tags = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM',
'MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']
levels = ['1','2','3']
valid = ["Y", "N"]

gedcom_file = open("Holcomb-Project02.ged", "r")

for line in gedcom_file:
  print(f"-->|{line}")
  level = line[:1]
  split_line = line.split()
  for word in tags:
    i = 0
    if word = word[i]
    i += 1  
  if word in split_line is in tags:
    valid = "Y"
    print(f"<--|" + word + "|" + level + "|" + valid)

