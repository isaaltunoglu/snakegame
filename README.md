# Snake Game

Bu proje, Python'un `tkinter` kütüphanesi ile oluşturulmuş klasik bir **Yılan Oyunu**dur. Oyunda yılanı yön tuşlarıyla kontrol ederek yiyeceklere ulaşmanız ve büyümeniz gerekiyor. Yılan duvarlara veya kendi vücuduna çarparsa oyun sona erer.

## Oyun Özellikleri
- `tkinter.Canvas` kullanılarak görselleştirme sağlanmıştır.
- Yılanın hareketi yön tuşlarıyla değiştirilir (`Up`, `Down`, `Left`, `Right`).
- Yılan yiyeceği yedikçe uzar ve puan kazanırsınız.
- Duvara veya kendine çarpan yılan oyunu kaybeder.
- `Game Over` ekranı görüntülenir.

## Gereksinimler
Bu oyunu çalıştırmak için Python'un yüklü olması gerekmektedir. Python 3.x önerilir.

## Kurulum ve Çalıştırma
1. Python'u bilgisayarınıza kurun (eğer yüklü değilse).
2. Bu projeyi klonlayın veya `.py` dosyasını indirin.
3. Terminal veya Komut İstemi'ni açın ve şu komutu çalıştırın:
   ```sh
   python snake_game.py
   ```
4. Oyun açıldıktan sonra yön tuşlarıyla yılanı kontrol edebilirsiniz.

## Oyun Kontrolleri
| Tuş | İşlev |
|------|------|
| **↑ (Up Arrow)** | Yukarı hareket |
| **↓ (Down Arrow)** | Aşağı hareket |
| **→ (Right Arrow)** | Sağa hareket |
| **← (Left Arrow)** | Sola hareket |

## Oyun Mantığı
- **Yılanın hareketi:** `velocityX` ve `velocityY` değişkenleri ile belirlenir.
- **Yiyecek oluşturma:** Rastgele bir konumda belirlenir.
- **Çarpışma kontrolleri:** Yılanın kendisine veya duvara çarpıp çarpmadığı kontrol edilir.
- **Oyun döngüsü:** `draw()` fonksiyonu sürekli çalışarak oyunun akıcı olmasını sağlar.

## Geliştirme Önerileri
Bu oyunu daha da geliştirmek isterseniz:
- **Skor tablosu** ekleyerek en yüksek skoru saklayabilirsiniz.
- **Hız artışı** ekleyerek zorluk seviyesini yükseltebilirsiniz.
- **Arayüz geliştirmeleri** ile daha renkli ve canlı bir görünüm sağlayabilirsiniz.

Bu oyunu geliştirdiğin için tebrikler! 😊

