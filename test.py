key_words = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM',
             'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']

levels = ['1', '2', '3']

text_file = open("export-BloodTree.ged", 'r')


y = '000'
lerp = '000'
derp = '000'
for line in text_file:
  level_number = line[:1]

  line = line.split()

  ##For user story to print all the males in a genealogy
  for name in line:
      while line[2] != "M" or "F":
        if line[1]==


  for word in key_words:
      if word in line:

       derp = word
       y = 'Y'

  for burb in levels:
      if burb in line:
        lerp = burb

  print('<-- |' + derp + '|' + lerp + '|' + y)
  print("-->", line)

  
