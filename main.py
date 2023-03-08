from instagrapi import Client

client = Client()
client.login('melaniehenderson671wwg', 'FtsNFUgC')


URL = "https://www.instagram.com/p/CphXPaHsF7K/"

pk = client.media_pk_from_url(URL)
user = client.media_user(pk)

with open('temp.txt', 'w') as f:
    f.write(str(user))

client.logout()
