
###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
# Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..

###############################################################
# Veri Seti Hikayesi
###############################################################

# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# last_order_channel : En son alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

###############################################################
# GÖREVLER
###############################################################

# GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama
           # 1. flo_data_20K.csv verisini okuyunuz.
           # 2. Veri setinde
                     # a. İlk 10 gözlem,
                     # b. Değişken isimleri,
                     # c. Betimsel istatistik,
                     # d. Boş değer,
                     # e. Değişken tipleri, incelemesi yapınız.
           # 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
           # alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
           # 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
           # 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
           # 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
           # 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
           # 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.
import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option("display.width", 1000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
df_ = pd.read_csv("FLOMusteriSegmentasyonu/flo_data_20k.csv")
df = df_.copy()
df.info()
# GÖREV 2: RFM Metriklerinin Hesaplanması

# GÖREV 3: RF ve RFM Skorlarının Hesaplanması

# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması

# GÖREV 5: Aksiyon zamanı!
           # 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.
           # 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulun ve müşteri id'lerini csv ye kaydediniz.
                   # a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
                   # tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers),
                   # ortalama 250 TL üzeri ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kuralacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına
                   # yeni_marka_hedef_müşteri_id.cvs olarak kaydediniz.
                   # b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşteri olan ama uzun süredir
                   # alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
                   # olarak kaydediniz.


# GÖREV 6: Tüm süreci fonksiyonlaştırınız.

###############################################################
# GÖREV 1: Veriyi  Hazırlama ve Anlama (Data Understanding)
###############################################################


# 2. Veri setinde
        # a. İlk 10 gözlem,
        # b. Değişken isimleri,
        # c. Boyut,
        # d. Betimsel istatistik,
        # e. Boş değer,
        # f. Değişken tipleri, incelemesi yapınız.
def check_df(dataframe):
    print("##################### First 10 Observations #####################")
    print(dataframe.head(10))
    print("##################### Column names #####################")
    print(df.info())
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Types #####################")
    print(dataframe.dtypes)
check_df(df)
# 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Herbir müşterinin toplam alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.

df["total_num_order"] = df["order_num_total_ever_online"]+df["order_num_total_ever_offline"]

df["total_customer_value"]=df["customer_value_total_ever_offline"]+df["customer_value_total_ever_online"]
df.info()

# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
df.dtypes
for i in df.columns:
    if "date" in i:
        print(i)
        df[i] = df[i].apply(pd.to_datetime)
        print(df[i].dtype)


# 5. Alışveriş kanallarındaki müşteri sayısının, toplam alınan ürün sayısı ve toplam harcamaların dağılımına bakınız.

df.groupby("order_channel").agg({"total_num_order":["sum"],
                                "total_customer_value":["sum"]})

## soru ?? gösterilen değerler yanlış....


# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.

df.sort_values("total_customer_value",ascending=False).iloc[0:10,[0,13]]


df[["master_id", 'total_shopping_number', 'total_value']].sort_values('total_shopping_number', ascending=False).head(10)

# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.

df.sort_values("total_num_order",ascending=False).iloc[0:10,[0,12]]


# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.

def pre_processing(df):
    for i in df.columns:
        if "date" in i:
            df[i] = df[i].apply(pd.to_datetime)
    df["total_num_order"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
    df["total_customer_value"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
    check_df(df)





###############################################################
# GÖREV 2: RFM Metriklerinin Hesaplanması
###############################################################

# Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi
df["last_order_date"].max()
today_date = dt.datetime(2021, 6, 1)

df["days_last_seen"]=df["last_order_date"].apply(lambda x: (today_date-x).days)
# customer_id, recency, frequnecy ve monetary değerlerinin yer aldığı yeni bir rfm dataframe
rfm = df.loc[:,["master_id", "days_last_seen", "total_num_order", "total_customer_value"]]
rfm.columns = ["customer_id", "recency", "frequency", "monetary"]

rfm.describe().T

###############################################################
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması (Calculating RF and RFM Scores)
###############################################################
rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])

rfm["frequency_score"] = pd.qcut(rfm['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])

#  Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çevrilmesi ve
# Bu skorları recency_score, frequency_score ve monetary_score olarak kaydedilmesi


rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) +
                    rfm['frequency_score'].astype(str))
# recency_score ve frequency_score’u tek bir değişken olarak ifade edilmesi ve RF_SCORE olarak kaydedilmesi


###############################################################
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
###############################################################
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}
#seg_map'te 2den fazla 3 adet yada koymak istersem?
rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)


# Oluşturulan RFM skorların daha açıklanabilir olması için segment tanımlama ve  tanımlanan seg_map yardımı ile RF_SCORE'u segmentlere çevirme


###############################################################
# GÖREV 5: Aksiyon zamanı!
###############################################################

# 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.

rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])

# 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulunuz ve müşteri id'lerini csv ye kaydediniz.

# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Bu müşterilerin sadık  ve
# kadın kategorisinden alışveriş yapan kişiler olması planlandı. Müşterilerin id numaralarını csv dosyasına yeni_marka_hedef_müşteri_id.cvs
# olarak kaydediniz.

rfm.rename(columns={"customer_id":"master_id"}, inplace=True)
rfm_new = pd.merge(rfm, df, on="master_id")
selected_ones = rfm_new.loc[
    ((rfm_new["segment"] == "loyal_customers") | (rfm_new["segment"] == "champions") &
     rfm_new["interested_in_categories_12"].str.contains("KADIN")),
    ["master_id", "interested_in_categories_12", "segment"]
]
selected_ones.to_csv("yeni_marka_hedef_musteri.csv")

# selected_ones = list(rfm.loc[(rfm["segment"]=="loyal_customers") | (rfm["segment"]=="champions"),"master_id"].values)
# df.drop("master_id",axis=1, inplace=True)
# df.reset_index(inplace=True)


# df["interested_in_categories_12"].value_counts()
# if "KADIN" in df["interested_in_categories_12"][2]:
#     print(True)


# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşterilerden olan ama uzun süredir
# alışveriş yapmayan ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz.
selected_ones_2 = rfm_new.loc[
    ((rfm_new["segment"] == "new_customers") | (rfm_new["segment"] == "cant_loose") | (rfm_new["segment"] == "at_Risk"))
    & ((rfm_new["interested_in_categories_12"].str.contains("COCUK")) |
       (rfm_new["interested_in_categories_12"].str.contains("ERKEK"))),
    ["master_id", "interested_in_categories_12","segment"]
]
selected_ones_2.to_csv("indirim_hedef_musteri_ids.csv")

selected_ones_2_1 = rfm_new.loc[(rfm_new["segment"].isin(["new_customers","cant_loose","new_customers"]))
                              & (rfm_new["interested_in_categories_12"].isin(["COCUK", "ERKEK"])),
                              ["master_id", "interested_in_categories_12","segment"]
                                 ]

selecte_ones_2_1.to_csv("indirim_hedef_musteri_2.csv", index=False)
