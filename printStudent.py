class Student:
    def __init__(self, isim, cinsiyet, ders_notu, ders_kredisi = 2.4, toplam_kredi = 60):
        print("Student class'ı çalıştı.")
        print("-------------------------")

        self.isim=isim
        self.cinsiyet=cinsiyet
        self.ders_notu=ders_notu
        self.ders_kredisi = ders_kredisi
        self.toplam_kredi=toplam_kredi

    def show_myself(self):
        print("İsim: " + self.isim)
        print("Cinsiyet: " + self.cinsiyet)
        print("Ders Notu: " + str(self.ders_notu))
        print("Ders Kredisi: " + str(self.ders_kredisi))
        print("Toplam Kredi: " + str(self.toplam_kredi))

    def show_point(self):
        print(self.ders_notu * self.ders_kredisi / self.toplam_kredi)

ali = Student('Ali','erkek',20)
ali.show_myself()
ali.show_point()
