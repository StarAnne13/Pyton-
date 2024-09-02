meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Garip ya da utandırıcı bir şey",
            "ROFL":"bir şakaya karşılık cevap",
            "SHEESH":"onaylamamak",
            "CREEPY":"korkunç",
            "AGGRO":"agrasifleşmek/sinirlenmek",
            }
word = input("Anlamadığınız bir kelime yazın : ").upper()

if word in meme_dict.keys():
    print(meme_dict[word ])
else:
    print("Kelime Bulunamadı Lütfen Başka kelime yazınız!")
