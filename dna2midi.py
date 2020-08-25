from midiutil import MIDIFile
import sys

gene = sys.stdin.read().upper()

pitch = {'A':52, 'T':59, 'G':66, 'C':68}
tempo = 130
acids = {'A', 'T', 'G', 'C'}

track = 0
channel = 0
time = 0
duration = 1

volume = 100

rf = MIDIFile(1)

rf.addTempo(track, time, tempo)

for acid in gene:
    if acid not in acids: continue
    rf.addNote(track, channel, pitch[acid], time, duration, volume)
    time += 1

with open("result.mid", "wb") as output_file:
    rf.writeFile(output_file)
