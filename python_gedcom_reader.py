tags = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM',
'MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']
levels = ['1','2','3']
valid = ["Y", "N"]

gedcom_file = open("Holcomb-Project02.ged", "r")

def gedcom_file_reader(gedcom_file):
  line_count = 0
  for line in gedcom_file:
    line_count += 1
    print(f"-->|{line}")
    level = line[:1]
    split_line = line.split()
    for keyword in split_line:
      if keyword in tags:
        valid = "Y"
        print(f"<--|" + keyword + "|" + level + "|" + valid)
      else:
        valid = "N"
        print(f"<--|" + keyword + "|" + level + "|" + valid)
  print(line_count)

gedcom_file_reader(gedcom_file)




