print("COPTUPOBKA n 4UCEJI")
KOJIU4ECTBO_4UCEJI = int(input("BBEgUTE KOJIU4ECTBO 4UCEJI: "))
MACCUB_4UCEJI = []
for i in range(KOJIU4ECTBO_4UCEJI):
    _4UCJIO = int(input("BBEgUTE " + str(i + 1) + " 4UCJIO: "))
    MACCUB_4UCEJI.append(_4UCJIO)
print(MACCUB_4UCEJI)
#COPTUPOBKA
for i in range(KOJIU4ECTBO_4UCEJI-1):
    for j in range(KOJIU4ECTBO_4UCEJI-i-1):
        if MACCUB_4UCEJI[j] > MACCUB_4UCEJI[j+1]:
            CMEHA = MACCUB_4UCEJI[j]
            MACCUB_4UCEJI[j] = MACCUB_4UCEJI[j+1]
            MACCUB_4UCEJI[j+1] = CMEHA
print("OTCOPTUPOBAHHbIU MACCUB")
print(MACCUB_4UCEJI)
