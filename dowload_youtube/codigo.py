from pytube import YouTube


#url video
url = input("Qual a Url do vídeo? ")

#formato da mídia
audio_ou_video = input("Escolha a mídia>>>> [1] Áudio [2] Vídeo [3] Complemento:" ) 

#nome do video
nome_do_arquivo = pytube.Youtube(url).title

if audio_ou_video == '1':
        youtube = pytube.Youtube(url).streams.filter(adaptive=True, type="audio")
        nome_do_arquivo = f'{nome_do_arquivo}_audio'

elif audio_ou_video == '2':
     youtube = pytube.Youtube(url).streams.filter(adaptive=True, type="video")
     nome_do_arquivo = f'{nome_do_arquivo}_video'

elif audio_ou_video == '3':
     youtube = pytube.Youtube(url).streams.filter(progressive=True)
     nome_do_arquivo = f'{nome_do_arquivo}_completo'

#salva
youtube.first().download(ouput_path="C:\\Downloads", filename=nome_do_arquivo)
