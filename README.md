# Hava durumu

Bu proje, kullanıcıların şehir ve ülke kodu girerek hava durumu bilgilerini görüntülemelerine olanak tanıyan basit bir hava durumu uygulamasıdır. Uygulama, şehir ve ülke koduna göre hava durumu verilerini almak için bir API çağrısı yapar ve sonucu kullanıcıya gösterir.

## Özellikler

- Şehir ve ülke koduna göre hava durumu verilerini görüntüleyebilme
- Flask uygulaması hava durumu verilerini OpenWeather API'den çekecek.
Verileri işleyip HTML sayfasında görüntüleyecek.

## Teknolojiler

- HTML
- JavaScript
- API
- Docker
- Docker Compose

## Kurulum talimatları ve çalıştırma işlemi

1. **Projeyi İndirin:**
   Projeyi yerel bilgisayarınıza indirin veya kopyalayın.

2. **HTML Dosyasını Açın:**
   Projeyi bir tarayıcıda görüntülemek için `index.html` dosyasını bir tarayıcıda açın.

3. **Dockerfile Dosyası açın**
     Dockerfile dosyası açarak çalışması için gerekli docker komutlarını girin.

4. **Docker Compose**
   docker-compose.yml şeklinde bir compose dosyası açın.

5. **API Bağlantısı:**
   Bu uygulama, hava durumu verilerini almak için bir API'ye ihtiyaç duyar. API uç noktası `/weather` olarak varsayılmıştır. Uygulamanızı çalıştırmadan önce, bu uç noktanın doğru bir şekilde ayarlandığından emin olun veya bir hava durumu API'si ile iletişim sağlayın.

6. **Kullanım:**
   - Şehir adı ve ülke kodunu girin.
   - "Hava Durumu" düğmesine tıklayın.
   - Hava durumu bilgilerini ekranda ekranda görebileceksiniz.

Bu adımları takip ederek proje hazır ve çalışır durumda olacaktır.

### Açıklamalar

- **Flask Uygulaması (`app.py`)**: Flask, hava durumu verilerini OpenWeather API'den alır ve kullanıcıya gösterir.
- **HTML ve JavaScript (`index.html`)**: Basit bir kullanıcı arayüzü ve hava durumu verilerini çeken JavaScript kodu içerir.
- **Dockerfile**: Flask uygulamasını çalıştırmak için gerekli ortamı oluşturur.
- **Docker Compose (`docker-compose.yml`)**: Tek bir komutla tüm uygulamanın başlatılmasını sağlar.

## API Bilgileri

Uygulama, hava durumu verilerini almak için aşağıdaki gibi bir API çağrısı yapar:


- `city`: Şehir adı (örneğin, `Istanbul`)
- `country`: Ülke kodu (örneğin, `TR`)

## Hata Yönetimi

API'den dönen hata mesajları uygulama ekranında gösterilir. Hata kodları ve mesajları hakkında daha fazla bilgi için API dökümantasyonuna başvurun.

## Katkıda Bulunma

Eğer bu projeyi geliştirmek istiyorsanız, katkılarınızı her zaman bekleriz! Lütfen pull request göndererek katkıda bulunun.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

## İletişim

Herhangi bir soru veya öneri için iletişime geçmekten çekinmeyin.

---

Bu `README.md` dosyası projenizin temel bilgilerini, nasıl çalıştırılacağını ve nasıl kullanılacağını açıklamak için tasarlanmıştır. Gerektiğinde proje gereksinimlerinize uygun olarak düzenlemeler yapabilirsiniz.

