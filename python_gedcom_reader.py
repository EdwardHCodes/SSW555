tags = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM',
'MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']
levels = ['1','2','3']
valid = ["Y", "N"]

gedcom_file = open("Holcomb-Project02.ged", "r")

for line in gedcom_file:
  print(f"-->|{line}")
  level = line[:1]
  split_line = line.split()
  for keyword in tags:
    if keyword in split_line:
      valid = "Y"
      print(f"<--|" + keyword + "|" + level + "|" + valid)
    else:
      valid = "N"
      print(f"<--|" + keyword + "|" + level + "|" + valid)
