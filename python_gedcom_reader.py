tags = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM',
'MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']
valid = ["Y", "N"]

gedcom_file = open("Holcomb-Project02.ged", "r")

def gedcom_file_reader(gedcom_file):
  line_count = 0
  for line in gedcom_file:
    line_count += 1
    print(f"--> {line}")
    level = line[0]
    print(level)
    split_line = line.split()
    for keyword in split_line:
      if keyword in tags:
        ##if keyword == "INDI" or keyword == "FAM":
        ##level += 1
        valid = "Y"
        print(f"<-- " + level + "|" + keyword + "|" + valid + "|" + str(split_line))
      else:
        valid = "N"
        print(f"<-- " + level + "|" + line[1] + "|" + valid + "|" + str(split_line))
  print(line_count)

gedcom_file_reader(gedcom_file)




