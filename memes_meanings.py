None
genzwords = {
    "CRINGE":"Utandırıcı bir olay yaşandığında kullanılır"
    "CREEPY":"Bir şey ürkütücü olunca kullanılır"
    "LMAO":"Bir şey çok komik olunca",
    "BTW":"Bu arada demek"
}
word = input("Günümüzdeki çocoukların kullanıpta sizin anlamadığınız bir kelime yazın(Hepsini büyük harfle yazın.):")
if word in genzwords.keys():
    print(genzwords[word])
else:
    print("Bu kelime sözlükte yoktur.")
