tags = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM',
        'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']
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
      value = line[1]
      if value in tags:
        key = keyword
        valid = "Y"
        if keyword == "INDI" or keyword == "FAM":
          args = line[1]
        else:
          args = line[2:]
      else:
        valid = "N"
        args = line[2:]
        key = line[1]
    empty_string = "<-- " + level + "|" + key + "|" + valid + "|" + args
    empty_array.append(empty_string)
  for item in empty_array:
    print(item)
  print(line_count)


gedcom_file_reader(gedcom_file)

def persons_age(age):
  pass








