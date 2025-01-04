# HandGestureAI
Predict sign language just using a hand gesture! =========================================================================================================================================================================================================================
 * CARA MEREKAM DAN MEMBUAT GESTURE BARU (custom)
 1.) File gesture_record.py
     File ini merupakan file sebagai tempat mengumpulkan data. dikarenakan projek ini
     kita sudah isi dengan data datanya yaitu A-Z (peragaan nya bisa dilihat di folder Dataset(peragaan)), 
     maka dari itu kami akan jelaskan bagaimana
     cara mengumpulkan datanya. Jika kalian ingin record ulang datanya, kalian bisa menghapus
     2 file yang bernama 
     - gestures_data.npy 
     - gestures_labels.npy
     jika sudah dihapus 2 file tersebut, sebenarnya kalian sudah bisa merekam/record tetapi
     sebelumnya kalian harus mengganti atau menambah field ini
     gestures = {'A': 0, 'B': 1, 'C': 2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}  
     didalam array itu, kalian bisa ganti isi dari array tersebut sesuai kemauan kalian.
     lalu, kalian bisa mengganti atau menambah statement if elif ini
     if key == ord('a'): <--------- ini merupakan keyword yang akan dipencet guna untuk menyimpan hasil record
      data.append(landmark_array)
               labels.append(gestures['A']) <-------- ini berfungsi supaya hasil record disimpan ke label ini
               print("Saved gesture: A") <------ ini akan ditampilkan jika hasil record berhasil di simpan
       
     jika kalian sudah melakukan langkah diatas, kalian bisa jalankan dan mulai untuk merekam.
     cara recordnya, kalian bisa langsung meragakan gesture tangannya ke depan kamera.
     tunggu sampai gesture tangannya terlihat lalu kalian bisa save. nah tombol untuk savenya
     kalian bisa menekan tombol sesuai huruf yang kalian peragakan. misalnya kalian meragakan huruf "A"
     maka, kalian menyimpannya dengan menekan tombol "a" dikeyboard. kalian bisa menekan beberapa kali untuk memastikan 
     model supaya bisa lebih akurat.lalu untuk outputnya, data data yang sudah direkam tadi akan disimpan ke folder
     berformat (.npy) (terdapat 2 file berformat tersebut).

 2)  File model_gesture.py
     Nah, di file ini, data data yang sudah kalian kumpulkan tadi dan tersimpan di 2 file
     yang berformat (.npy) tadi, kalian bisa melatih model kalian sendiri.
     cara kerjanya, jadi file ini akan membuat variable 'data' dan 'label'

     data = np.load('gestures_data.npy')
     labels = np.load('gestures_labels.npy')

     2 variabel ini akan mengambil data data yang sudah di kumpulkan di 2 file tersebut.
     jika tidak ada masalah, kalian bisa menjalankan program di file ini.
     output yang dihasilkan akan menghasilkan file "gesture_model.h5". model kalian akan disimpan ke file tersebut.

 3.) File app.py (main file)
     Nah terakhir, file ini merupakan file utama dari projek kami. sebelum kalian jalankan,
     kalian harus mengatur 1 hal yaitu mengganti atau menambahkan label.

     labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

     kode ini berada di app.py. kalian bisa ganti atau tambah label ini sesuai dengan data yang sudah kalian kumpulkan tadi.
     jika sudah semua, kalian bisa jalankan programnya dan seharusnya programnya bisa dijalankan dengan lancar.

 ========================================================================================================================================================================================================================
 
  Dan untuk yang terakhir, kita akan menunjukkan kontrol kontrol yang kita gunakan di projek kami:
  - a = untuk menambahkan huruf ke layar (screen)
 - s = untuk membuat spasi antar huruf di layar
  - c = untuk menghapus keseluruhan huruf di layar
  - t = untuk membacakan huruf yang berada di layar (text to speech)
  - q = untuk keluar dari program

 mungkin itu saja penjelasan dan tutorial singkat dari projek kami
 mohon maaf jika ada yang kurang dipahami dan tidak jelas
 wassalamualaikum wr.wb dan selamat pagi/siang/sore/malam.
