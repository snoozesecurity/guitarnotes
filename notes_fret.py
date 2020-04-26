# Accepts user input in the form of a space-separated string; zero input validation, might fix later

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

def printFretboard(start: str, frets: int) -> str:
  output = []
  idx = notes.index(start)
  output.append(notes[idx] + "|")
  if idx + 1 == len(notes):
    idx = 0
  else: 
    idx += 1
  for i in range(frets):
    if i + 1 == frets:
      output.append("|-" + notes[idx] + "-|")
    else:
      output.append("|-" + notes[idx] + "-")
    if idx + 1 >= len(notes):
      idx = 0
    else:
      idx += 1
  return output

tuning = input("Enter your tuning with notes separated by spaces (ex. E A D G B E): ")
userNotes = [x.strip().upper() for x in tuning.split()]
outList = []
for item in userNotes[::-1]:
  outList.append(printFretboard(item, 12))
for item in outList:
  print(''.join(item))
