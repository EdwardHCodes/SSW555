tags = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM',
'MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']
valid = ["Y", "N"]
empty_array = []
empty_string = ""

gedcom_file = open("Holcomb-Project02.ged", "r")

def gedcom_file_reader(gedcom_file):
  empty_string = ""
  line_count = 0
  for line in gedcom_file:
    line_count += 1
    empty_array.append((f"--> {line}"))
    level = line[0]
    #print(level)
    split_line = line.split()
    for keyword in split_line:
      if keyword in tags:
        key = keyword
        if keyword == "INDI" or keyword == "FAM":
          args = line[1]
        else:
          args = line[2:]
        valid = "Y"
      else:
        valid = "N"
        key = line[1]
        args = line[2:]
        print("Keyword's we know" + keyword)
    empty_string = "<-- " + level + "|" + key + "|" + valid + "|" + str(args)
    empty_array.append(empty_string)
  for item in empty_array:
    print(item)
  print(line_count)

gedcom_file_reader(gedcom_file)




