# DefenceTURK Ui
[DefenceTURK](http://www.defenceturk.com/) web sitesi içeriğini daha düzgün ve optimize görüntülenebilmesi için hobi olarak yaptığım web arayüz projesi.Bu projede BeautifulSoup ile sitedeki veriler kazınmış daha sonrada Flask ve Tailwind ile daha düzgün bir siteye içerik aktarılmıştır.

> Bu projeden herhangi bir gelir elde edilmemiştir. Hobi amaçlı geliştirilmiştir.

## Kullanılan Teknolojiler
* Python
* BeautifulSoup
* Flask
* Tailwind
* request

### Kurulum
> Bilgisayarınızda Python kurulu olmalıdır
> Proje localhost:5000 portunda çalışmaktadır.
```
cd project
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
flask run --debug
```

#### Ekran Görüntüleri

##### Anasayfa
![Ana Sayfa](</screenshot/home.png>)

##### Konular
![alt text](<./screenshot/topic.png>)

##### Postlar
![Ee](<./screenshot/post.png>)