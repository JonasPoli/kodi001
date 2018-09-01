# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.

VIDEOS = {            '1000 filmes': [
                       {'name': 'A Noite do Jogo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjQxMDE5NDg0NV5BMl5BanBnXkFtZTgwNTA5MDE2NDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/gamenight-leg-720p.mp4',
                       'genre': ''},

                       {'name': 'Batman Ninja',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYmFhYzZhYzgtZjZiYS00NWEwLWFhYTUtN2UxM2FmYzdhNDUyXkEyXkFqcGdeQXVyNDk2Nzc1Mg@@._V1_UY268_CR4,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/batmanninja-leg-720p.mp4',
                       'genre': ''},

                       {'name': 'Com Amor, Simon',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTMyZDdiMzUtZjcxNS00Mjc3LTljY2UtYjI4YmY5NzJlYjc1XkEyXkFqcGdeQXVyMTA5OTkwNTc@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/comamorsimon-dub-720p.mp4',
                       'genre': ''},

                       {'name': 'Covil de Ladrões',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzYyODcwMDAyM15BMl5BanBnXkFtZTgwOTA4MjIwNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/covildeladroes-dub-720p.mp4',
                       'genre': ''},

                       {'name': 'Eu Só Posso Imaginar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTRjNDc5NTAtZGJlYS00NTg4LTk2NTEtNGUwY2NiZWM3YTY2XkEyXkFqcGdeQXVyNTQ3MjE4NTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/icanonlyimagine-leg-720p.mp4',
                       'genre': ''},

                       {'name': 'Maze Runner 3: A Cura Mortal',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYyNzk3MDc2NF5BMl5BanBnXkFtZTgwMDk3OTM1NDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/mazerunnerdeathcure-dub-720p.mp4',
                       'genre': ''},

                       {'name': 'MAZE RUNNER: A CURA MORTA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYyNzk3MDc2NF5BMl5BanBnXkFtZTgwMDk3OTM1NDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://server02.dropapk.com:182/d/axcrrhxs4tcdvbi476y4zc25yrcwejpbjo5kz75nu7wcovbctanec2v4j55vijdwithim7nq/video.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Operação Red Sparrow',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTA3MDkxOTc4NDdeQTJeQWpwZ15BbWU4MDAxNzgyNTQz._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/redsparrow-dub-720p.mp4',
                       'genre': ''},

                       {'name': 'Pantera Negra',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://dropapk.com/vidembed-kmvsele1xmp0.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Pantera Negra',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/blackpanther-dub-720p.mp4',
                       'genre': ''},

                       {'name': 'PANTERA NEGRA ( -ONLINE)',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://bit.ly/2w8mVTe',
                       'genre': 'FASE 3'},

                       {'name': 'Pantera Negra ( Dublad0)',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://chronos.feralhosting.com/locaweb123/2017/filmes/2017/p123.mp4',
                       'genre': 'FILMES'},

                       {'name': 'Pedro Coelho',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOWE4YzE3Y2MtYzIyZS00NjA4LTliMDgtY2U0NGM2NzI4MjZlXkEyXkFqcGdeQXVyNTU5Mzk0NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://chronos.feralhosting.com/locaweb123/2017/filmes/2017/pedrocoelhohd.mp4',
                       'genre': 'FILMES'},

                       {'name': 'Pedro Coelho',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOWE4YzE3Y2MtYzIyZS00NjA4LTliMDgtY2U0NGM2NzI4MjZlXkEyXkFqcGdeQXVyNTU5Mzk0NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://dropapk.com/vidembed-ohatg90lgbvi.mp4',
                       'genre': 'Animação'},

                       {'name': 'Rampage: Destruição Total',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDA1NjA3ODU3OV5BMl5BanBnXkFtZTgwOTg3MTIwNTM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/rampage-leg-1080p.mp4',
                       'genre': ''},

                       {'name': 'Um Lugar Silencioso',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjI0MDMzNTQ0M15BMl5BanBnXkFtZTgwMTM5NzM3NDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/aquietplacenew-leg-1080p.mp4',
                       'genre': ''},

                       {'name': 'Vingadores: Guerra Infinita',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/infinitywar-dub-360p.mp4',
                       'genre': ''},

                       {'name': 'Vingadores: Guerra Infinita',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://chronos.feralhosting.com/locaweb123/2017/filmes/2017/vin123dbts.mp4',
                       'genre': 'FILMES'},

                       {'name': 'VINGADORES:GUERRA INFINITA ( - GRAVADO DO CINEMA)',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://conteudo.maxcinefree.ga/filmes/138-os-vingadores-guerra-infinita-2018-720-db.mp4',
                       'genre': 'FASE 3'},

                       {'name': ',A Grande Jogada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTkzMzRlYjEtMTQ5Yi00OWY3LWI0NzYtNGQ4ZDkzZTU0M2IwXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/g/z6/otvlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'A Forma da Água',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNGNiNWQ5M2MtNGI0OC00MDA2LWI5NzEtMmZiYjVjMDEyOWYzXkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://dropapk.com/vidembed-5uuo9mi35nip.mp4',
                       'genre': 'Lançamentos 2018'},

                       {'name': 'A Forma da Água',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNGNiNWQ5M2MtNGI0OC00MDA2LWI5NzEtMmZiYjVjMDEyOWYzXkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/aformadaagua-dub-720p.mp4',
                       'genre': ''},

                       {'name': 'A Grande Jogada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTkzMzRlYjEtMTQ5Yi00OWY3LWI0NzYtNGQ4ZDkzZTU0M2IwXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/g/z6/otvlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'A Grande Jogada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTkzMzRlYjEtMTQ5Yi00OWY3LWI0NzYtNGQ4ZDkzZTU0M2IwXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/mollysgame-leg-720p.mp4',
                       'genre': ''},

                       {'name': 'A Grande Jogada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTkzMzRlYjEtMTQ5Yi00OWY3LWI0NzYtNGQ4ZDkzZTU0M2IwXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/g/z6/otvlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'A Grande Jogada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTkzMzRlYjEtMTQ5Yi00OWY3LWI0NzYtNGQ4ZDkzZTU0M2IwXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/g/z6/otvlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'A morte de da parabens',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk0ODMyNjk1NF5BMl5BanBnXkFtZTgwNDkxOTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://ia601501.us.archive.org/1/items/LHMTVfilmes/A.M.T.D.P.LHMTv.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'A Morte Te Dá Parabéns',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk0ODMyNjk1NF5BMl5BanBnXkFtZTgwNDkxOTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/9jvnq-_gnPvOPyfBcojxBf8SxR2JxqysqGX_M1itNigSVgakr3FafseEiKe0JT_5wqbj3ZP3nRJZ_eI-=m22',
                       'genre': 'Filmes'},

                       {'name': 'A Vigilante do Amanhã: Ghost in the Shell',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzJiNTI3MjItMGJiMy00YzA1LTg2MTItZmE1ZmRhOWQ0NGY1XkEyXkFqcGdeQXVyOTk4MTM0NQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://s.netcine.tv/netcine-bucket/filmes2017/GHOSTLEG-BAIXO.mp4?',
                       'genre': 'FICCAO CIENTIFICA'},

                       {'name': 'A Vigilante do Amanhã: Ghost in the Shell (2017)',
                       'thumb': 'http://i.imgur.com/Ua9rtt6.jpg',
                       'video': 'http://s.netcine.tv/netcine-bucket/filmes2017/GHOSTLEG-BAIXO.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'DOENTES DE AMOR',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWM4YzZjOTEtZmU5ZS00ZTRkLWFiNjAtZTEwNzIzMDM5MjdmXkEyXkFqcGdeQXVyNDg2MjUxNjM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://srv.vplayer.tk/movie/doentesdeamor.mp4',
                       'genre': 'Filmes'},

                       {'name': 'DUNKIRK [COLOR orange] [/COLOR]',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BN2YyZjQ0NTEtNzU5MS00NGZkLTg0MTEtYzJmMWY3MWRhZjM2XkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://proxy-06.nyc.dailymotion.com/sec(c4dd4fd41d911df22e1ec852ab07e516)/video/937/925/357529739_mp4_h264_aac.m3u8',
                       'genre': 'Filmes'},

                       {'name': 'EM RITMO DE FUGA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjM3MjQ1MzkxNl5BMl5BanBnXkFtZTgwODk1ODgyMjI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/bR57Ycifl9fmSW0vFIJDSEkMGRDul5zltJWflc0is_o6eJPoZ-TAyamnXPQYn7SJWL9ewBJb8A=m22',
                       'genre': 'Filmes'},

                       {'name': 'EM RITMO DE FUGA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjM3MjQ1MzkxNl5BMl5BanBnXkFtZTgwODk1ODgyMjI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://srv1.unitplay.net/stream/720/339403-baby-driver.mp4',
                       'genre': 'Filmes'},

                       {'name': 'EXTRAORDINARIO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjFhOWY0OTgtNDkzMC00YWJkLTk1NGEtYWUxNjhmMmQ5ZjYyXkEyXkFqcGdeQXVyMjMxOTE0ODA@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/N_el4Oitf8HUXju7lz0rKeLypA2dWh1Zo8HYuq34QjCS4TUFmKijF6KM4xGXKt0RBaJ9gs0bnw=m18',
                       'genre': 'Filmes'},

                       {'name': 'EXTRAORDINÁRIO  TS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjFhOWY0OTgtNDkzMC00YWJkLTk1NGEtYWUxNjhmMmQ5ZjYyXkEyXkFqcGdeQXVyMjMxOTE0ODA@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://ia801506.us.archive.org/0/items/Extraordinrio.DUB.HDTS.Up.By.Ejds27/Extraordin%C3%A1rio.DUB.HDTS.Up.By.Ejds27.mp4',
                       'genre': 'Filmes'},

                       {'name': 'FORMA DA AGUA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNGNiNWQ5M2MtNGI0OC00MDA2LWI5NzEtMmZiYjVjMDEyOWYzXkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://srv1.unitplay.net/stream/ts/399055-the-shape-of-water.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Guardiões da Galáxia Vol. 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.youtube.com/watch?v=4MsVS5RwtKo',
                       'genre': 'Trailers de Filmes HD'},

                       {'name': 'GUERRA DOS SEXOS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZTljYmU2NTMtODhhNC00NjlhLWJhZTUtNDllODYyYWM4ZjA5XkEyXkFqcGdeQXVyNjM0ODk5NDY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/VDnL8ealr3JeDf5ndyhtTyRdNsNhuYEle_5iJ5ChNtjIBBsHt26tMTN59sBcs7QUnXc6W20TFA=m37',
                       'genre': 'Filmes'},

                       {'name': 'Homem-Aranha: De Volta ao Lar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.youtube.com/watch?v=YFqOn_fDCrc',
                       'genre': 'Trailers de Filmes HD'},

                       {'name': 'Homem-Aranha: De Volta ao Lar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/JQFLMZMaI-TMRXlQABQJnX4JoinfoWamcdd77wa9tu-66hZwkp2Au7ROaQrIlz8qTzPtCqp_rOuSQQhbeQ=m37',
                       'genre': 'Filmes'},

                       {'name': 'Homens de Coragem',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWFlOWI3YTMtYTk3NS00YWQ2LTlmYTMtZjk0ZDk4Y2NjODI0XkEyXkFqcGdeQXVyNTQxNTQ4Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/SS9aCIchZwIaOwX0qFd12SLvMG62bC_sT6sumSqhZpKtHyYdJVpnWt9LXyWs2zvujG17W7Lo=m22',
                       'genre': 'Filmes'},

                       {'name': 'HOMENS DE CORAGEM',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWFlOWI3YTMtYTk3NS00YWQ2LTlmYTMtZjk0ZDk4Y2NjODI0XkEyXkFqcGdeQXVyNTQxNTQ4Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/ExgmE_bocTmygEdFJPdImlMTylM_csy-4o9TBkzhvPHIAdCApY0Emlwx5HTwU2n6HFofsNXh=m22',
                       'genre': 'Filmes'},

                       {'name': 'Homens de Coragem',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWFlOWI3YTMtYTk3NS00YWQ2LTlmYTMtZjk0ZDk4Y2NjODI0XkEyXkFqcGdeQXVyNTQxNTQ4Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/QaOXL5k4TO6GOYbWjkkqqhpOmDhIsGNzMzox-CkQ3022ycI2oHgkcAPRyOEUFb_o8r8rv2lFkg=m22',
                       'genre': 'Filmes'},

                       {'name': 'John Wick Um Novo Dia para Matar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://filmesonlinenow.club/embed/JHONWICK2BLURAYDUB.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Liga da Justiça',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWVhZjZkYTItOGIwYS00NmRkLWJlYjctMWM0ZjFmMDU4ZjEzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.youtube.com/watch?v=bsoSmgLShzE&t=73s',
                       'genre': 'Trailers de Filmes HD'},

                       {'name': 'LOGAN LUCK: ROUBO EM FAMÍLIA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYyODg0NDU1OV5BMl5BanBnXkFtZTgwNjcxMzU0MjI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://ia601504.us.archive.org/30/items/L.L.R.E.F.2017.720p/L.L.R.E.F.2017.720p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'O ESTRANGEIRO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BM2RlMjcyMGQtZTU3OC00NGRlLWExMGEtYjU3ZjUyMDc0NWZmXkEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.googleapis.com/drive/v3/files/1SdTZ_X9CsCDGNG3CVGQbu0m1KyodTIki?key=AIzaSyAHfTjunuAnmyVgGADZo4HD4XN2YAO0MnQ&alt=media',
                       'genre': 'Filmes'},

                       {'name': 'O Poderoso Chefinho',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg5MzUxNzgxNV5BMl5BanBnXkFtZTgwMTM2NzQ3MjI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://dropapk.com/vidembed-u2nmsfx2ze4g.mp4?GATTITV',
                       'genre': 'INFANTIL'},

                       {'name': 'O PODEROSO CHEFINHO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg5MzUxNzgxNV5BMl5BanBnXkFtZTgwMTM2NzQ3MjI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/mh8V60RRIVFeaLH_ncJ-2IoP0RSkrkptfxbreAJ5j3s897hn5SBss-LIsWDZHE4mF7XB4Goqeg=m22',
                       'genre': 'Filmes'},

                       {'name': 'O PODEROSO CHEFINHO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg5MzUxNzgxNV5BMl5BanBnXkFtZTgwMTM2NzQ3MjI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/mh8V60RRIVFeaLH_ncJ-2IoP0RSkrkptfxbreAJ5j3s897hn5SBss-LIsWDZHE4mF7XB4Goqeg=m37',
                       'genre': 'Filmes'},

                       {'name': 'O Rei do Show',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjI1NDYzNzY2Ml5BMl5BanBnXkFtZTgwODQwODczNTM@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/oreidoshow-dub-720p.mp4',
                       'genre': ''},

                       {'name': 'O Touro Ferdinando',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTIwMDI0NjQ4OF5BMl5BanBnXkFtZTgwNjU0MzAyNDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://chronos.feralhosting.com/locaweb123/2017/filmes/2017/0t0ur0f3rd1n4nd0.mp4',
                       'genre': 'FILMES'},

                       {'name': 'O Touro Ferdinando',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTIwMDI0NjQ4OF5BMl5BanBnXkFtZTgwNjU0MzAyNDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://dropapk.com/vidembed-i34st9i3nxhp.mp4',
                       'genre': 'LANÃ‡AMENTOS 2018'},

                       {'name': 'O Touro Ferdinando',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTIwMDI0NjQ4OF5BMl5BanBnXkFtZTgwNjU0MzAyNDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://dropapk.com/vidembed-lqm6xzsyuk9r.mp4',
                       'genre': 'Animação'},

                       {'name': 'PLANETA DOS MACACOS: A GUERRA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDNmYTQzMDEtMmY0MS00OTNjLTk4MjItMDZhMzkzOGI3MzA0XkEyXkFqcGdeQXVyNjk5NDA3OTk@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/cVs6wlIwLTILfZ5Fn7W6go8GKJo5b1hNIIaKWPvgTplCee6yyeb-nugKOpr_TXNw4V2gMFWYyw=m22',
                       'genre': 'Filmes'},

                       {'name': 'PLANETA DOS MACACOS: A GUERRA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDNmYTQzMDEtMmY0MS00OTNjLTk4MjItMDZhMzkzOGI3MzA0XkEyXkFqcGdeQXVyNjk5NDA3OTk@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/cVs6wlIwLTILfZ5Fn7W6go8GKJo5b1hNIIaKWPvgTplCee6yyeb-nugKOpr_TXNw4V2gMFWYyw=m37',
                       'genre': 'Filmes'},

                       {'name': 'QUATRO VIDAS CACHORRO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDQ4NjkxNzgzN15BMl5BanBnXkFtZTgwMjAzODQ4OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://ia601500.us.archive.org/4/items/lua4vidacachorro/lua4vidacachorro.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'QUATRO VIDAS CACHORRO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDQ4NjkxNzgzN15BMl5BanBnXkFtZTgwMjAzODQ4OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://ia601500.us.archive.org/4/items/lua4vidacachorro/lua4vidacachorro.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'QUATRO VIDAS DE UM CACHORRO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDQ4NjkxNzgzN15BMl5BanBnXkFtZTgwMjAzODQ4OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://ia601500.us.archive.org/4/items/lua4vidacachorro/lua4vidacachorro.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Quatro Vidas de um Cachorro (Leg)',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDQ4NjkxNzgzN15BMl5BanBnXkFtZTgwMjAzODQ4OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://userscloud.com/embed-vczn0auvdr0z.html',
                       'genre': 'Filmes'},

                       {'name': 'Star Wars - Os ultimos Jedi',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://ia601501.us.archive.org/1/items/LHMTVfilmes/S.W-O.U.J.LHMTv.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'STAR WARS - OS ÚLTIMOS JEDI TS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://ia601507.us.archive.org/34/items/SWOUJTS/SW-OUJ-TS.MP4',
                       'genre': 'Filmes'},

                       {'name': 'STAR WARS OS ULTIMOS JEDI',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://srv1.unitplay.net/stream/720/181808-star-wars-the-last-jedi.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Terra Selvagem',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUyMjU1OTUwM15BMl5BanBnXkFtZTgwMDg1NDQ2MjI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/terraselvagem-dub-720p.mp4',
                       'genre': ''},

                       {'name': 'THE BIG SICK',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWM4YzZjOTEtZmU5ZS00ZTRkLWFiNjAtZTEwNzIzMDM5MjdmXkEyXkFqcGdeQXVyNDg2MjUxNjM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://cecegeek@goo.gl/hR6Nxu',
                       'genre': ''},

                       {'name': 'The Post -A Guerra Secreta',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjQyMjEwOTIwNV5BMl5BanBnXkFtZTgwOTkzNTMxNDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://dropapk.com/vidembed-29yq99q8eop6.mp4',
                       'genre': 'Lançamentos 2017'},

                       {'name': 'THE POST: A GUERRA SECRETA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjQyMjEwOTIwNV5BMl5BanBnXkFtZTgwOTkzNTMxNDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/w0HZcaFnrgaRoJn7m5xpZ2kYnocCs0us6aCXDIfLKDFFeMWiAKk8qkGHRKmtq0qJOq1gWNkkg-o=m37',
                       'genre': 'Filmes'},

                       {'name': 'Thor Ragnarok',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://bit.ly/2zOMTbe?RTNews',
                       'genre': 'Filmes'},

                       {'name': 'Thor: Ragnarok',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.youtube.com/watch?v=FMYVZ0JwfeI',
                       'genre': 'Trailers de Filmes HD'},

                       {'name': 'THOR: RAGNAROK(QUALIDADE CINEMA)',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://ia601507.us.archive.org/26/items/THLIJUSRAG/44694903787a4f7135996751eacc1fdf.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Todo o Dinheiro do Mundo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjY3Mjg0OTc1OF5BMl5BanBnXkFtZTgwNDU0MzAyNDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/allthemoneyintheworld-leg-720p.mp4',
                       'genre': ''},

                       {'name': 'Trama Fantasma',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUxODcwOTU2Nl5BMl5BanBnXkFtZTgwOTUzNjY2NDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/phantomthread-leg-720p.mp4',
                       'genre': ''},

                       {'name': 'Três Anúncios Para um Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMxNzgwMDUyMl5BMl5BanBnXkFtZTgwMTQ0NTIyNDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://dropapk.com/vidembed-14b3n64o6i71.mp4',
                       'genre': 'Lançamentos 2018'},

                       {'name': 'TV Geral',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzg0NGE0N2MtYTg1My00NTBkLWI5NjEtZTgyMDA0MTU4MmIyXkEyXkFqcGdeQXVyMTU2NTcyMg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://fms1.tacitus.com.br:1935/tvgeral/tvgeral/live.m3u8',
                       'genre': 'BRAZIL'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/3/v6/z1zlf_tnl_2 8.jpg?ts=20140530223429,O Ritual',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjAzMzAyMDI4Ml5BMl5BanBnXkFtZTgwODMwOTY2NDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/v6/z1zlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'VIAGEM DAS GAROTAS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMwNTEzODUwMV5BMl5BanBnXkFtZTgwNjE5NjA5MjI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://ia801500.us.archive.org/34/items/V.D.G.2017.Dub.720p.Up.By.Ejds27/V.D.G.2017.Dub.720p.Up.By.Ejds27.mp4',
                       'genre': 'Filmes'},

                       {'name': 'VIVA A VIDA E UMA FESTA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjQ5NjM0Y2YtNjZkNC00ZDhkLWJjMWItN2QyNzFkMDE3ZjAxXkEyXkFqcGdeQXVyODIxMzk5NjA@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://srv1.unitplay.net/stream/720/354912-coco.mp4',
                       'genre': 'Filmes'},

                       {'name': 'When We Rise',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjYxNTdiZmYtNDk1MS00YjE4LTgzYTItNDBmZWJhYWVmM2Y1XkEyXkFqcGdeQXVyMzIzODgwODU@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=1cc47c9c7d27a61a',
                       'genre': 'When We Rise Day DUB'},

                       {'name': 'When We Rise',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjYxNTdiZmYtNDk1MS00YjE4LTgzYTItNDBmZWJhYWVmM2Y1XkEyXkFqcGdeQXVyMzIzODgwODU@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=44364d1db7d997d1',
                       'genre': 'When We Rise Day DUB'},

                       {'name': 'When We Rise',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjYxNTdiZmYtNDk1MS00YjE4LTgzYTItNDBmZWJhYWVmM2Y1XkEyXkFqcGdeQXVyMzIzODgwODU@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=8e6139595cfef08b',
                       'genre': 'When We Rise Day DUB'},

                       {'name': 'When We Rise',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjYxNTdiZmYtNDk1MS00YjE4LTgzYTItNDBmZWJhYWVmM2Y1XkEyXkFqcGdeQXVyMzIzODgwODU@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=9f22474c6a972a1a',
                       'genre': 'When We Rise Day DUB'},

                       {'name': 'When We Rise',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjYxNTdiZmYtNDk1MS00YjE4LTgzYTItNDBmZWJhYWVmM2Y1XkEyXkFqcGdeQXVyMzIzODgwODU@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=31a7dd6944af17b8',
                       'genre': 'When We Rise Day DUB'},

                       {'name': 'When We Rise',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjYxNTdiZmYtNDk1MS00YjE4LTgzYTItNDBmZWJhYWVmM2Y1XkEyXkFqcGdeQXVyMzIzODgwODU@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=aaee9eb4da2215ef',
                       'genre': 'When We Rise Day DUB'},

                       {'name': 'When We Rise',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjYxNTdiZmYtNDk1MS00YjE4LTgzYTItNDBmZWJhYWVmM2Y1XkEyXkFqcGdeQXVyMzIzODgwODU@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=e75a8194bfb1ca2d',
                       'genre': 'When We Rise Day DUB'},

                       {'name': 'When We Rise',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjYxNTdiZmYtNDk1MS00YjE4LTgzYTItNDBmZWJhYWVmM2Y1XkEyXkFqcGdeQXVyMzIzODgwODU@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=69378663a358a3f0',
                       'genre': 'When We Rise Day DUB'},

                       {'name': '13 HORAS: OS SOLDADOS SECRETOS DE BENGHAZ',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjY0OWVjMGQtNTIzZi00OGU5LWI4N2EtMGU0YzQ4OWM4ZmVhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/SQGczfwJ4hhgyrn1Y3UFFGeif1XYfDb7UwAhszW1R5Zr3li9j9yq63kCJQwnLwfappT0Mxgb3obZwJF93xmsZ5TwotUrWy0qKXYBYlVWxwhkciHavNqqczgnlnAo5Y-WWteAFw=m22',
                       'genre': 'Filmes'},

                       {'name': 'A Bailarina',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjEzMmFlNWUtYTFhOC00ZDMxLTllZmItZjc3ODMwNTk2ZmNlXkEyXkFqcGdeQXVyNTY2ODgzODg@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/nvmByp8yfLab_-e09faGxwUMhUslIyJrBO4k71v5hoU6ixyamLJ2z4gr-865tEhMqM4iCRo-hGs=m37',
                       'genre': 'Filmes'},

                       {'name': 'A Chegada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/Zez97miuWHVG-P89vzDyMt4MiwmAnklQnoFpcvfffeOQFNGokhhnUtcWaKaD8lxqCaFPhm7evlk=m37',
                       'genre': 'Filmes'},

                       {'name': 'A Garota no Trem',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzFlMjA0ZmUtZWI0Mi00ZGJkLTlmMmYtZmE1ODZiMjhjMGM0XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/MTrtj0NMApblOwZumkgvdnu1f787mOjgDxJkL80LWXuHXgipPRKAGLOH-q2ttY4cTqkBXljRzum4xiSCRbchsBV4yCSHjngiv0j7=m18',
                       'genre': 'Filmes'},

                       {'name': 'Águas Rasas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA1MTA4MzU4Ml5BMl5BanBnXkFtZTgwNjUxNjczODE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/NX5DSgb7M7Mm0WtGPr1E8KUYHv9cDfHizseLFIqTXvMzwYKyFtk9D-GJ6_eJsZ4cR6GNYhJLNeazf3V-v1pjHXJzZlCT43xkAaCTurov9A6lAFFWM0eBc-KeD6K23ZFO_MPsZTyztw=m22',
                       'genre': 'Filmes'},

                       {'name': 'Animais Fantásticos e Onde Habitam',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMxOTM1OTI4MV5BMl5BanBnXkFtZTgwODE5OTYxMDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/bvbDzIVAZD5F9hdjL6CYdC5fDNqPe-BCu8n4rXZ-1eZ0Xp1fHrIKSI9kZLw2GNT8cFaAjGWrT7jHRv-nkw=m37',
                       'genre': 'Filmes'},

                       {'name': 'ANIMAIS FANTASTICOS E ONDE HABITAM',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMxOTM1OTI4MV5BMl5BanBnXkFtZTgwODE5OTYxMDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/BekfxQDO3gmUZLwqbZ5Rn8_9ClA6-5d6K2Wdr4zxz0HE4d0bSI-DMY6FHLmEqzwVRNaRYhaGrRuJ=m22',
                       'genre': 'Filmes'},

                       {'name': 'Batman ?A Piada Mortal',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTdjZTliODYtNWExMi00NjQ1LWIzN2MtN2Q5NTg5NTk3NzliL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/CwT0p4l2PqaETJSq8RYal-aHchSxAAfk1yuiGvctb4kXHofTgFLDys7R4ayBSZIE1lD0_tFF=m22',
                       'genre': 'Filmes'},

                       {'name': 'BATMAN A PIADA MORTAL',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTdjZTliODYtNWExMi00NjQ1LWIzN2MtN2Q5NTg5NTk3NzliL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://srv1.unitplay.net/stream/720/382322-batman-the-killing-joke.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Batman Vs Superman',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYThjYzcyYzItNTVjNy00NDk0LTgwMWQtYjMwNmNlNWJhMzMyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/4A0JHBuotyS1_THZ-zipwwE6iKg8M8OZGoZFdXpFEv-h_BKIq15BMkaBqNpSaQFxfE1Hc1fpTQ=m18',
                       'genre': 'Filmes'},

                       {'name': 'COMO EU ERA ANTES DE VOCÊ',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ2NjE4NDE2NV5BMl5BanBnXkFtZTgwOTcwNDE5NzE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/r39D5cypghb7h9jiGOs778XFeZrhhw_5kvz2n9n7yDiFzhvLmEmYtw_pYu8mUdMrG364VW3K5g=m22',
                       'genre': 'Filmes'},

                       {'name': 'COMO EU ERA ANTES DE VOCÊ',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ2NjE4NDE2NV5BMl5BanBnXkFtZTgwOTcwNDE5NzE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/r39D5cypghb7h9jiGOs778XFeZrhhw_5kvz2n9n7yDiFzhvLmEmYtw_pYu8mUdMrG364VW3K5g=m37',
                       'genre': 'Filmes'},

                       {'name': 'Esquadrao Suicida',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjM1OTMxNzUyM15BMl5BanBnXkFtZTgwNjYzMTIzOTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/UYE_Ha3mQpaxybvZKAgKBXJdKf0hcp2-H_3wqLKQvrNg1LfPHyUkjX_PImuI--vA4Kjok4i1NA=m18',
                       'genre': 'Filmes'},

                       {'name': 'ESQUADRÃO SUICIDA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjM1OTMxNzUyM15BMl5BanBnXkFtZTgwNjYzMTIzOTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/i3iaW0lL2noAYWZ9lsVskZqhhtuB-s7kJob3U5DBPhDfLXoapni8Y3ELuu1Nju6LfyVLILkJvw=m37',
                       'genre': 'Filmes'},

                       {'name': 'Festa da Salsicha',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjkxOTk1MzY4MF5BMl5BanBnXkFtZTgwODQzOTU5ODE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh4.googleusercontent.com/3Vh5SjUJB15gMSSkzc7TRgTufsDEb7wEKmnPRq6iZTMAu8rxcBuhxDp7UalV0TrfhsEX3oArE79mas7VhSDkAE44VbgRduVHOBqGKcckNvT4OK91ksTEgsJsEQGvSqEng17Phw=m18',
                       'genre': 'Filmes'},

                       {'name': 'FOME DE PODER',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzExNDg0MDk1M15BMl5BanBnXkFtZTgwNzE1Mjg0MDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/f5sbqUJeIUlMaLSUKbg1R6mQMNdcMSE2z3Cu1An95DOOadsrW3wGl6FyafpmxGx6BbhuEZz-_g=m22',
                       'genre': 'Filmes'},

                       {'name': 'FOME DE PODER',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzExNDg0MDk1M15BMl5BanBnXkFtZTgwNzE1Mjg0MDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/f5sbqUJeIUlMaLSUKbg1R6mQMNdcMSE2z3Cu1An95DOOadsrW3wGl6FyafpmxGx6BbhuEZz-_g=m37',
                       'genre': 'Filmes'},

                       {'name': 'Invocação do Mal 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjU5OWVlN2EtODNlYy00MjhhLWI0MDUtMTA3MmQ5MGMwYTZmXkEyXkFqcGdeQXVyNjE5MTM4MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/XTQw5h1Gxrb4-C1pKOgl5u0cFhAq6vEvnIHjo7Y55v5b5gCZT1PZsci1_biu9cSu3Fnk6AqrShOpcjrl=m22',
                       'genre': 'Filmes'},

                       {'name': 'Jack Reacher Sem Retorno',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODQ3ODQ3NDI4NV5BMl5BanBnXkFtZTgwMDY1Mzk5OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/Jd15d41XxNqowEcSJ4qPgV54edg8Jp-f7yFLcFO6aBIMTrsVis_2tymM55FpLgh1ljssx-JpiMFfxN0EXoTAwEQNEOeMto9V-OmC=m18',
                       'genre': 'Filmes'},

                       {'name': 'Mogli - O Menino Lobo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc3NTUzNTI4MV5BMl5BanBnXkFtZTgwNjU0NjU5NzE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/8SGxnIks_yxCJCb5rwTRjkW5cFQgpWvoGsnAKPtFZR-DHxPMyKtd0q0VaemR6Ezid13MTISF=m22',
                       'genre': 'Filmes'},

                       {'name': 'MOONLIGHT (480p)',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzQxNTIyODAxMV5BMl5BanBnXkFtZTgwNzQyMDA3OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://str03.vidoza.net/kipkgzrlrwmthhxdunhe7bcorjfwjmvwiv73reyylmc53fjzhqph4hpe35aa/v.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Nerve - Um Jogo Sem Regras',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUzOTg1OTM4NV5BMl5BanBnXkFtZTgwMTg2Mjg0OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/GPve_brtcr1s4U2mp5FaS8sNlu-UYPFXo6PgXOMH6uNnRlhf1J2DVtt8MzkHZBNJaS1w3yNwxrjvnQ=m18',
                       'genre': 'Filmes'},

                       {'name': 'NERVE - UM JOGO SEM REGRAS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUzOTg1OTM4NV5BMl5BanBnXkFtZTgwMTg2Mjg0OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/jEKYBK8n_Bf__mwgWPDzoAuSvpTh9GphFaibIVp3RlK5Yb-76eRZxED_citGu8vzxdqTcxeY=m22',
                       'genre': 'Filmes'},

                       {'name': 'Procurando Dory',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzg4MjM2NDQ4MV5BMl5BanBnXkFtZTgwMzk3MTgyODE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/pLIibDJQa43iKaO7OFR4pAZwfbVMWjN9dKV0HMdNpVystH6o5OjlOqZLRI45iHcGptg-G9gDGw=m18',
                       'genre': 'Animação'},

                       {'name': 'Quando as luzes se apagam',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg1OTkxNDgyMV5BMl5BanBnXkFtZTgwMjEzNTc0ODE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/4-fKaPfKv0RskZ-IFZjOsV4x5lh-7EpjUGHRkKy_oM6cPiHJP4fZ8eKoFh8zKdGvtmMfE9bpZQ=m18',
                       'genre': 'Filmes'},

                       {'name': 'Rua Cloverfield 10',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjEzMjczOTIxMV5BMl5BanBnXkFtZTgwOTUwMjI3NzE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/4iMAv2bH3frbK9tSXgfVs6zlp8z4Pq3wfZ_qiPcyuntYwbQ5xCZPprBX_SDEBR6c7rqbsANz=m37',
                       'genre': 'Filmes'},

                       {'name': 'Sete Homens e um Destino',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUzNTc0NTAyM15BMl5BanBnXkFtZTgwMTk1ODA5OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/3fhlUcHsShRcNGdP2hlR6ruqgm5G0_ZeWK-MfqHv_pM12al7YVPwgrC1QhwaF7RHgoGJvRDV=m37',
                       'genre': 'Filmes'},

                       {'name': 'Zootopia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTMyMjEyNzIzMV5BMl5BanBnXkFtZTgwNzIyNjU0NzE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/YXgpbO_-lErksFrunt2vRC03hxC9a3ATFBJA3fyW6bC750jRbLam3AVRottdTjhHt_nPppuMzQ=m18',
                       'genre': 'Animação'},

                       {'name': '007 Contra Spectre',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOWQ1MDE1NzgtNTQ4OC00ZjliLTllZDAtN2IyOTVmMTc5YjUxXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/wTUraM-5GJ40aOX4IpxZCRxLp7ScKEkisHoKskbda9XZKWM2C45RAQQj3iGfqegnaI80S9FK_yI=m37',
                       'genre': 'Filmes'},

                       {'name': 'A Grande Aposta',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDc4MThhN2EtZjMzNC00ZDJmLThiZTgtNThlY2UxZWMzNjdkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/14UquWBiDVC-tmdo8OvLEI4sYBA1qProNMEjxD1HxvNIDoMbc1Vv5Gjfbk6FlV3jRus=m37',
                       'genre': 'Filmes'},

                       {'name': 'À Prova de Fogo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE3MDU2NzQyMl5BMl5BanBnXkFtZTgwMzQxMDQ3NTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/viKOBIAKvGH89cNqhv3Eybba8UeN4DiUzykFqXelZp7cN7Ia6XMD_G4fSjQZ9Vl5bhPcmsDStU6KKuCPtQ=m22',
                       'genre': 'Filmes'},

                       {'name': 'Bridge of Spies',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjIxOTI0MjU5NV5BMl5BanBnXkFtZTgwNzM4OTk4NTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/EKakvXIcmjumFFIlWxVEOobMf70Lli1eqcpGK0WNBHW-_KpRXlrM7VRn2mw0EorVsLg=m22',
                       'genre': 'Filmes'},

                       {'name': 'Como Sobreviver a um Ataque Zumbi',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4NjczNjE4OV5BMl5BanBnXkFtZTgwODk0MjQ5NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/LvrcUwwT8mrySaq6XKUNNkP7rCFc8sxYUcghk1u1f2kP_bXJg1eWBPzUiy3qQxfIbeTiAWCjeg=m18',
                       'genre': 'Filmes'},

                       {'name': 'DESCOMPENSADA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ4MjgwNTMyOV5BMl5BanBnXkFtZTgwMTc1MjI0NDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/0WEfaAmGcn4C6TjkE2kbf4vn7EoZdQEgaWwjbRWhAzthxUK7Gkr8lHjthKxRqCt8hm0Lxam0mtDVEg=m22',
                       'genre': 'Filmes'},

                       {'name': 'DIVERTIDA MENTE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/IhnCG4aSvd-FtE6bsE7qENuz7EnJz8JzCURTLPmoG1V6IwpISpumNXWAlVYqDfxzqSdjgdSEw_0INw=m22',
                       'genre': 'ANIMAÇÃO'},

                       {'name': 'EU VOCÊ E A GAROTA QUE VAI MORRER (480p)',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTA1NzUzNjY4MV5BMl5BanBnXkFtZTgwNDU0MDI0NTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://ia800409.us.archive.org/19/items/EuVoceEAGarotaQueVaiMorrerDublado/Eu%2C%20Voc%C3%AA%20e%20a%20Garota%20que%20Vai%20Morrer%20Dublado.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Joy: o nome do sucesso',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzRiOWZmMzUtZTJiOC00MjQ1LTkwMjgtNzhlYzBmODAzYTA0XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/cHEVdnAbZY9jKXy3uPzhH7kgnFe-o7faVHfEgYRKFLPZA-vK_PrP9xcPwnyRN_PMbAc=m37',
                       'genre': 'Filmes'},

                       {'name': 'Le revenant',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BY2FmODc2N2QtYmY3MS00YTMwLWI2NGYtZWRmYWVkNjFjZmI0XkEyXkFqcGdeQXVyNTMxMjgxMzA@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/ETj5ibzaQdpLIypKbGa1Cy5-0p91jazaRlvHLe1Z1kfv61Sp0_th_EhGq6nqLf79mdE=m22',
                       'genre': 'Filmes'},

                       {'name': 'Maze Runner: The Scorch Trials',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE3MDU2NzQyMl5BMl5BanBnXkFtZTgwMzQxMDQ3NTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/PJzY6hjNNX2z4Alnw4vMD6SWcD0EsafkFYNTGaKwjJTxa7Ynr0UxXnTEXPXcKfHT6CXbrYdV=m18',
                       'genre': 'Filmes'},

                       {'name': 'Mission: Impossible 5 - Rogue Nation',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTFmNDA3ZjMtN2Y0MC00NDYyLWFlY2UtNTQ4OTQxMmY1NmVjXkEyXkFqcGdeQXVyNTg4NDQ4NDY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/8WS27fLDMFcAx46wVDVLhRNKrSMrhi0AHOJdPCVt9FiMlbi4smrIqG57Aumm1GOqfs8=m22',
                       'genre': 'Filmes'},

                       {'name': 'No Coração do Mar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5NzUwODExM15BMl5BanBnXkFtZTgwNjM0MzE4NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh4.googleusercontent.com/UqFxWMNAuGgppIU6UYfPVvvIuXeSI_2AgcX1RujszJB3q74kUHfAawR7uNAgEDXPnrb1H_Z7=m18',
                       'genre': 'Filmes'},

                       {'name': 'O BOM DINOSSAURO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc5MTg2NjQ4MV5BMl5BanBnXkFtZTgwNzcxOTY5NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/_4WExwFgtC-3rRS5RZLQBBUD4K_RUz-bmbbDBdf258fgboZAWMhS-WSpXTUORCd6vzhh4XN1KBMKbA=m22',
                       'genre': 'ANIMAÇÃO'},

                       {'name': 'O Experimento de Aprisionamento de Stanford',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUyNDIyMTA4NV5BMl5BanBnXkFtZTgwODM2MDMxNjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/MvD0Rk2HfSz8C7znsy_cWy_16oAs6XrNrbS0HF4W_Jr_8FwzAEqivde9bxTAIWemDto=m37',
                       'genre': 'Filmes'},

                       {'name': 'Olhos da JustiCa',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE0ODU1NDE0Ml5BMl5BanBnXkFtZTgwNzc4Njc3NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/o5KhJ9cp8_LWabKvL1wbDXj7JiAdwPmMcsaVLrsWAy0v1L5f5MzXrrDhxwPH-PjWeq8=m37',
                       'genre': 'Filmes'},

                       {'name': 'PEGANDO FOGO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjEzNTk2OTEwNF5BMl5BanBnXkFtZTgwNzExMTg0NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/R7zPZ3vRVq0ePWnixREGPw3izlYMqAy0KzEtlQwMzGWmxrT3NaCNupPkBpf0af0IN7rAYe8GwzXiFA=m22',
                       'genre': 'Filmes'},

                       {'name': 'PERDIDO EM MARTE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/uVJyJt48gmoyWcj0aSuyZIMFvYk5pFJJSZs_irlAlMgjSsUbr2IOcQflB69BOK4wB0eZvdbRKDTwRw=m22',
                       'genre': 'Filmes'},

                       {'name': 'Ponte dos Espi??',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjIxOTI0MjU5NV5BMl5BanBnXkFtZTgwNzM4OTk4NTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/EKakvXIcmjumFFIlWxVEOobMf70Lli1eqcpGK0WNBHW-_KpRXlrM7VRn2mw0EorVsLg=m37',
                       'genre': 'Filmes'},

                       {'name': 'Ponte dos Espiões',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjIxOTI0MjU5NV5BMl5BanBnXkFtZTgwNzM4OTk4NTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/EKakvXIcmjumFFIlWxVEOobMf70Lli1eqcpGK0WNBHW-_KpRXlrM7VRn2mw0EorVsLg=m37',
                       'genre': 'Filmes'},

                       {'name': 'Rastro de Maldade',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzQ0MzE4OTUzMF5BMl5BanBnXkFtZTgwODAyNzI3NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/bCGa7nVOTGt73WW21Xb--qjbtJ4zhP2mPushXKGQgSQpEz64PAOaaMikAFKTdCF_IkaroHq9=m22',
                       'genre': 'Filmes'},

                       {'name': 'SPECTRE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOWQ1MDE1NzgtNTQ4OC00ZjliLTllZDAtN2IyOTVmMTc5YjUxXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://goo.gl/3KGMLf',
                       'genre': ''},

                       {'name': 'Steve Jobs',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE0NTA2MTEwOV5BMl5BanBnXkFtZTgwNzg4NzU2NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/imB33pdkPNiDDe7ZXUbFWZ5bcR44_kyO2cNyaUFIQrAz4JC1CZakX6K_YOvnx8nhvXo=m22',
                       'genre': 'Filmes'},

                       {'name': 'Steve Jobs',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE0NTA2MTEwOV5BMl5BanBnXkFtZTgwNzg4NzU2NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/imB33pdkPNiDDe7ZXUbFWZ5bcR44_kyO2cNyaUFIQrAz4JC1CZakX6K_YOvnx8nhvXo=m37',
                       'genre': 'Filmes'},

                       {'name': 'TEF TV',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA1MTc1NTg5NV5BMl5BanBnXkFtZTgwOTM2MDEzNzE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://server10.streaming-pro.com:1937/live/teftvlive/playlist.m3u8',
                       'genre': ''},

                       {'name': 'The Stanford Prison Experiment',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUyNDIyMTA4NV5BMl5BanBnXkFtZTgwODM2MDMxNjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/MvD0Rk2HfSz8C7znsy_cWy_16oAs6XrNrbS0HF4W_Jr_8FwzAEqivde9bxTAIWemDto=m22',
                       'genre': 'Filmes'},

                       {'name': 'Um Senhor Estagiário',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUyNjE5NjI5OF5BMl5BanBnXkFtZTgwNzYzMzU3NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/fIa2wzTCdSJ9aDWQFK7GSizH4D6-YXRLaDZTVTCWPGI_fVZ3hlaouPT84fm6KnDDeDPD0nGH40o=m37',
                       'genre': 'Filmes'},

                       {'name': 'Uma Longa Jornada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzIzMjg0NjQwNF5BMl5BanBnXkFtZTgwODAwOTE4MzE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/45cszbfsUoiMdtkR0P37m4OrBMCir00iP7GxCFsDSlNjy2MEnXhxg3U554KsHty1SDQJLBpPmA=m18',
                       'genre': 'Filmes'},

                       {'name': 'Vingadores: Era de Ultron',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTM4OGJmNWMtOTM4Ni00NTE3LTg3MDItZmQxYjc4N2JhNmUxXkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/2WCKvatr6M5zFWcFzS1Gg4Vt4UmNarmHUaklRJ7ygkqNJSlrP9oNUiMfwMZyxJhZKbE=m22',
                       'genre': 'Filmes'},

                       {'name': '3 Days to Kill',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzM0MjE0Nzg1N15BMl5BanBnXkFtZTgwODA4ODE4MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/9XgzdJ2yIHMMFu3fFFOIB6YI__lp9yZRTCH2UGRRhWrSBmyAmuQttr-agrH1ty2HKDE=m22',
                       'genre': 'Filmes'},

                       {'name': '3 DAYS TO KILL',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzM0MjE0Nzg1N15BMl5BanBnXkFtZTgwODA4ODE4MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/3days.mp4',
                       'genre': ''},

                       {'name': '3 Dias Para Matar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzM0MjE0Nzg1N15BMl5BanBnXkFtZTgwODA4ODE4MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/Hn5WH9GJWyZGJXFzwMJceY8H-37G0cSXspugVJWjvl-9TVHN_ijKdKftGH8uJS0DbHk=m18',
                       'genre': 'Filmes'},

                       {'name': '300 RISE OF AN EMPIRE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTEwNTU2MjAwMDdeQTJeQWpwZ15BbWU3MDk2Njc2Njk@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/300rise.mp4',
                       'genre': ''},

                       {'name': 'As Aventuras de Tadeo 2 – O Segredo do Rei Midas',
                       'thumb': 'http://www.lhmtv.tk/channellogo/filmes.png',
                       'video': 'http://ia601501.us.archive.org/1/items/LHMTVfilmes/A.A.D.T.2.-O.S.D.R.M.LHMTv.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Dracula - A Historia Nunca Contada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTkzNzI1OTI4N15BMl5BanBnXkFtZTgwNTQ2NzEwMjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/94NPclUDQdLLaGAmIMSJvzOeCh4oi3bLDHVjJ23GM6D9qhFoOTRGUsPzhxdd3E2_c9Y=m18',
                       'genre': 'Filmes'},

                       {'name': 'Garota Exemplar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjgwY2E1N2QtNDJkMi00YzE4LThiYTItYWI5YmE4NWMzMGFhXkEyXkFqcGdeQXVyMjU3OTA4NzQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/9GUZt6MmLVbxGm0r2K2ht6-HHt-aPCPZPQsCWDndwBKmn4fYQvkIYWllrPXxmYPRFNk=m18',
                       'genre': 'Filmes'},

                       {'name': 'Garota Exemplar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjgwY2E1N2QtNDJkMi00YzE4LThiYTItYWI5YmE4NWMzMGFhXkEyXkFqcGdeQXVyMjU3OTA4NzQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/9GUZt6MmLVbxGm0r2K2ht6-HHt-aPCPZPQsCWDndwBKmn4fYQvkIYWllrPXxmYPRFNk=m18',
                       'genre': 'Filmes'},

                       {'name': 'Interestelar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/NloiK_YE_FqLRYIcZbOY_h5YIxn_H5azNHsFSmOxEIpARPHhDS6IfBCUhtRZQL34FezPAlri=m18',
                       'genre': 'Filmes'},

                       {'name': 'INTERESTELAR',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/lKEseOkFdcF6u5uXzZ6pQHHohPbgPnIid1xNEiUxDU-YGAFRqqrxQ-zdxN7-oO4ixmJl6mzpRVDdUQ=m22',
                       'genre': 'Filmes'},

                       {'name': 'INTERESTELAR -',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/r4LHwjkrWxlgh6u1O_zv69HMoi8Xz1XeVzgpO9sQzwCmxuwK6DJKG616WOQaxMOXCtBbYyU50w=m37',
                       'genre': 'Filmes'},

                       {'name': 'Lucy',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODcxMzY3ODY1NF5BMl5BanBnXkFtZTgwNzg1NDY4MTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/1QIc9TZEmjJL7FSErdCay7Yz3gZPnlze3LFhPKh5wWyQb2-eqJ-DWPtCyy3V1ejyqfgBWbOyFQ=m22',
                       'genre': 'Filmes'},

                       {'name': 'LUCY',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODcxMzY3ODY1NF5BMl5BanBnXkFtZTgwNzg1NDY4MTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/4Ns_PBBtAJA4Aa7gJSSwKknN1ZSEdwJ8IRk1kRXgm9qVryfhBVqoz3j8SGTJZsX_1CasC87z=m22',
                       'genre': 'Filmes'},

                       {'name': 'LUCY',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODcxMzY3ODY1NF5BMl5BanBnXkFtZTgwNzg1NDY4MTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://archive.org/download/Lucy_Movie/Lucy.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Lucy',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODcxMzY3ODY1NF5BMl5BanBnXkFtZTgwNzg1NDY4MTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/R4LN1RIzx-pHxeP1UFv2uoyYWJy5TdViXS0MoI-WALumGmIBEB7T1UjwR7mHwnvylxNLtvHT=m18',
                       'genre': 'Filmes'},

                       {'name': 'MALEFICENT',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjAwMzAzMzExOF5BMl5BanBnXkFtZTgwOTcwMDA5MTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/maleficent.mp4',
                       'genre': ''},

                       {'name': 'Need for Speed',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ3ODY4NzYzOF5BMl5BanBnXkFtZTgwNjI3OTE4MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.youtube.com/watch?v=fnjU-R5H9TY',
                       'genre': 'Filmes'},

                       {'name': 'NEED FOR SPEED',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ3ODY4NzYzOF5BMl5BanBnXkFtZTgwNjI3OTE4MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/needforspeed.mp4',
                       'genre': ''},

                       {'name': 'NON STOP',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTI3NzcxMjkzMl5BMl5BanBnXkFtZTgwMDY0NTQ0MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/nonstop2014.mp4',
                       'genre': ''},

                       {'name': 'O Doador de Mem??s',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY1MTIxMjg2Ml5BMl5BanBnXkFtZTgwMjUyNzgwMjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/N9TMub2RfwPfRPC84_iWL4Ltp1PoBbcy8GEBWpexs3_5G3M4YRABEQ6wBqfT6xj7IyCVMNAY=m18',
                       'genre': 'Filmes'},

                       {'name': 'O Grande Hotel Budapeste',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzM5NjUxOTEyMl5BMl5BanBnXkFtZTgwNjEyMDM0MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/lDZ1Go8_QRiON5Kr2sBY36je52yAemlzO_CyzkA2hwh63poJsQhInwDaX4FxYGTA3ZPPPtB0=m18',
                       'genre': 'Filmes'},

                       {'name': 'O Melhor de mim',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzQ5Njg3Njk5N15BMl5BanBnXkFtZTgwODIwODIxMjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/_fnbOdAPZkrUV2uguCwpXyQDA0tqMnl9bnCeNCKdiYIuIiHcYM802g1NXiJKFTW5ZKmIXGEc9HY=m18',
                       'genre': 'Filmes'},

                       {'name': 'O Predestinado',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAzODc3NjU1NzNeQTJeQWpwZ15BbWU4MDk5NTQ4NTMx._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/i4nqlBz5Oo9MoU5zuJgQjNgb_MtJflhIykJON-BBtbbOENs5oGGO203PpjUZvPMjP7o=m18',
                       'genre': 'Filmes'},

                       {'name': 'O Sinal',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTA2MDc5MDQ2MTVeQTJeQWpwZ15BbWU4MDY4Njc3NDEx._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/roPPLf5td3SA2S8Zh8qIg0x255HVoMJyRsp6OJ1JJTrM2zgF0YlLS00MBEtyuFGVuAk=m18',
                       'genre': 'Filmes'},

                       {'name': 'OPERACAO BIG HERO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDliOTIzNmUtOTllOC00NDU3LWFiNjYtMGM0NDc1YTMxNjYxXkEyXkFqcGdeQXVyNTM3NzExMDQ@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/sLIOAAQSudIxfIHwsDSKiVFJQtgNu992U01S4U5K7e3PkL-xfsz6cNRYOOuJmkKenVLVc7IuWQ=m37',
                       'genre': 'Filmes'},

                       {'name': 'OperaCAo Big Hero',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDliOTIzNmUtOTllOC00NDU3LWFiNjYtMGM0NDc1YTMxNjYxXkEyXkFqcGdeQXVyNTM3NzExMDQ@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/JjOvAh6XY_3A4aXrmbOP9V7faL8fYa-Vrf6BV9MWSQiY4SaD30gCnE0pa9q_BgUs2glfxhAk=m18',
                       'genre': 'Filmes'},

                       {'name': 'Predestination',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAzODc3NjU1NzNeQTJeQWpwZ15BbWU4MDk5NTQ4NTMx._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/i4nqlBz5Oo9MoU5zuJgQjNgb_MtJflhIykJON-BBtbbOENs5oGGO203PpjUZvPMjP7o=m18',
                       'genre': 'Filmes'},

                       {'name': 'Simplesmente Acontece',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk0Mzg1MTU1MF5BMl5BanBnXkFtZTgwMjU3ODI2MzE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/NsLONrY0fGc_dTifnI3eTjbYVeraeVFVKDLqjVyBO5I50Cs1Oikgj4jzG2sFlgr2p-RLNdOPzQ=m18',
                       'genre': 'Filmes'},

                       {'name': 'Sin City: A Dama Fatal',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5ODYwNjgxMF5BMl5BanBnXkFtZTgwMTcwNzAyMjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/19nSJ-PeVnWUyMQ1pvPlyjTTubONX_6q0dlwuKYPqo2kPXMML2ArW3ofI9HXIl3yy30=m18',
                       'genre': 'Filmes'},

                       {'name': 'Sin City: A Dame to Kill For',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5ODYwNjgxMF5BMl5BanBnXkFtZTgwMTcwNzAyMjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/19nSJ-PeVnWUyMQ1pvPlyjTTubONX_6q0dlwuKYPqo2kPXMML2ArW3ofI9HXIl3yy30=m18',
                       'genre': 'Filmes'},

                       {'name': 'Sniper Americano',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTkxNzI3ODI4Nl5BMl5BanBnXkFtZTgwMjkwMjY4MjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/kxFv8YbaZhJVTSK_3v18NuhVtrZ69TT20ARUV7RCP_jRfV_6Sd05NHR6pWa-357iJzkK3g0y=m18',
                       'genre': 'Filmes'},

                       {'name': 'The Signal',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTA2MDc5MDQ2MTVeQTJeQWpwZ15BbWU4MDY4Njc3NDEx._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/roPPLf5td3SA2S8Zh8qIg0x255HVoMJyRsp6OJ1JJTrM2zgF0YlLS00MBEtyuFGVuAk=m18',
                       'genre': 'Filmes'},

                       {'name': 'Transcendence ?A Revolu?',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc1MjQ3ODAyOV5BMl5BanBnXkFtZTgwNjI1NDQ0MTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/r82c71Jyfm7IK9HA4HjlZ403Jysm_g_mOfuQ7rIJdanxZjkOCwe5FJMb2GUAtkiLvZw=m18',
                       'genre': 'Filmes'},

                       {'name': 'Uma Noite de Crime 2: Anarquia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE2ODMxMTk1Nl5BMl5BanBnXkFtZTgwMDEzNjEzMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/RCV1FlQjRd_XWhDogW3b42UgHTbrxAj_lwlKajLDfGuz5_ieDUvnD85Cfu7uoFcR2kY=m18',
                       'genre': 'Filmes'},

                       {'name': 'UMA NOITE DE CRIME 2: ANARQUIA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE2ODMxMTk1Nl5BMl5BanBnXkFtZTgwMDEzNjEzMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/RCV1FlQjRd_XWhDogW3b42UgHTbrxAj_lwlKajLDfGuz5_ieDUvnD85Cfu7uoFcR2kY=m18',
                       'genre': 'Filmes'},

                       {'name': 'Uma Noite de Crime: Anarquia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE2ODMxMTk1Nl5BMl5BanBnXkFtZTgwMDEzNjEzMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/frNORk8Y_jFr2pbwzYn39b147TLneaUZoSLophrhv2mAgkd-vxqmFfZY22MrvALWuU-jON6vmw1oH2vIvg=m22',
                       'genre': 'Filmes'},

                       {'name': 'X MEN - DIAS DE UM FUTURO ESQUECIDO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGIzNWYzN2YtMjcwYS00YjQ3LWI2NjMtOTNiYTUyYjE2MGNkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/sy2RKy-mpwDBEXRcYjiP8VIeo2-TwB-P3j8vF35sX9dTMp85DanwwHxv174RYk8PFd7wQB0dczKL9A=m22',
                       'genre': 'Filmes'},

                       {'name': ',Haven',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg4MzcxODA3OV5BMl5BanBnXkFtZTcwMTYzNDkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/p/im/zrdyb_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': '12 Anos de Escravidão',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjFkOGNjZjAtMzZjNS00ZjI2LTkwNjEtOWQ3NzQzOTBlMDA5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/3tPbMb5a1lZ7j_UnsVIWLcU9B4-FOZmlXapmxxk3_TtvPL6a8KzGbwCbLefu_JCnu7TMss3F=m22',
                       'genre': 'Filmes'},

                       {'name': '12 YEARS A SLAVE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjFkOGNjZjAtMzZjNS00ZjI2LTkwNjEtOWQ3NzQzOTBlMDA5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/12slave.mp4',
                       'genre': ''},

                       {'name': 'Além da Escuridão - Star Trek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk2NzczOTgxNF5BMl5BanBnXkFtZTcwODQ5ODczOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/K4eW0mgR0JiCYav5oXgt3Tmld8ONaSVhYuQpeitjSaQZ9FXJjymjwPPoul0h7PeF_bDMjKr40A=m22',
                       'genre': 'Filmes'},

                       {'name': 'AMERICAN HUSTLE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmM4YzJjZGMtNjQxMy00NjdlLWJjYTItZWZkYzdhOTdhNzFiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/hustle2013.mp4',
                       'genre': ''},

                       {'name': 'As Bem-Armadas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA2MDQ2ODM3MV5BMl5BanBnXkFtZTcwNDUzMTQ3OQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/Xu1jGTQafJwEW9avawfMaFDfnUJY5s6BTqwBunTaRWjV97Hzk_eGgAF3CyxKRRPICei0CSKKmBY=m18',
                       'genre': 'Filmes'},

                       {'name': 'DELIVERY MAN',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjIxNjc2MzMzMl5BMl5BanBnXkFtZTgwMjA5NjM0MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/deliveryman.mp4',
                       'genre': ''},

                       {'name': 'Fam?a do Bagulho',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5Njc0NDUxNV5BMl5BanBnXkFtZTcwMjYzNzU1OQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/VDSuK6zXc_5aPRxXUd3jbLPxE8VBSukn4gjG2Vb204OBx9ZBoi6slhqWL9S4ZiO5Bnp-Io6KUg=m18',
                       'genre': 'Filmes'},

                       {'name': 'Filth',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE2NTgyMzM0NV5BMl5BanBnXkFtZTgwNzkwNDE1MzE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/KXc5vMy513k4KtrLKQ8lKAAEtpD9TKVirsg1b5zsNPPUAnddm6yJSM75MmKCRfhdS-qPT8zVVQ=m22',
                       'genre': 'Filmes'},

                       {'name': 'Haven',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg4MzcxODA3OV5BMl5BanBnXkFtZTcwMTYzNDkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/h/16/yaylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Haven',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg4MzcxODA3OV5BMl5BanBnXkFtZTcwMTYzNDkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/p/im/zrdyb_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Haven',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg4MzcxODA3OV5BMl5BanBnXkFtZTcwMTYzNDkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/p/im/zrdyb_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Haven',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg4MzcxODA3OV5BMl5BanBnXkFtZTcwMTYzNDkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/h/16/yaylf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'João e Maria: Caçadores de Bruxas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA4MDQwODg2NV5BMl5BanBnXkFtZTcwNTc5ODc2OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://transfvanila1.com/videos/RedeCanais/RCFServer1/ondemand/JAOEMRA01.mp4',
                       'genre': 'Filmes'},

                       {'name': 'JoAo, Maria e a Bruxa',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA4MDQwODg2NV5BMl5BanBnXkFtZTcwNTc5ODc2OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/Emk-8KoqpdPyqmOlVsvCUSLfKHovnaNepdNbwFjK9yUHsDmRN3L9px-hXj9RvgVXOxCbPXrqog=m37',
                       'genre': 'Filmes'},

                       {'name': 'MONSTERS UNIVERSITY',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUyODgwMDU3M15BMl5BanBnXkFtZTcwOTM4MjcxOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/monsters2.mp4',
                       'genre': ''},

                       {'name': 'O Hobbit: A Desolação de Smaug',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzU0NDY0NDEzNV5BMl5BanBnXkFtZTgwOTIxNDU1MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/JwdCgqVAvKCSl9gYX33K-q1YYA6Euw7YBVhrwTePQCotqJBh4ttQaXlIAIryVD-ON0-3-8cmGTEQ2rnQFw=m22',
                       'genre': 'Filmes'},

                       {'name': 'O Homem Duplicado',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ2NzA5NjE4N15BMl5BanBnXkFtZTgwMjQ4NzMxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/R4OZPNsxMu8XaznHq-lgByXG12WUlRC9iuisojt_PN3P4KZf_fdtfAVTvJyq0YS-GqTU=m18',
                       'genre': 'Filmes'},

                       {'name': 'Oculus',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzE1NzM4MjEyNV5BMl5BanBnXkFtZTgwMjYzMjMzMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/NEilD3mr2kDwAF7-geNdmkjPsrlDD8hbd0KGzI23v37BkVdhIGPKK6lLMkjCTVYm6C4=m18',
                       'genre': 'Filmes'},

                       {'name': 'OLYMPUS HAS FALLEN',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTU0NmY4MWYtNzRlMS00MDkxLWJkODYtOTM3NGI2ZDc1NTJhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/fallen1.mp4',
                       'genre': ''},

                       {'name': 'Os Estagiarios',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjM1MzczMDgwOV5BMl5BanBnXkFtZTcwMDM4NjM2OQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/DC6oXusWKu25c3F6xUIHBcd00rYROt8gmgh5icoxGYkafoMrvRAECb0h8nSXai85RUqhDGbzlGRyzYYCe5_r5MH27SUPdIpyB1ulRqXEpn6gucjQFbwzX19HmQ561Hi8RloEDQ=m18',
                       'genre': 'Filmes'},

                       {'name': 'PRISONERS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg0NTIzMjQ1NV5BMl5BanBnXkFtZTcwNDc3MzM5OQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/prisoners.mp4',
                       'genre': ''},

                       {'name': 'SAVING MR BANKS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc0MTQ3NzE4Nl5BMl5BanBnXkFtZTcwMzA4NDM5OQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/savingbanks.mp4',
                       'genre': ''},

                       {'name': 'THE HUNGER GAMES: CATCHING FIRE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAyMjQ3OTAxMzNeQTJeQWpwZ15BbWU4MDU0NzA1MzAx._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/hungergames2.mp4',
                       'genre': ''},

                       {'name': 'THE INTERNSHIP',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjM1MzczMDgwOV5BMl5BanBnXkFtZTcwMDM4NjM2OQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/internship2013.mp4',
                       'genre': ''},

                       {'name': 'THE WOLF OF WALL STREET',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/thewolf2013.mp4',
                       'genre': ''},

                       {'name': 'THE WOLVERINE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzg1MDQxMTQ2OF5BMl5BanBnXkFtZTcwMTk3MjAzOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/thewolverine.mp4',
                       'genre': ''},

                       {'name': 'THIS IS THE END',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQxODE3NjM1Ml5BMl5BanBnXkFtZTcwMzkzNjc4OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/theend.mp4',
                       'genre': ''},

                       {'name': 'This Is the End',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQxODE3NjM1Ml5BMl5BanBnXkFtZTcwMzkzNjc4OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.youtube.com/watch?v=wXzlszZMJGc',
                       'genre': 'Filmes'},

                       {'name': 'WALTER',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODYwNDYxNDk1Nl5BMl5BanBnXkFtZTgwOTAwMTk2MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/U09HdrVkh8A_bYaeRMKjRhSfXtbI2A7h4HEfWaCxLbs1EK5l_tqUxhPqVk-OPGIYOBzIpT4BBBsolA=m22',
                       'genre': 'Filmes'},

                       {'name': 'A Beira do Abismo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc5MTE4MzY2N15BMl5BanBnXkFtZTcwNjMwNDc3Ng@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/v6/r1zlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'A Beira do Abismo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc5MTE4MzY2N15BMl5BanBnXkFtZTcwNjMwNDc3Ng@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/v6/r1zlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'BATMAN - O CAVALEIRO DAS TREVAS RESSURGE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/VguWnEeqTITH8RMHv0JRo-FkEDUaDEzDd7xi4CdtIwB1ZVTW8cUBQ91zB5jd2QfAcPJS59HWWGk_Fm9EPQ=m22',
                       'genre': 'Filmes'},

                       {'name': 'DETONA RALPH',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzMxNTExOTkyMF5BMl5BanBnXkFtZTcwMzEyNDc0OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/9huO2C9dXDtISDw46Bi376ZZ2wRyDZjfBDK75ImOBGjPDXag99U4XnzIklwaJRN-71LqONExBA=m22',
                       'genre': 'Filmes'},

                       {'name': 'DETONA RALPH',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzMxNTExOTkyMF5BMl5BanBnXkFtZTcwMzEyNDc0OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/9huO2C9dXDtISDw46Bi376ZZ2wRyDZjfBDK75ImOBGjPDXag99U4XnzIklwaJRN-71LqONExBA=m37',
                       'genre': 'Filmes'},

                       {'name': 'Django Livre',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://transfvanila1.com/videos/RedeCanais/RCFServer1/ondemand/DJNGLVR.mp4',
                       'genre': 'Filmes'},

                       {'name': 'john_carter_entre_dois_mundos',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDEwZmIzNjYtNjUwNS00MzgzLWJiOGYtZWMxZGQ5NDcxZjUwXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UY268_CR6,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/9tza4VOGRUU_ci03KHL26W9-5dEze1Ex1iZaCg_KaoN0_3gUwm3LCP_1aYB6FUJcpxV1lQjk=m22',
                       'genre': 'Filmes'},

                       {'name': 'O Hobbit: Uma Jornada Inesperada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTcwNTE4MTUxMl5BMl5BanBnXkFtZTcwMDIyODM4OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/pnahF0JFvYEyxMHVb2-fdR-qnKE4XdrYgiG3OzOyoYBUqVJ4vdLxipd_vxWgEiiKCUifm9w_fwQcypJbjw=m22',
                       'genre': 'Filmes'},

                       {'name': 'O Lugar Onde Tudo Termina',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjc1OTEwNjU4N15BMl5BanBnXkFtZTcwNzUzNDIwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/7m8ZSPDR-C15PoyAJYtfa2I1QfjM3nzerjeVuF-u0SOhZZ94EPcGBDesG2eNHUaTpn4=m18',
                       'genre': 'Filmes'},

                       {'name': 'PROMETHEUS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY3NzIyNTA2NV5BMl5BanBnXkFtZTcwNzE2NjI4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/prometheus.mp4',
                       'genre': ''},

                       {'name': 'THE BOURNE LEGACY',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc4Njk3MDM1Nl5BMl5BanBnXkFtZTcwODgyOTMxOA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/bourne4.mp4',
                       'genre': ''},

                       {'name': 'The Collection',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODQ0MDgzNDA0NV5BMl5BanBnXkFtZTcwNDM4MDQ1OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=14b160f262d6f7b7',
                       'genre': 'The Collection LEG'},

                       {'name': 'The Collection',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODQ0MDgzNDA0NV5BMl5BanBnXkFtZTcwNDM4MDQ1OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=662bd4b1bfb5b15a',
                       'genre': 'The Collection LEG'},

                       {'name': 'The Collection',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODQ0MDgzNDA0NV5BMl5BanBnXkFtZTcwNDM4MDQ1OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=40cdba803aa6b130',
                       'genre': 'The Collection LEG'},

                       {'name': 'The Collection',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODQ0MDgzNDA0NV5BMl5BanBnXkFtZTcwNDM4MDQ1OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=2d6f6006388c080f',
                       'genre': 'The Collection LEG'},

                       {'name': 'The Collection',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODQ0MDgzNDA0NV5BMl5BanBnXkFtZTcwNDM4MDQ1OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=701a055e5c511693',
                       'genre': 'The Collection LEG'},

                       {'name': 'The Collection',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODQ0MDgzNDA0NV5BMl5BanBnXkFtZTcwNDM4MDQ1OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=4bb3a9d091179658',
                       'genre': 'The Collection LEG'},

                       {'name': 'The Collection',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODQ0MDgzNDA0NV5BMl5BanBnXkFtZTcwNDM4MDQ1OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=a0aacadf02ee3264',
                       'genre': 'The Collection LEG'},

                       {'name': 'The Collection',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODQ0MDgzNDA0NV5BMl5BanBnXkFtZTcwNDM4MDQ1OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=97ef89c0bfb48e49',
                       'genre': 'The Collection LEG'},

                       {'name': 'The First Time',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMxNDI1OTY5NF5BMl5BanBnXkFtZTcwMDExOTY1OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.youtube.com/watch?v=Ebhdw3Rv0DY',
                       'genre': 'Filmes'},

                       {'name': 'THE HOBBIT AN UNEXPECTED JOURNEY',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTcwNTE4MTUxMl5BMl5BanBnXkFtZTcwMDIyODM4OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/hobbit1.mp4',
                       'genre': ''},

                       {'name': 'The Place Beyond the Pines',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjc1OTEwNjU4N15BMl5BanBnXkFtZTcwNzUzNDIwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/7m8ZSPDR-C15PoyAJYtfa2I1QfjM3nzerjeVuF-u0SOhZZ94EPcGBDesG2eNHUaTpn4=m18',
                       'genre': 'Filmes'},

                       {'name': 'THINK LIKE A MAN',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjExNTc4NDg3OV5BMl5BanBnXkFtZTcwNTMzNDAxNw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/thinklike1.mp4',
                       'genre': ''},

                       {'name': 'tvg-logo=http://pipocacombo.com/wp-content/uploads/2012/01/A-beira-do-Abismo-33 80.jpg,A Beira do Abismo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc5MTE4MzY2N15BMl5BanBnXkFtZTcwNjMwNDc3Ng@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/v6/r1zlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'FAST FIVE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUxNTk5MTE0OF5BMl5BanBnXkFtZTcwMjA2NzY3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/fast5.mp4',
                       'genre': ''},

                       {'name': 'Friends with Benefits',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ2MzQ0NTk4N15BMl5BanBnXkFtZTcwMDc2NDYzNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/2CqusxcGS9l8HRMsNMrLliN2MAT0_saksZG0utwjDHqASXALlDyk8ODYqp3QxZa_chM=m18',
                       'genre': 'Filmes'},

                       {'name': 'GATO DE BOTAS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTMxMTU5MTY4MV5BMl5BanBnXkFtZTcwNzgyNjg2NQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/N9Mh-1JMAMHTAO-n_kBu_S3KMpSms_cVwhvZar-znXn7KEeD79-Yhl3EFbsDtmls0JZnmSLLzRePM0PbLAB_jPJOAUYD45TgMOUFKKUy49ZZ_v-H0cv5sUeZ4-dFzcR1uU2xZiw9hg=m22',
                       'genre': 'Filmes'},

                       {'name': 'GATO DE BOTAS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTMxMTU5MTY4MV5BMl5BanBnXkFtZTcwNzgyNjg2NQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/N9Mh-1JMAMHTAO-n_kBu_S3KMpSms_cVwhvZar-znXn7KEeD79-Yhl3EFbsDtmls0JZnmSLLzRePM0PbLAB_jPJOAUYD45TgMOUFKKUy49ZZ_v-H0cv5sUeZ4-dFzcR1uU2xZiw9hg=m37',
                       'genre': 'Filmes'},

                       {'name': 'OperaCAo InvasAo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGIxODNjM2YtZjA5Mi00MjA5LTk2YjItODE0OWI5NThjNTBmXkEyXkFqcGdeQXVyNzQ1ODk3MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/14jcGUnB_ZCG4Up5UKQfnnAPpoNEowLtq-gWLya2cy2SRRO1x6Yt__5cILUSFokqEeT6NZbu=m37',
                       'genre': 'Filmes'},

                       {'name': 'Operação Invasão',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGIxODNjM2YtZjA5Mi00MjA5LTk2YjItODE0OWI5NThjNTBmXkEyXkFqcGdeQXVyNzQ1ODk3MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/14jcGUnB_ZCG4Up5UKQfnnAPpoNEowLtq-gWLya2cy2SRRO1x6Yt__5cILUSFokqEeT6NZbu=m22',
                       'genre': 'Filmes'},

                       {'name': 'OS AGENTES DO DESTINO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzc0ZDcwZTYtOWUzZi00NDE4LWI4NjgtMWVjZTUyYTA2ZTNhXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UY268_CR12,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/UcKcjEyIimmTGkdifuM4RKrzRu9dFTbTiJi-6z7ruxlnblkBILFqbmZss1B2klo0yZ6W5vCm=m22',
                       'genre': 'Filmes'},

                       {'name': 'RISE OF THE PLANET OF THE APES',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYzE3ZmNlZTctMDdmNy00MjMzLWFmZmYtN2M5N2YyYTQ1ZDJjXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/apes7.mp4',
                       'genre': ''},

                       {'name': 'THE GIRL WITH THE DRAGON TATTOO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTczNDk4NTQ0OV5BMl5BanBnXkFtZTcwNDAxMDgxNw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/dragontattoo.mp4',
                       'genre': ''},

                       {'name': 'TRANSFORMERS:DARK OF THE MOON',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTkwOTY0MTc1NV5BMl5BanBnXkFtZTcwMDQwNjA2NQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/transformers3.mp4',
                       'genre': ''},

                       {'name': 'Tudo Pelo Poder',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTU4MjkzNTY0OF5BMl5BanBnXkFtZTcwNDI5ODIxNg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/7HsQfKXWKcgTCRf15tgLj_w6t1cKvd52MFz2swxHk4idDrFffTfjgAZsXtDXLbfLpmDtkF1IPg=m22',
                       'genre': 'Filmes'},

                       {'name': 'Diário de um Banana',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGJmYTM4MjUtNTk3Ni00ZDIxLTgzOWUtZDZhZmEwMGYwMTcxXkEyXkFqcGdeQXVyNzkzNTg4NjY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/cwtm9rkUkeLwA6UBhonFAsk5LrT9ZG1PIsN723g-KwvfiOzutYm6anEkY_h5eEjreNAFlVaXWpgAUIKOtg=m22',
                       'genre': 'Filmes'},

                       {'name': 'Diário de um Banana 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGJmYTM4MjUtNTk3Ni00ZDIxLTgzOWUtZDZhZmEwMGYwMTcxXkEyXkFqcGdeQXVyNzkzNTg4NjY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/bLAxCmh24IJ5huHHjtIC_7sN59tTf0xvCmZJxfLq726PvSf0GstZ4hIni0RurYwj7ehm90XoS0zpmvhkdw=m22',
                       'genre': 'Filmes'},

                       {'name': 'Diário de um Banana 3',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGJmYTM4MjUtNTk3Ni00ZDIxLTgzOWUtZDZhZmEwMGYwMTcxXkEyXkFqcGdeQXVyNzkzNTg4NjY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/j7S36GSkxLTEhGsu6FU3hlJuLu8dVVdTx6ZQ2K13JzdtBQx3B8XfM4hRLB4ZTNkh-yDCOtT_5Bm3MuP4kg=m22',
                       'genre': 'Filmes'},

                       {'name': 'EsquadrAo Classe A',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc4ODc4NTQ1N15BMl5BanBnXkFtZTcwNDUxODUyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/5n_4JZ2GV_DB7aqsdyYcu926IhhIYWjz3DjuGjPYavQ2LacBvToBQNZbU7sXSxDxqHwXaZnyMw=m18',
                       'genre': 'Filmes'},

                       {'name': 'HOT TUB TIME MACHINE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQwMjExODA4Ml5BMl5BanBnXkFtZTcwNTYwMDYxMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/hottub2010.mp4',
                       'genre': ''},

                       {'name': 'O Aprendiz de Feiticeiro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDY3NzQ0NjYxM15BMl5BanBnXkFtZTcwMDkzODM2Mw@@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/oaprendizdefeiticeiro-dub-720p.mp4',
                       'genre': ''},

                       {'name': 'O Cisne Negro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzY2NzI4OTE5MF5BMl5BanBnXkFtZTcwMjMyNDY4Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://archive.org/download/OCisneNegro1942Dubl/O%20Cisne%20Negro%201942%20Dubl.mp4',
                       'genre': 'Filmes'},

                       {'name': 'O Cisne Negro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzY2NzI4OTE5MF5BMl5BanBnXkFtZTcwMjMyNDY4Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://archive.org/download/OCisneNegro1942Dubl/O%20Cisne%20Negro%201942%20Dubl.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Cisne Negro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzY2NzI4OTE5MF5BMl5BanBnXkFtZTcwMjMyNDY4Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://archive.org/download/OCisneNegro1942Dubl/O%20Cisne%20Negro%201942%20Dubl.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'PREDADORES',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjFmNDNlMGItMDQxMS00ZWMxLTg4MmQtMTBiNWU3ZDU1Nzk1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/FvKM3z2zn6IRwM0SdEugp6FRsod4sacM6HKHig0VzcEpHPtsNFidPPA0CrQRHt31ftbaayUZ=m22',
                       'genre': 'Filmes'},

                       {'name': 'Querido John',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk1NDEzMTU5NV5BMl5BanBnXkFtZTcwNTI3MTk5Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/1CoHfiOccZr2dkx57QsgIqhQS9F_oywsyX9dM0w6u7oQerr9sE2KJFRpwtzp7bElJHXIh9ANJw=m22',
                       'genre': 'Filmes'},

                       {'name': 'Shrek Para Sempre',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY0OTU1NzkxMl5BMl5BanBnXkFtZTcwMzI2NDUzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/h2i6QcsiPTyTULyXhf5YoRdBtmllfSnDl3vcgPvXrpw5yQm0oUR2Gd6-0qHsm0qzAgNj0EUjhBvbxoF0UA=m22',
                       'genre': 'ANIMACAO'},

                       {'name': 'THE OTHER GUYS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc0NDQzNTA2Ml5BMl5BanBnXkFtZTcwNzI2OTQzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/otherguys.mp4',
                       'genre': ''},

                       {'name': 'Trust Me',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzM2Mjc0Nzc4NF5BMl5BanBnXkFtZTcwNDk0MjY0NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=9394054eb3ba3382',
                       'genre': 'Trust Me (2017) LEG'},

                       {'name': 'Trust Me',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzM2Mjc0Nzc4NF5BMl5BanBnXkFtZTcwNDk0MjY0NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=8331f9a7877c2b27',
                       'genre': 'Trust Me (2017) LEG'},

                       {'name': 'Trust Me',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzM2Mjc0Nzc4NF5BMl5BanBnXkFtZTcwNDk0MjY0NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=3f13ec99365be81',
                       'genre': 'Trust Me (2017) LEG'},

                       {'name': 'Trust Me',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzM2Mjc0Nzc4NF5BMl5BanBnXkFtZTcwNDk0MjY0NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=12a7f23d31f6a822',
                       'genre': 'Trust Me (2017) LEG'},

                       {'name': 'UNSTOPPABLE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjI4NDQwMDM0N15BMl5BanBnXkFtZTcwMzY1ODMwNA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/unstoppable.mp4',
                       'genre': ''},

                       {'name': 'A Jovem Rainha Victoria',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTM4MjExMDk3NV5BMl5BanBnXkFtZTcwMTU3OTMwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/f6/66ylf_480p.mp4?',
                       'genre': 'AVENTURA'},

                       {'name': 'A Jovem Rainha Victoria',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTM4MjExMDk3NV5BMl5BanBnXkFtZTcwMTU3OTMwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/f6/66ylf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'A Jovem Rainha Victoria',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTM4MjExMDk3NV5BMl5BanBnXkFtZTcwMTU3OTMwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/f6/66ylf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Anjos da Noite 3 - A Rebeliao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg1OTU5ODc0MV5BMl5BanBnXkFtZTcwNDYyMDUwMg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/k/om/wffyb_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'Anjos da Noite 3 - A Rebeliao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg1OTU5ODc0MV5BMl5BanBnXkFtZTcwNDYyMDUwMg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/k/om/wffyb_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Anjos da Noite 3 - A Rebeliao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg1OTU5ODc0MV5BMl5BanBnXkFtZTcwNDYyMDUwMg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/2/16/dp1lf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Anjos Da Noite 3: A Rebelião',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg1OTU5ODc0MV5BMl5BanBnXkFtZTcwNDYyMDUwMg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/2/16/dp1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Anjos e Demônios',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjEzNzM2MjgxMF5BMl5BanBnXkFtZTcwNTQ1MTM0Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/ncSeQ7B6N0-Ul4C3lc-M6baJ1Cs7mqq_ajm3g6cp8fzARDZgajQ9f8zTmVTQBw0ZdaN8cQ2aXzPdZXcJ=m22',
                       'genre': 'Filmes'},

                       {'name': 'Anticristo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE3MjQ2ODc1N15BMl5BanBnXkFtZTcwNjYyMzI5Mg@@._V1_UY268_CR6,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/9D5Ra06Og3BJgvf8ElEWxtRpxXRL5D_A-3ujRRkImwHYTD0w0Em9x08v3HvrYsnIvKZG69omrw=m22',
                       'genre': 'Filmes'},

                       {'name': 'Anticristo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE3MjQ2ODc1N15BMl5BanBnXkFtZTcwNjYyMzI5Mg@@._V1_UY268_CR6,0,182,268_AL_.jpg',
                       'video': 'https://minhalista.live/channel/65317/wando/redirect',
                       'genre': 'Filmes'},

                       {'name': 'Bastardos InglOrios',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTJiNDEzOWYtMTVjOC00ZjlmLWE0NGMtZmE1OWVmZDQ2OWJhXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/5lSYCKPkZGKtnFoRvGM14WIBsyKLNEsi31pDlDTZ2BA4yywGiRN4QVzCGkIcyeBHF9Xh75F8=m18',
                       'genre': 'Filmes'},

                       {'name': 'Coraline e o Mundo Secreto  -',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzQxNjM5NzkxNV5BMl5BanBnXkFtZTcwMzg5NDMwMg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/1qF3zVzfXrYU9j2lHZG8yInV7yYME3JxbBAdYJkMHKERGMDzApuRP8iCjuJzIa2HN1f4cA7sfeg=m37',
                       'genre': 'Filmes'},

                       {'name': 'DISTRITO 9',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYmQ5MzFjYWMtMTMwNC00ZGU5LWI3YTQtYzhkMGExNGFlY2Q0XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/RW5eG4nfrzv720ZJ_tgRXtLFVaYEuM-Rjd07juCSRFqrXlPJ1CQcn26DfNPxaaABBNElUkPRKHTPHG_7xA=m22',
                       'genre': 'Filmes'},

                       {'name': 'Julie & Julia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzA4NjA2NjI2NV5BMl5BanBnXkFtZTcwOTEzNzI2Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/n6/2w2lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Julie & Julia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzA4NjA2NjI2NV5BMl5BanBnXkFtZTcwOTEzNzI2Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/n6/2w2lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'LAW ABIDING CITIZEN',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTMyODY1NTg1N15BMl5BanBnXkFtZTcwMTUyODI4Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/lawcitizen.mp4',
                       'genre': ''},

                       {'name': 'New Orleans TV',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTcyMzY0NTMzMF5BMl5BanBnXkFtZTcwMTc1MjY4Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media4.tripsmarter.com:1935/LiveTV/NOTVHD/playlist.m3u8',
                       'genre': 'USA'},

                       {'name': 'O Sequestro do Metro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU3NzA4MDcwNV5BMl5BanBnXkFtZTcwMDAyNzc1Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/4/v6/3ovlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'O Sequestro do Metro 123',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU3NzA4MDcwNV5BMl5BanBnXkFtZTcwMDAyNzc1Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/4/v6/3ovlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Sequestro do Metro 123',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU3NzA4MDcwNV5BMl5BanBnXkFtZTcwMDAyNzc1Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/4/v6/3ovlf_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'Pandorum',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDQxNjc5NTMxNl5BMl5BanBnXkFtZTcwNjg2NDE4Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/sthSU7UNrdu14zDta-eRORreGtiyy86TndItExLG0QtFVW47ukqUGwjIpIdCC4OEPik=m18',
                       'genre': 'Filmes'},

                       {'name': 'Pandorum',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDQxNjc5NTMxNl5BMl5BanBnXkFtZTcwNjg2NDE4Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/sthSU7UNrdu14zDta-eRORreGtiyy86TndItExLG0QtFVW47ukqUGwjIpIdCC4OEPik=m18',
                       'genre': 'Filmes'},

                       {'name': 'Sempre ao Seu Lado',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTNhZDFkN2ItMmZjNy00ODUwLTk1Y2MtMDZhYTA2N2MyNDU5XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/-oOSiOgN2A8zR2Wk9hDG4bNX6xBZeSAOhZ5DcZIpebwyLY74MlGVh0ycVSwdchhZqIA3bJzk=m22',
                       'genre': 'Filmes'},

                       {'name': 'The One I Love',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjAwNDA1MTM2MF5BMl5BanBnXkFtZTcwMzg3NDcwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/MwohBjxBqgkOVLL0zBEvO3ZYQubQkYFqDcwCmd3dj6vzZ31vMykLOnKq9B4GEsnQFjM=m18',
                       'genre': 'Filmes'},

                       {'name': 'THE TAKING OF PELHAM 123',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU3NzA4MDcwNV5BMl5BanBnXkFtZTcwMDAyNzc1Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/pelham123.mp4',
                       'genre': ''},

                       {'name': 'Travelers',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWNlN2RmZDktNzllNC00NDVlLTllMzgtZGQ1YmRmZThmZjZmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=45eb518e928ebffd',
                       'genre': 'Travelers LEG'},

                       {'name': 'Travelers',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWNlN2RmZDktNzllNC00NDVlLTllMzgtZGQ1YmRmZThmZjZmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=7d8b70d1b3544ce7',
                       'genre': 'Travelers LEG'},

                       {'name': 'Travelers',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWNlN2RmZDktNzllNC00NDVlLTllMzgtZGQ1YmRmZThmZjZmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=90d52e6b460648ed',
                       'genre': 'Travelers LEG'},

                       {'name': 'Travelers',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWNlN2RmZDktNzllNC00NDVlLTllMzgtZGQ1YmRmZThmZjZmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=defdeb4ebbff8f33',
                       'genre': 'Travelers LEG'},

                       {'name': 'Travelers',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWNlN2RmZDktNzllNC00NDVlLTllMzgtZGQ1YmRmZThmZjZmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=4735f7bac7847e31',
                       'genre': 'Travelers LEG'},

                       {'name': 'Travelers',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWNlN2RmZDktNzllNC00NDVlLTllMzgtZGQ1YmRmZThmZjZmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=64e8f0e40761e575',
                       'genre': 'Travelers LEG'},

                       {'name': 'Travelers',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWNlN2RmZDktNzllNC00NDVlLTllMzgtZGQ1YmRmZThmZjZmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=c4a6831e2abbb156',
                       'genre': 'Travelers LEG'},

                       {'name': 'Travelers',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWNlN2RmZDktNzllNC00NDVlLTllMzgtZGQ1YmRmZThmZjZmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=26a704f2a6129592',
                       'genre': 'Travelers LEG'},

                       {'name': 'Travelers',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWNlN2RmZDktNzllNC00NDVlLTllMzgtZGQ1YmRmZThmZjZmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=474acc68a5e0bff',
                       'genre': 'Travelers LEG'},

                       {'name': 'Travelers',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWNlN2RmZDktNzllNC00NDVlLTllMzgtZGQ1YmRmZThmZjZmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=2e18d404b4bc0da',
                       'genre': 'Travelers LEG'},

                       {'name': 'Travelers',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWNlN2RmZDktNzllNC00NDVlLTllMzgtZGQ1YmRmZThmZjZmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=3fcfc55eca30a1e5',
                       'genre': 'Travelers LEG'},

                       {'name': 'Travelers',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWNlN2RmZDktNzllNC00NDVlLTllMzgtZGQ1YmRmZThmZjZmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=572dad596807fb76',
                       'genre': 'Travelers LEG'},

                       {'name': 'tvg-logo=http://br.web.img2.acsta.net/medias/nmedia/18/87/32/62/19874342.jpg,A Jovem Rainha Victoria',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTM4MjExMDk3NV5BMl5BanBnXkFtZTcwMTU3OTMwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/f6/66ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://br.web.img2.acsta.net/r_160_240/b_1_d6d6d6/medias/nmedia/18/87/29/50/19874017.jpg,O Sequestro do Metro 123',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU3NzA4MDcwNV5BMl5BanBnXkFtZTcwMDAyNzc1Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/4/v6/3ovlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/r/n6/2w2lf_tnl_2 8.jpg?ts=20150225004008,Julie & Julia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzA4NjA2NjI2NV5BMl5BanBnXkFtZTcwOTEzNzI2Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/n6/2w2lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://www.assistirfilmesdublados.com.br/wp-content/uploads/2015/01/Anjos-Da-Noite-3-a-Rebeli%C3%A3o.jpg,Anjos da Noite 3 - A Rebeliao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg1OTU5ODc0MV5BMl5BanBnXkFtZTcwNDYyMDUwMg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/k/om/wffyb_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Uma Prova de Amor',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ2NDg4MDU3NF5BMl5BanBnXkFtZTcwMjg5Njc1Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/RqvJtY3e5fg-V5V6lZu0qGo_0LJTR_ugEuetD2h0STOgOv6d33j02YmbiCgdRspl0b6yg4hevQ=m18',
                       'genre': 'Filmes'},

                       {'name': 'Zumbilandia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU5MDg0NTQ1N15BMl5BanBnXkFtZTcwMjA4Mjg3Mg@@._V1_UY268_CR5,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/Xsl2_M_pM0YslMK_Yl1dsFOiCxlo_5XKrM4vBfEKA7DWwnV_vka8eOqa7JQG2iUng9757jC_ng=m18',
                       'genre': 'Filmes'},

                       {'name': ',Guerra ao Terror',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzEwNzQ1NjczM15BMl5BanBnXkFtZTcwNTk3MTE1Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/f6/95ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Hancock',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTgyMzc4ODU3NV5BMl5BanBnXkFtZTcwNjk5Mzc1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/96/631lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Bons Costumes',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI0NDA2NDM4OV5BMl5BanBnXkFtZTcwMjUxODk0Mg@@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/96/d41lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Bons Costumes',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI0NDA2NDM4OV5BMl5BanBnXkFtZTcwMjUxODk0Mg@@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/96/d41lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Corrida Mortal',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTkwMDU1ODg5Ml5BMl5BanBnXkFtZTcwNjMzNjY3MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/vfJzkSQRpplPhA-J5mvVaaaI9Yeavmx-0NjSywuisMbqTCOqXPjUvdFWVoparFHqed0QD7eNpun0JB-g2wnsNBW4r6GoH-6BftFp=m18',
                       'genre': 'Filmes'},

                       {'name': 'Espelhos Do Medo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI2NTA1ODEyOF5BMl5BanBnXkFtZTcwNjc3MjY3MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/rXQL1MDBXGyZymCbQ2DUPPdCiSiDT06WpQb_kRDQYf5QCPsKQ16J_kpcKq-e5nieDuX5kWkr=m37',
                       'genre': 'Filmes'},

                       {'name': 'Espelhos do Medo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI2NTA1ODEyOF5BMl5BanBnXkFtZTcwNjc3MjY3MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/mirrors-dub-720p.mp4',
                       'genre': ''},

                       {'name': 'Espelhos Do Medo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI2NTA1ODEyOF5BMl5BanBnXkFtZTcwNjc3MjY3MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/SKmr9b160VFcDbzYMXaATGtlwNSyyIgSsAyxIAyXxANu2hCs7rC2cujKYcroY250C42q1EmWz50=m22',
                       'genre': 'Filmes'},

                       {'name': 'Foi Apenas um Sonho',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTczNDgzMjczOV5BMl5BanBnXkFtZTcwOTU3MzMwMg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/oSkdxPHrgW80lhSvlXzEYCnX3gJwOIMxKecfgCZWp5hCWgCVScMTEboLf7rmqF13vKL6btfrwZc=m18',
                       'genre': 'Filmes'},

                       {'name': 'Guerra ao Terror',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzEwNzQ1NjczM15BMl5BanBnXkFtZTcwNTk3MTE1Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/f6/95ylf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Hancock',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTgyMzc4ODU3NV5BMl5BanBnXkFtZTcwNjk5Mzc1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/m5u6zyWfYJ56JLHK-VjftGt4Wy7T3xxNdq09OoCLHkWfSRyT_zzVf-skMjq7epYfNUJF_-iq=m22',
                       'genre': 'Filmes'},

                       {'name': 'Hancock-',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTgyMzc4ODU3NV5BMl5BanBnXkFtZTcwNjk5Mzc1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/96/631lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Marley e Eu',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTlkYmM2NjAtMDkyZi00M2JiLThjZmItMjUzZDhiMDg2NGJmXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'https://dropapk.com/vidembed-5yxiz9kv3h2t.mp4',
                       'genre': 'Diversos'},

                       {'name': 'Martyrs',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTY0NTZlZjYtNWRmZi00MGRjLTk4ZDctMjE4NjBiZTUyNGNhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/L6ItZhgXAbJZRVYgmvoi4k9UTIrMdrZ1khBIPJY6DwK9CY8U6-4_HFjJ1Jy4gx0yUaPGtCYfn4s=m18',
                       'genre': 'Filmes'},

                       {'name': 'O Casamento de Rachel',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA0NTY2NzQ1MF5BMl5BanBnXkFtZTcwNjU1NjAyMg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/16/ap1lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Casamento de Rachel',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA0NTY2NzQ1MF5BMl5BanBnXkFtZTcwNjU1NjAyMg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/16/ap1lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'O Casamento de Rachel',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA0NTY2NzQ1MF5BMl5BanBnXkFtZTcwNjU1NjAyMg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/16/ap1lf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'O Incrível Hulk',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUyNzk3MjA1OF5BMl5BanBnXkFtZTcwMTE1Njg2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/ou1OWl_kz13A8D7f5W5PyhF4Bj-4Q1t47sKsaOU-EMNAhTU1kxnmZH0bLSmXLU-W-UmLlw5fMboidQrbIQ=m22',
                       'genre': 'Filmes'},

                       {'name': 'O INCRIVEL HULK',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUyNzk3MjA1OF5BMl5BanBnXkFtZTcwMTE1Njg2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://conteudo.maxcinefree.ga/filmes/71-o-incrivel-hulk-2008-1080-db.mp4',
                       'genre': 'FASE 1'},

                       {'name': 'O Paraiso e Logo Aqui',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI5ODIwNzg0NV5BMl5BanBnXkFtZTcwOTE0NDY3MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/d6/20vlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Outlander: Guerreiro vs Predador',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTBhYmNhZTYtMTEzMi00M2E2LTgyMTYtM2FmYjhjZGFlZWUzXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/oNgjuvvTMhGL7MjVLBb1tD9VjozQoDbf9DyVfU3Jrfi8mJ0vzrBeo50skKcYl9h9K7VFKNh0v--Yxbw_1m7YFofhFcqRPYhRilF0Wfc9dTAxK1k90niYv6qTmZtVhpBKfF_0r5YwbA=m22',
                       'genre': 'Filmes'},

                       {'name': 'Segurando As Pontas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY1MTE4NzAwM15BMl5BanBnXkFtZTcwNzg3Mjg2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/f6/a4ylf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Segurando As Pontas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY1MTE4NzAwM15BMl5BanBnXkFtZTcwNzg3Mjg2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/f6/a4ylf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'Sem Vestigios',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYyNTcwODYzMF5BMl5BanBnXkFtZTcwNjMwMzU1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/56/bw1lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Sem Vestigios',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYyNTcwODYzMF5BMl5BanBnXkFtZTcwNjMwMzU1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/56/bw1lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Sete Vidas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU0NzY0MTY5OF5BMl5BanBnXkFtZTcwODY3MDEwMg@@._V1_UY268_CR9,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/16/3o1lf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'SEVEN POUNDS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU0NzY0MTY5OF5BMl5BanBnXkFtZTcwODY3MDEwMg@@._V1_UY268_CR9,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/sevenp.mp4',
                       'genre': ''},

                       {'name': 'STEP BROTHERS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjZiNzU0YWQtYTA4OS00OTYwLTk4ZmYtNGNmZjU3YTFjMjM5XkEyXkFqcGdeQXVyMTMxMTY0OTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/stepbro.mp4',
                       'genre': ''},

                       {'name': 'TrovAo Tropical',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDE5NjQzMDkzOF5BMl5BanBnXkFtZTcwODI3ODI3MQ@@._V1_UY268_CR4,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/GX10PFLhQKn16w5aEUiKxvbzeO1XP-TzLlplzXdM05gxWDHI4z8E4effGkCm3mcXEe9zdBW2=m18',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://1.bp.blogspot.com/_5EE1wK9F0qs/TA8afo8VZDI/AAAAAAAAB8I/Fhro_JuHTPU/s1600/Segurando.as.Pontas.DVDIP.Xvid.Dublado.jpg,Segurando As Pontas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY1MTE4NzAwM15BMl5BanBnXkFtZTcwNzg3Mjg2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/f6/a4ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://2.bp.blogspot.com/-w8tq3EXTCCY/TaZEosyEriI/AAAAAAAAAQU/-YGCuojAmNA/s1600/Um+Ato+de+Liberdade.jpg,Um Ato de Liberdade',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjEyYjk4ZDQtZDhjMi00NGFkLWExM2UtZjgyMDMxODgwNjgyXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/f6/c7ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://amalgama.blog.br/imagens/101/casamento-de-rachel.jpg,O Casamento de Rachel',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA0NTY2NzQ1MF5BMl5BanBnXkFtZTcwNjU1NjAyMg@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/16/ap1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/q/sl/wbcyb_tnl_2 8.jpg?ts=20140407013733,Sem Vestigios',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYyNTcwODYzMF5BMl5BanBnXkFtZTcwNjMwMzU1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/56/bw1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/w/96/d41lf_tnl_2 8.jpg?ts=20150226222223,Bons Costumes',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI0NDA2NDM4OV5BMl5BanBnXkFtZTcwMjUxODk0Mg@@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/96/d41lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images1.folha.com.br/livraria/images/3/c/1153148-250x250.png,Sete Vidas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU0NzY0MTY5OF5BMl5BanBnXkFtZTcwODY3MDEwMg@@._V1_UY268_CR9,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/16/3o1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Um Ato de Liberdade',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjEyYjk4ZDQtZDhjMi00NGFkLWExM2UtZjgyMDMxODgwNjgyXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/f6/c7ylf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Um Ato de Liberdade',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjEyYjk4ZDQtZDhjMi00NGFkLWExM2UtZjgyMDMxODgwNjgyXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/f6/c7ylf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Um Ato de Liberdade',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjEyYjk4ZDQtZDhjMi00NGFkLWExM2UtZjgyMDMxODgwNjgyXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/f6/c7ylf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Valkyrie',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg3Njc2ODEyN15BMl5BanBnXkFtZTcwNTAwMzc3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/kuDBpi_LY-NxcMJmF0S-l-_WB-mrUANoOdw67bvwE4PMQjUDMrIU0aleCYkGhUUaYrw=m18',
                       'genre': 'Filmes'},

                       {'name': ',Superbad - E Hoje',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc0NjIyMjA2OF5BMl5BanBnXkFtZTcwMzIxNDE1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/d6/32vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': '24/7 The Simpsons',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTgxMDczMTA5N15BMl5BanBnXkFtZTcwMzk1MzMzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://righttv.ddns.net:25461/live/trial30/trial30/11260.ts',
                       'genre': ''},

                       {'name': 'A LENDA DO TESOURO PERDIDO:LIVRO DOS SEGREDOS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU2NTM3NjU1N15BMl5BanBnXkFtZTcwODg1MDU1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/x6/qs4lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=5a8baa2deeb71949',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d63ac94be4e1c08f',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=decb82530eb1c456',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=f750e2aef01d8930',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d65347ddc3cd056a',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=cda8ad2bbfa62f1d',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=77f12972119ca819',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=8e9cb357ad128998',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=9e9da7a5cf22fbf',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=7b0d95a6d8c28cd2',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=34e5efc95163370',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=ee9df44da55e412d',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=e9a9e71cd95cd7e8',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=254d505452715e2e',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=f7450e9362e9ec75',
                       'genre': 'American Crime LEG'},

                       {'name': 'American Crime',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDc5YjRlMzctODMxYS00MDA4LWFhNjktMjhlODBkZTE0ZDQwXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=c97f05d408fc32ca',
                       'genre': 'American Crime LEG'},

                       {'name': 'AMERICAN GANGSTER',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTkyNzY5MDA5MV5BMl5BanBnXkFtZTcwMjg4MzI3MQ@@._V1_UY268_CR4,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/agangster.mp4',
                       'genre': ''},

                       {'name': 'Apenas Uma Vez',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWUxZjJkMDktZmMxMS00Mzg3LTk4MDItN2IwODlmN2E0MTM0XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/f6/86ylf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'Apenas Uma Vez',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWUxZjJkMDktZmMxMS00Mzg3LTk4MDItN2IwODlmN2E0MTM0XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/f6/86ylf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Apenas Uma Vez',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWUxZjJkMDktZmMxMS00Mzg3LTk4MDItN2IwODlmN2E0MTM0XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/f6/86ylf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Apenas Uma Vez',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWUxZjJkMDktZmMxMS00Mzg3LTk4MDItN2IwODlmN2E0MTM0XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/f6/86ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'As Férias de Mr Bean',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTM2NzQ1Mzc4M15BMl5BanBnXkFtZTcwNTk3NjA1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://dl.dropboxusercontent.com/apitl/1/AAA2sN6iRUWdkhCGAU25_buxMMZheWCBJ4I4pAys4brlnIxdlXTs6YgB03hxP--5oL3jjsD1DMsUQ3fvID8kLcZcaAUKIkm6bYMGo8Np-O_gSXAUWAwfxzi25m1ePq5jvUs86l2FjQyqsgE4fUAIf8bqiffUi81qyIB9tkSjl0T_53z0UwUczTCD4QuK0vQW0hjgbkjBG_BlHNWznBIlIO5vzkBRKhDbMFGEns1bNay37DPODJNkdsdYxKHvFN5zk5hlcMs2qCW5KahDCzkB1jnY',
                       'genre': 'Filmes'},

                       {'name': 'BLADES OF GLORY',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY3MDMyMTYxMl5BMl5BanBnXkFtZTcwMjk0NzI0MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/glory.mp4',
                       'genre': ''},

                       {'name': 'El orfanato',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc3MjE0NzQzMV5BMl5BanBnXkFtZTYwMzI0ODc4._V1_UY268_CR4,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/Axq8sCyuhWKmMOULtLW_8hUycMOKzqwMzdFnCs0hGKNB0AFP82FDYzKIYyFYxP4PdpA=m18',
                       'genre': 'Filmes'},

                       {'name': 'HOT FUZZ',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzg4MDJhMDMtYmJiMS00ZDZmLThmZWUtYTMwZDM1YTc5MWE2XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/hotfuzz.mp4',
                       'genre': ''},

                       {'name': 'Juno',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIwMDgwODc5Nl5BMl5BanBnXkFtZTYwMjQzMDM4._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/a/56/lq1lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Juno',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIwMDgwODc5Nl5BMl5BanBnXkFtZTYwMjQzMDM4._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/a/56/lq1lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'O clube de Leitura de Jane Austen',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY5MTYwMzM3MF5BMl5BanBnXkFtZTcwOTAxODM1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/2/d6/g4vlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'O Nevoeiro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU2NjQyNDY1Ml5BMl5BanBnXkFtZTcwMTk1MDU1MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=aad4e8a34dcf7cb3',
                       'genre': 'The Mist DUB'},

                       {'name': 'O Nevoeiro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU2NjQyNDY1Ml5BMl5BanBnXkFtZTcwMTk1MDU1MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=27c56115958f7e63',
                       'genre': 'The Mist DUB'},

                       {'name': 'O Nevoeiro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU2NjQyNDY1Ml5BMl5BanBnXkFtZTcwMTk1MDU1MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=b9339c0fb651df5f',
                       'genre': 'The Mist DUB'},

                       {'name': 'O Nevoeiro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU2NjQyNDY1Ml5BMl5BanBnXkFtZTcwMTk1MDU1MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=115e4e3c7ccc1f6',
                       'genre': 'The Mist DUB'},

                       {'name': 'O Nevoeiro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU2NjQyNDY1Ml5BMl5BanBnXkFtZTcwMTk1MDU1MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d12834d52644cf3b',
                       'genre': 'The Mist DUB'},

                       {'name': 'O Nevoeiro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU2NjQyNDY1Ml5BMl5BanBnXkFtZTcwMTk1MDU1MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d2796e0c3480b718',
                       'genre': 'The Mist DUB'},

                       {'name': 'O Nevoeiro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU2NjQyNDY1Ml5BMl5BanBnXkFtZTcwMTk1MDU1MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=4bbeab50f0fb586f',
                       'genre': 'The Mist DUB'},

                       {'name': 'O Nevoeiro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU2NjQyNDY1Ml5BMl5BanBnXkFtZTcwMTk1MDU1MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=f115d383a6faacf2',
                       'genre': 'The Mist DUB'},

                       {'name': 'O Nevoeiro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU2NjQyNDY1Ml5BMl5BanBnXkFtZTcwMTk1MDU1MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=3ae4e1b97790810b',
                       'genre': 'The Mist DUB'},

                       {'name': 'O Nevoeiro',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU2NjQyNDY1Ml5BMl5BanBnXkFtZTcwMTk1MDU1MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=677d1e2cfc11ac49',
                       'genre': 'The Mist DUB'},

                       {'name': 'O Orfanato',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc3MjE0NzQzMV5BMl5BanBnXkFtZTYwMzI0ODc4._V1_UY268_CR4,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/Axq8sCyuhWKmMOULtLW_8hUycMOKzqwMzdFnCs0hGKNB0AFP82FDYzKIYyFYxP4PdpA=m18',
                       'genre': 'Filmes'},

                       {'name': 'Ratatouille',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/MsJQacleH376A_V2DNkQ5BAUdD6yuEdbQ7TNWeUaLxrCAVWGTjPoPI4vR55KGfJbGaMIomrG=m22',
                       'genre': 'Filmes'},

                       {'name': 'RATATOUILLE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/ratatouille.mp4',
                       'genre': ''},

                       {'name': 'Resident Evil 3: A Extincao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDQ0MWI3MmEtMzM0OC00Y2ViLWE4MDItMzNhNmY1ZTdjMWE2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/0/v6/n1zlf_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'Resident Evil 3: A Extincao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDQ0MWI3MmEtMzM0OC00Y2ViLWE4MDItMzNhNmY1ZTdjMWE2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/0/v6/n1zlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Resident Evil: Extinction',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDQ0MWI3MmEtMzM0OC00Y2ViLWE4MDItMzNhNmY1ZTdjMWE2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/nWPp6LWI4hLRU1YkHU2uN7n62c8kpAVBeA-1rT9YOJLMTroQKvSbDwX8R1NAuDQSmVQML7qg=m22',
                       'genre': 'Filmes'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=ea3bd2853a81dc14',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=b536d3d236fe55b4',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=8f0c1d98c0cdc46f',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=fd12f0be1919ff9e',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=bbb73cf0d1c6787d',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=efe0a36eecd94501',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=998394f241acb235',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=4f2c8d8a34ffbc35',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=cdd4ce598f3244b',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=3484f52eef6b96ec',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=9911bd150970ffee',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=266c4ab869d5bed5',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=982da945de38d8d3',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=fb83fe113fce449c',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=f839de1f0f0ac726',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=196503ae1a503f57',
                       'genre': 'Shooter DUB'},

                       {'name': 'Shooter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGRjMzY0OGItNDc4YS00OGNlLWI3MGYtZjRkNjdiNWUyNDY4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=768f2303ddc0ca5b',
                       'genre': 'Shooter DUB'},

                       {'name': 'Superbad - E Hoje',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc0NjIyMjA2OF5BMl5BanBnXkFtZTcwMzIxNDE1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/d6/32vlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Superbad - E Hoje',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc0NjIyMjA2OF5BMl5BanBnXkFtZTcwMzIxNDE1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/d6/32vlf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'Superbad - Eh Hoje',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc0NjIyMjA2OF5BMl5BanBnXkFtZTcwMzIxNDE1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/d6/32vlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Tá Dando Onda 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE4NDE3NzcwM15BMl5BanBnXkFtZTcwMTI0ODYzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/aM5_Qinl18j5fb71FelSOEmvm5PdiTGgyO8xFCTJSQwoBr2BjjNkwxQGPlqLrG3xSwpLAXIHQVEuVfFxSw=m37',
                       'genre': 'ANIMACAO'},

                       {'name': 'Tá Dando Onda 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE4NDE3NzcwM15BMl5BanBnXkFtZTcwMTI0ODYzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/5K-RS9EcP7D046mXXyHwy5OfEZXeVg5Fo5mtp16CKiDOxupnSuQhKRYPUsI6Rzv2q2FjKppkWPWxhQ=m18',
                       'genre': 'Filmes'},

                       {'name': 'THE BOURNE ULTIMATUM',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNGNiNmU2YTMtZmU4OS00MjM0LTlmYWUtMjVlYjAzYjE2N2RjXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/bourne3.mp4',
                       'genre': ''},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/a/56/lq1lf_tnl_2 8.jpg?ts=20150319144703,Juno',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIwMDgwODc5Nl5BMl5BanBnXkFtZTYwMjQzMDM4._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/a/56/lq1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://upload.wikimedia.org/wikipedia/pt/3/34/Resident_Evil_Extinction.jpg,Resident Evil 3: A Extincao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDQ0MWI3MmEtMzM0OC00Y2ViLWE4MDItMzNhNmY1ZTdjMWE2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/0/v6/n1zlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Anjos da Noite: A Evolucao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjEzNDY1OTQwOV5BMl5BanBnXkFtZTcwNjcxMTIzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/n6/d6ulf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Desafio Radical',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI1MDAzMDgzMF5BMl5BanBnXkFtZTcwNzc1ODQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/z6/jsvlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',O Codigo Da Vinci',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjIxMjQyMTc3Nl5BMl5BanBnXkFtZTcwMTA1MDUzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/n/z6/grvlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',O Ilusionista',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BY2VkMzZlZDAtNTkzNS00MDIzLWFmOTctMWQwZjQ1OWJiYzQ1XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/z6/vsvlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Rocky Balboa',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNWIyNmQyNjctYmVmMS00MGI4LWIxMmUtNjA0ODYzOTA0Yjk0L2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR6,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/x/f6/23ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'A Procura Da Felicidade',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ5NjQ0NDI3NF5BMl5BanBnXkFtZTcwNDI0MjEzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/t/96/201lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'À Procura Da Felicidade',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ5NjQ0NDI3NF5BMl5BanBnXkFtZTcwNDI0MjEzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/U7H7be90fmBFJk1B_2cpSJ1pDlYIWNhtMvOF2vpyOjsVZFdRLsOK7Xs-e3b7hpU7Lq93NBjm=m22',
                       'genre': 'Filmes'},

                       {'name': 'Anjos da Noite: A Evolucao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjEzNDY1OTQwOV5BMl5BanBnXkFtZTcwNjcxMTIzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/n6/d6ulf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Anjos da Noite: A Evolucao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjEzNDY1OTQwOV5BMl5BanBnXkFtZTcwNjcxMTIzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/n6/d6ulf_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'Apocalypto',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzhmNGMzMDMtZDM0Yi00MmVmLWExYjAtZDhjZjcxZDM0MzJhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://cecegeek@goo.gl/agdAzp',
                       'genre': 'Filmes'},

                       {'name': 'Bicho Vai Pegar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQwOTg2MjU0OV5BMl5BanBnXkFtZTcwMzIzNTQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/jASrogR0kTBuEV2Roly-Fkltvu6_yhkA4geFFj5R6Efene6Ds4cPN4zw9JzP3LwMr89kDXbxpXQ=m18',
                       'genre': 'Animação'},

                       {'name': 'Bicho Vai Pegar 3',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQwOTg2MjU0OV5BMl5BanBnXkFtZTcwMzIzNTQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/0Kkg7GUFbGmAAbnaLlK12xEBDFmbdjZkUFiRWL2NI-Je-N_5mxB-GrxyLolRTTjqES7grKn828Q=m18',
                       'genre': 'Animação'},

                       {'name': 'Bicho Vai Pegar 4',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQwOTg2MjU0OV5BMl5BanBnXkFtZTcwMzIzNTQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/7EKsm3QwnoEeMjcU8Ncp4r9mtIHrxQbgD0xAW6AWxje18-8bnQYwze3FjdEYTlNndvxlp4pwYg=m18',
                       'genre': 'Animação'},

                       {'name': 'Click',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTA1MTUxNDY4NzReQTJeQWpwZ15BbWU2MDE3ODAxNw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/d/f6/q4ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'DEJA VU',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzEwNTAwNjEwMV5BMl5BanBnXkFtZTYwMzgzMjA3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/dejavu.mp4',
                       'genre': ''},

                       {'name': 'Desafio Radical',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI1MDAzMDgzMF5BMl5BanBnXkFtZTcwNzc1ODQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/z6/jsvlf_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'Desafio Radical',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI1MDAzMDgzMF5BMl5BanBnXkFtZTcwNzc1ODQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/z6/jsvlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Desafio Radical',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI1MDAzMDgzMF5BMl5BanBnXkFtZTcwNzc1ODQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/z6/jsvlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'INSIDE MAN',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjc4MjA2ZDgtOGY3YS00NDYzLTlmNTEtYWMxMzcwZjgzYWNjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/insideman.mp4',
                       'genre': ''},

                       {'name': 'Le code Da Vinci',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjIxMjQyMTc3Nl5BMl5BanBnXkFtZTcwMTA1MDUzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/9ow0AfR2toDFElmKK5KP2fEsaDZpWrCOwUB346Op87hT66uq9rmEYFpPwVCjnwjQ7io=m18',
                       'genre': 'Filmes'},

                       {'name': 'O Bicho Vai Pegar 4',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQwOTg2MjU0OV5BMl5BanBnXkFtZTcwMzIzNTQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/elwH18dsc14Ekcwad90SrPKLWRNZw-uPHZpE3TJ99YHVA8doGSgZQ1KS9qmxSDKAP7vOirHWRQ=m37',
                       'genre': 'Filmes'},

                       {'name': 'O Bom Pastor',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU5MjExMzA1Nl5BMl5BanBnXkFtZTgwMzIxNzQxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://archive.org/download/O_Monstro_Do_Mar_Revolto_1955_Leg/O_Monstro_Do_Mar_Revolto_1955_Leg.mp4',
                       'genre': 'Filmes'},

                       {'name': 'O Bom Pastor',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU5MjExMzA1Nl5BMl5BanBnXkFtZTgwMzIxNzQxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://archive.org/download/O_Bom_Pastor_1944_Leg/O_Bom_Pastor_1944_Leg.mp4?',
                       'genre': 'RELIGIOSO'},

                       {'name': 'O Bom Pastor',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU5MjExMzA1Nl5BMl5BanBnXkFtZTgwMzIxNzQxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://archive.org/download/O_Bom_Pastor_1944_Leg/O_Bom_Pastor_1944_Leg.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Codigo Da Vinci',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjIxMjQyMTc3Nl5BMl5BanBnXkFtZTcwMTA1MDUzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/n/z6/grvlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Codigo Da Vinci',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjIxMjQyMTc3Nl5BMl5BanBnXkFtZTcwMTA1MDUzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/n/z6/grvlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'O Despertar de uma Paixao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTMzODg4MjU4OF5BMl5BanBnXkFtZTYwNDAzNTU3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/5/8l/u7cyb_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Despertar De Uma Paixão',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTMzODg4MjU4OF5BMl5BanBnXkFtZTYwNDAzNTU3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/h6/77vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'O Despertar de uma Paixao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTMzODg4MjU4OF5BMl5BanBnXkFtZTYwNDAzNTU3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/5/8l/u7cyb_480p.mp4?',
                       'genre': 'ROMANCE'},

                       {'name': 'O Despertar de Uma Paixao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTMzODg4MjU4OF5BMl5BanBnXkFtZTYwNDAzNTU3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/h6/77vlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'O Ilusionista',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BY2VkMzZlZDAtNTkzNS00MDIzLWFmOTctMWQwZjQ1OWJiYzQ1XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/z6/vsvlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'O Ilusionista',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BY2VkMzZlZDAtNTkzNS00MDIzLWFmOTctMWQwZjQ1OWJiYzQ1XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/z6/vsvlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Ilusionista',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BY2VkMzZlZDAtNTkzNS00MDIzLWFmOTctMWQwZjQ1OWJiYzQ1XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/z6/vsvlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Ricky Bobby - A Toda Velocidade',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzAzOTk1OTIyM15BMl5BanBnXkFtZTcwNDIzNTQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/x/r6/0gvlf_480p.mp4?',
                       'genre': 'AVENTURA'},

                       {'name': 'Ricky Bobby - A Toda Velocidade',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzAzOTk1OTIyM15BMl5BanBnXkFtZTcwNDIzNTQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/x/r6/0gvlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Rocky Balboa',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNWIyNmQyNjctYmVmMS00MGI4LWIxMmUtNjA0ODYzOTA0Yjk0L2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR6,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/x/f6/23ylf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'TALLADEGA NIGHTS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzAzOTk1OTIyM15BMl5BanBnXkFtZTcwNDIzNTQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/talla.mp4',
                       'genre': ''},

                       {'name': 'The Veil',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTMzODg4MjU4OF5BMl5BanBnXkFtZTYwNDAzNTU3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/FxDyOfaaKAmPjY6m3fUQLQ3K8jJsptmGqimy6AHYlylrWBqpxNAptC6zgX6-zbyCC5k=m22',
                       'genre': 'Filmes'},

                       {'name': 'TV CULTURA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk0MTQ3NDQ4Ml5BMl5BanBnXkFtZTcwOTQ3OTQzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://s1.elitehdbr.vip:8880/live/sconnec/duAVYZUail/309.ts',
                       'genre': 'SKY'},

                       {'name': 'TV CULTURA MG',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk0MTQ3NDQ4Ml5BMl5BanBnXkFtZTcwOTQ3OTQzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://173.236.10.10:1935/redeatividade/redeatividade/playlist.m3u8',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/5/8l/u7cyb_tnl_2 8.jpg?ts=20130817031148,O Despertar de uma Paixao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTMzODg4MjU4OF5BMl5BanBnXkFtZTYwNDAzNTU3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/5/8l/u7cyb_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/p/4l/ql9wb_tnl_250x141.jpg?ts=20140405112550,Ricky Bobby - A Toda Velocidade',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzAzOTk1OTIyM15BMl5BanBnXkFtZTcwNDIzNTQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/x/r6/0gvlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'VIAGEM MALDITA 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzk0MTg5MzEyOF5BMl5BanBnXkFtZTcwNDUyMzIzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://srv.vplayer.tk/movie/viagemmaldita2.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Menina Ma.com',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc0MzgzNTI3N15BMl5BanBnXkFtZTcwNDk3MDIzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/n6/ty2lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',O Senhor das Armas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYzZWE3MDAtZjZkMi00MzhlLTlhZDUtNmI2Zjg3OWVlZWI0XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/z6/2tvlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Os Produtores',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA3NjAyNzg2OF5BMl5BanBnXkFtZTcwOTIyMDUzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/d/l6/bdwlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Os Reis de Dogtown',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDBhNGJlOTAtM2ExNi00NmEzLWFmZTQtYTZhYTRlNjJjODhmXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/n6/39ulf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Tempos de Violencia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk0Mzc1NTY1N15BMl5BanBnXkFtZTYwMTMxOTY3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/d6/b0vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'A Chave Mestra',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTMxNDYzODE3NF5BMl5BanBnXkFtZTcwMDc1NDAzMQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/YnPqWkGkDu0iAyqYXFdaYOYjBNWTGTBmzOzBJhls5E5RtnpsvnnhEdknCS45KrgJr9agza89rg=m18',
                       'genre': 'Filmes'},

                       {'name': 'A Hora do Rango',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODA1NDYyNjYtZDJkMi00NzAwLTkyN2UtNjI1YzdmNTIxZjFhXkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/l6/7ewlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'A Hora do Rango',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODA1NDYyNjYtZDJkMi00NzAwLTkyN2UtNjI1YzdmNTIxZjFhXkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/l6/7ewlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'A Hora do Rango',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODA1NDYyNjYtZDJkMi00NzAwLTkyN2UtNjI1YzdmNTIxZjFhXkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/l6/7ewlf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'A Lula E A Baleia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg1NTE4NTc3NV5BMl5BanBnXkFtZTgwNDA1NDI1MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/5/f6/17ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'A Lula e a Baleia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg1NTE4NTc3NV5BMl5BanBnXkFtZTgwNDA1NDI1MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/5/f6/17ylf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'BOA SORTE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY0NzQ2NDg2Ml5BMl5BanBnXkFtZTYwMzcwOTY2._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/QoAVB10xOgUyyI6cGzs0w1KrVL2l-JdRheIEYdUDJhM8XITSxE0DgR7HyBrGzkXZty9VsecGJQ=m22',
                       'genre': 'Filmes'},

                       {'name': 'BOA SORTE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY0NzQ2NDg2Ml5BMl5BanBnXkFtZTYwMzcwOTY2._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/QoAVB10xOgUyyI6cGzs0w1KrVL2l-JdRheIEYdUDJhM8XITSxE0DgR7HyBrGzkXZty9VsecGJQ=m37',
                       'genre': 'Filmes'},

                       {'name': 'Boa Sorte',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY0NzQ2NDg2Ml5BMl5BanBnXkFtZTYwMzcwOTY2._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/IfESROafKmdIwS26nrmI0uI5HI6uCMh16BOauBfrUZqtzF1I6rKUCsVLPtjWncBnkME=m18',
                       'genre': 'Filmes'},

                       {'name': 'Boa Sorte',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY0NzQ2NDg2Ml5BMl5BanBnXkFtZTYwMzcwOTY2._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/IfESROafKmdIwS26nrmI0uI5HI6uCMh16BOauBfrUZqtzF1I6rKUCsVLPtjWncBnkME=m18',
                       'genre': 'Filmes'},

                       {'name': 'Brokeback Mountain',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY5NTAzNTc1NF5BMl5BanBnXkFtZTYwNDY4MDc3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/t/am/vddyb_480p_1mbps.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Cache-cache',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk2NjM3NTM5MV5BMl5BanBnXkFtZTcwNTgyNzEzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/iXBOz4w9-a2p96QBCn-C6tyDOdAlwfTGWYFJArZd1nzFyrKFQWKtvze2QwPIpyJoBfA=m18',
                       'genre': 'Filmes'},

                       {'name': 'Constantine',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTE5NDk5NTUyN15BMl5BanBnXkFtZTYwNzUyMDA3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/dlnZgTV55Z3t18eGbhW7muszzU4u41AVL0vi29ZsZ70aex-aYEPyteV88mlTQkvZZ20=m18',
                       'genre': 'Filmes'},

                       {'name': 'Constantine',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTE5NDk5NTUyN15BMl5BanBnXkFtZTYwNzUyMDA3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/PflBK23RacIBId3EnpAtRIbwqbVBsoiGD8Ej75N8fFQBxyZK7W2uCqW1kzvEn6ClX3Dnw0ya=m22',
                       'genre': 'Filmes'},

                       {'name': 'Constantine',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTE5NDk5NTUyN15BMl5BanBnXkFtZTYwNzUyMDA3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/dlnZgTV55Z3t18eGbhW7muszzU4u41AVL0vi29ZsZ70aex-aYEPyteV88mlTQkvZZ20=m18',
                       'genre': 'Filmes'},

                       {'name': 'DEU A LOUCA NA CHAPEUZINHO 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUxOTQxMTIyNl5BMl5BanBnXkFtZTcwOTAzNDEzMQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'http://srv.vplayer.tk/movie/deualocanachapeuzinho2.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Flores Partidas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ4OTk1MTYxM15BMl5BanBnXkFtZTcwMTYwNjAzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/z6/0tvlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'FOUR BROTHERS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU4NzM3Njg2NV5BMl5BanBnXkFtZTcwNjU4NDczMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/fourb.mp4',
                       'genre': ''},

                       {'name': 'Menina Ma.com',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc0MzgzNTI3N15BMl5BanBnXkFtZTcwNDk3MDIzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/n6/ty2lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Menina Ma.com',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc0MzgzNTI3N15BMl5BanBnXkFtZTcwNDk3MDIzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/n6/ty2lf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'O GUIA MOCHILEIRO DAS GALAXIAS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZmU5MGU4MjctNjA2OC00N2FhLWFhNWQtMzQyMGI2ZmQ0Y2YyL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/tclKI1eZqsk73s508a_ebpNq4nBKtjEu7rd2Z4WuVCXW0zvXvFJVixyKkt50VcyUqfjsSz-tINEgkg=m22',
                       'genre': 'Filmes'},

                       {'name': 'O Segredo de Brokeback Mountain',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY5NTAzNTc1NF5BMl5BanBnXkFtZTYwNDY4MDc3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/k/l6/2dwlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'O Segredo de Brokeback Mountain',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY5NTAzNTc1NF5BMl5BanBnXkFtZTYwNDY4MDc3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/k/l6/2dwlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Segredo de Brokeback Mountain',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY5NTAzNTc1NF5BMl5BanBnXkFtZTYwNDY4MDc3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/k/l6/2dwlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'O Senhor Das Armas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYzZWE3MDAtZjZkMi00MzhlLTlhZDUtNmI2Zjg3OWVlZWI0XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/z6/2tvlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'O Senhor das Armas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYzZWE3MDAtZjZkMi00MzhlLTlhZDUtNmI2Zjg3OWVlZWI0XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/z6/2tvlf_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'O Senhor das Armas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYzZWE3MDAtZjZkMi00MzhlLTlhZDUtNmI2Zjg3OWVlZWI0XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/z6/2tvlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'OS PENETRAS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZmJkNzViYjYtZWZlNy00OGE4LWI2MzUtYTcwNjY3Y2MyODIwXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/Fh3qZPXfZYzE9UDnD-nuAW2VerQ5pe0gKzy0c-eLPfqW8NpmZl-q_n2YNryzJTlV3pZ-JOHLrw=m22',
                       'genre': 'Filmes'},

                       {'name': 'Os Produtores',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA3NjAyNzg2OF5BMl5BanBnXkFtZTcwOTIyMDUzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/d/l6/bdwlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Os Produtores',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA3NjAyNzg2OF5BMl5BanBnXkFtZTcwOTIyMDUzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/d/l6/bdwlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Os Produtores',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA3NjAyNzg2OF5BMl5BanBnXkFtZTcwOTIyMDUzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/d/l6/bdwlf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'Os Reis de dogtown',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDBhNGJlOTAtM2ExNi00NmEzLWFmZTQtYTZhYTRlNjJjODhmXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/n6/39ulf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Os Reis de Dogtown',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDBhNGJlOTAtM2ExNi00NmEzLWFmZTQtYTZhYTRlNjJjODhmXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/n6/39ulf_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'Os Reis de Dogtown',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDBhNGJlOTAtM2ExNi00NmEzLWFmZTQtYTZhYTRlNjJjODhmXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/n6/39ulf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Sr. & Sra. Smith',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTUxMzcxNzQzOF5BMl5BanBnXkFtZTcwMzQxNjUyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/1MImnFND8-h7johkM6ukzjsAuo4ZN_D16xvK4j_F0uMxQnqTmshGamCQcCMKoC4pbUWYVPIP09w=m22',
                       'genre': 'Filmes'},

                       {'name': 'Tempos de Violencia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk0Mzc1NTY1N15BMl5BanBnXkFtZTYwMTMxOTY3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/d6/b0vlf_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'Tempos de Violencia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk0Mzc1NTY1N15BMl5BanBnXkFtZTYwMTMxOTY3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/d6/b0vlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Tempos de Violencia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk0Mzc1NTY1N15BMl5BanBnXkFtZTYwMTMxOTY3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/d6/b0vlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/r/am/mddyb_tnl_2 8.jpg?ts=20130911200444,A Hora do Rango',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODA1NDYyNjYtZDJkMi00NzAwLTkyN2UtNjI1YzdmNTIxZjFhXkEyXkFqcGdeQXVyNjExODE1MDc@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/l6/7ewlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/t/am/vddyb_tnl_2 8.jpg?ts=20130912041715,O Segredo de Brokeback Mountain',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY5NTAzNTc1NF5BMl5BanBnXkFtZTYwNDY4MDc3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/k/l6/2dwlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'UM MUNDO NOVO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTdjNjQ5ZTAtODJlZi00MzcyLWJjY2UtNDZhNTJkYjlkNGY5XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/mbM6lOQ4kxWAZHFVY_inxmVicKr5Y2WKJ3Bjcq2XDZT27yXBRvpsIjaHuN4l_onjySu7wPy3=m22',
                       'genre': 'Filmes'},

                       {'name': 'Wolf Creek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMjYwNTU4N15BMl5BanBnXkFtZTcwMjk0OTgzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=40792f82ff5e3565',
                       'genre': 'Wolf Creek LEG'},

                       {'name': 'Wolf Creek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMjYwNTU4N15BMl5BanBnXkFtZTcwMjk0OTgzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d388f2876ee476e',
                       'genre': 'Wolf Creek LEG'},

                       {'name': 'Wolf Creek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMjYwNTU4N15BMl5BanBnXkFtZTcwMjk0OTgzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d514dac6a8678689',
                       'genre': 'Wolf Creek LEG'},

                       {'name': 'Wolf Creek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMjYwNTU4N15BMl5BanBnXkFtZTcwMjk0OTgzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=42a72115d23e7f67',
                       'genre': 'Wolf Creek LEG'},

                       {'name': 'Wolf Creek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMjYwNTU4N15BMl5BanBnXkFtZTcwMjk0OTgzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=35fa823af9197905',
                       'genre': 'Wolf Creek LEG'},

                       {'name': 'Wolf Creek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMjYwNTU4N15BMl5BanBnXkFtZTcwMjk0OTgzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=527cf804a6fd8a01',
                       'genre': 'Wolf Creek LEG'},

                       {'name': 'Wolf Creek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMjYwNTU4N15BMl5BanBnXkFtZTcwMjk0OTgzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=be9678f32de8e0b3',
                       'genre': 'Wolf Creek LEG'},

                       {'name': 'Wolf Creek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMjYwNTU4N15BMl5BanBnXkFtZTcwMjk0OTgzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d3752b8a731cab1e',
                       'genre': 'Wolf Creek LEG'},

                       {'name': 'Wolf Creek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMjYwNTU4N15BMl5BanBnXkFtZTcwMjk0OTgzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=8a1b850c92bb43b0',
                       'genre': 'Wolf Creek LEG'},

                       {'name': 'Wolf Creek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMjYwNTU4N15BMl5BanBnXkFtZTcwMjk0OTgzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=c2946989469ab52d',
                       'genre': 'Wolf Creek LEG'},

                       {'name': 'Wolf Creek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMjYwNTU4N15BMl5BanBnXkFtZTcwMjk0OTgzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=2d9b3bf3373b7813',
                       'genre': 'Wolf Creek LEG'},

                       {'name': 'Wolf Creek',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMjYwNTU4N15BMl5BanBnXkFtZTcwMjk0OTgzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=888850735c462e7d',
                       'genre': 'Wolf Creek LEG'},

                       {'name': ',Um Amor de Verao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg2NTM0NDY1NV5BMl5BanBnXkFtZTcwMjU5OTkyMQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/16/0o1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Uma Garota Encantada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGI1MjMzMWEtZDc3Ni00Y2RiLTllOGQtMTVlZjRkOGE3MGNlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/h6/57vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'A QUEDA - AS ULTIMAS HORAS DE HITLER',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGU0MDlmYjYtNWI3Yy00OWJiLTljZTItNjBlMjMwMWFkZDllXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/bHvBlOkU4u1LW4qe_JKOdkehZ0pBwzD1efmqeTJp_YVB7GvYIgC6BlmLE20QTcI0VvTmVNBV0K2oxA=m22',
                       'genre': 'Filmes'},

                       {'name': 'A Supremacia Bourne',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTIyMDFmMmItMWQzYy00MjBiLTg2M2UtM2JiNDRhOWE4NjBhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/tEZUONlMyzTr3fBOBLMNrJCO34oJ8v9uIrThgROeuxvuIRiwNVmxCGdttfiYOgEiWDcNVoTJDvp77vy2RA=m22',
                       'genre': 'Filmes'},

                       {'name': 'ANCHORMAN THE LEGEND OF RON BURGUNDY',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ2MzYwMzk5Ml5BMl5BanBnXkFtZTcwOTI4NzUyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/anchorman.mp4',
                       'genre': ''},

                       {'name': 'ANTARES TV',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTYxMmQxY2UtMmQ3ZC00MDIyLWFhMzYtNjc3ZTZiYWU5MjUzXkEyXkFqcGdeQXVyNDkzNTM2ODg@._V1_UY268_CR9,0,182,268_AL_.jpg',
                       'video': 'http://173.192.105.252:1935/iptvantares/liveantarestv/playlist.m3u8',
                       'genre': ''},

                       {'name': 'Closer',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BN2I0Y2JmZjQtNjEyOC00ODhkLWE5YWUtOWFkOGQwMGYyODRiXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/vfA6IcLnwYWWBIiwCqGujDRvY_Da2W4m5p9fyYaUexycJyCft_2uw7Nn9sLeGu-1qLA=m18',
                       'genre': 'Filmes'},

                       {'name': 'Como Se Fosse a Primeira Vez',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjAwMzc4MDgxNF5BMl5BanBnXkFtZTYwNjUwMzE3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/56/uv1lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Como Se Fosse a Primeira Vez',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjAwMzc4MDgxNF5BMl5BanBnXkFtZTYwNjUwMzE3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/56/uv1lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Crash: No Limite',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTk1OTA1MjIyNV5BMl5BanBnXkFtZTcwODQxMTkyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/z6/usvlf_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'Crash: No Limite',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTk1OTA1MjIyNV5BMl5BanBnXkFtZTcwODQxMTkyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/z6/usvlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Crash: No Limite',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTk1OTA1MjIyNV5BMl5BanBnXkFtZTcwODQxMTkyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/z6/usvlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Crash: No Limite',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTk1OTA1MjIyNV5BMl5BanBnXkFtZTcwODQxMTkyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/z6/usvlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Diário de Uma Paixão',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk3OTM5Njg5M15BMl5BanBnXkFtZTYwMzA0ODI3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/jTYYJQxiSyRhdJ1h15vZCyx7C6GdhwcEJ0F2bm3QXPkFDXBAOtKfXWlz7VjvEh4Rb8c1favh7g=m18',
                       'genre': 'Filmes'},

                       {'name': 'Diário de uma Paixão',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTk3OTM5Njg5M15BMl5BanBnXkFtZTYwMzA0ODI3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://proxy-20.nyc.dailymotion.com/sec(6bbf393b29ef5a0325f4f6fea2b3d1b4)/video/594/513/156315495_mp4_h264_aac_hd.m3u8',
                       'genre': 'Filmes'},

                       {'name': 'Hotel Ruanda',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGJjYmIzZmQtNWE4Yy00ZGVmLWJkZGEtMzUzNmQ4ZWFlMjRhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/0/d6/a4vlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Hotel Ruanda',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGJjYmIzZmQtNWE4Yy00ZGVmLWJkZGEtMzUzNmQ4ZWFlMjRhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/0/d6/a4vlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Hotel Ruanda',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGJjYmIzZmQtNWE4Yy00ZGVmLWJkZGEtMzUzNmQ4ZWFlMjRhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/0/d6/a4vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Hotel Ruanda',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGJjYmIzZmQtNWE4Yy00ZGVmLWJkZGEtMzUzNmQ4ZWFlMjRhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/0/d6/a4vlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Kung-Fusão',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYmNhNzE2YjEtMDNmNS00ZGNkLTljZjktYTdlNGNmYzBmNjIyL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/s/n6/65ulf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Kung-Fusao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYmNhNzE2YjEtMDNmNS00ZGNkLTljZjktYTdlNGNmYzBmNjIyL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/s/n6/65ulf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Madrugada dos Mortos',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BN2M2ZmU2OGQtNmU5Yi00MTIyLTgwNWMtYjljMzZlYTdiNjBhXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/tD_KadEQEfTOhDuRYuRr_a-k0oiCW5eTQ_3gqqoAN7mrXEpzGfpNpwnqNhXAiv1eOsPYhsrKJHhyhdk9hQ=m22',
                       'genre': 'Filmes'},

                       {'name': 'Mindhunter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAwOTY3NDM1NjNeQTJeQWpwZ15BbWU3MDEzMjU1MjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=e3e4d1c47645cf08',
                       'genre': 'Originais Netflix'},

                       {'name': 'Mindhunter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAwOTY3NDM1NjNeQTJeQWpwZ15BbWU3MDEzMjU1MjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=df8da70b9a20e48f',
                       'genre': 'Originais Netflix'},

                       {'name': 'Mindhunter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAwOTY3NDM1NjNeQTJeQWpwZ15BbWU3MDEzMjU1MjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=c74971682b7af583',
                       'genre': 'Originais Netflix'},

                       {'name': 'Mindhunter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAwOTY3NDM1NjNeQTJeQWpwZ15BbWU3MDEzMjU1MjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=7d43a26d7a5c722d',
                       'genre': 'Originais Netflix'},

                       {'name': 'Mindhunter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAwOTY3NDM1NjNeQTJeQWpwZ15BbWU3MDEzMjU1MjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=911aa932bb248160',
                       'genre': 'Originais Netflix'},

                       {'name': 'Mindhunter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAwOTY3NDM1NjNeQTJeQWpwZ15BbWU3MDEzMjU1MjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=da2296eba20e34b',
                       'genre': 'Originais Netflix'},

                       {'name': 'Mindhunter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAwOTY3NDM1NjNeQTJeQWpwZ15BbWU3MDEzMjU1MjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=33fb9946b444878b',
                       'genre': 'Originais Netflix'},

                       {'name': 'Mindhunter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAwOTY3NDM1NjNeQTJeQWpwZ15BbWU3MDEzMjU1MjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=89922dd39f49441d',
                       'genre': 'Originais Netflix'},

                       {'name': 'Mindhunter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAwOTY3NDM1NjNeQTJeQWpwZ15BbWU3MDEzMjU1MjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=80230d8db1dd0f83',
                       'genre': 'Originais Netflix'},

                       {'name': 'Mindhunter',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAwOTY3NDM1NjNeQTJeQWpwZ15BbWU3MDEzMjU1MjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=916cf8db97b695fa',
                       'genre': 'Originais Netflix'},

                       {'name': 'Nem Tudo é o Que Parece',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI5MTE1OTAzOV5BMl5BanBnXkFtZTcwNDc2OTgyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/z6/2qvlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'O Castelo Animado',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZTRhY2QwM2UtNWRlNy00ZWQwLTg3MjktZThmNjQ3NTdjN2IxXkEyXkFqcGdeQXVyMzg2MzE2OTE@._V1_UY268_CR5,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/92-GOYuujSk7RrE4Yut163TDhwOceouApzFRLmf4UiOlcmtqWCCJ-HfIqybXuPi-eaRKPJqfJS1wqTq5zXkbjlW3Fg3ThjvTx0PXsmJkrqubdonEos6MqZ3oWQYiYEOUiYHrmPzC_g=m22',
                       'genre': 'ANIMACAO'},

                       {'name': 'Resident Evil - Apocalipse',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc1NTUxMzk0Nl5BMl5BanBnXkFtZTcwNDQ1MDIzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/v/n6/g6ulf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Resident Evil - Apocalipse',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc1NTUxMzk0Nl5BMl5BanBnXkFtZTcwNDQ1MDIzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/v/n6/g6ulf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Spotless',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=86c3fb6e1ad6e30',
                       'genre': 'Spotless LEG'},

                       {'name': 'Spotless',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=5975279feafe6ae5',
                       'genre': 'Spotless LEG'},

                       {'name': 'Spotless',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=13e9577b210e5b35',
                       'genre': 'Spotless LEG'},

                       {'name': 'Spotless',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=4924614e3270f3a1',
                       'genre': 'Spotless LEG'},

                       {'name': 'Spotless',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=ce3053fdf689b505',
                       'genre': 'Spotless LEG'},

                       {'name': 'Spotless',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=520352d710e4b335',
                       'genre': 'Spotless LEG'},

                       {'name': 'Spotless',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d4fc7355147ea42c',
                       'genre': 'Spotless LEG'},

                       {'name': 'Spotless',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=b15104bbee4aa68e',
                       'genre': 'Spotless LEG'},

                       {'name': 'Spotless',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=679bf67e35e58bf0',
                       'genre': 'Spotless LEG'},

                       {'name': 'Spotless',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=4ee89ff55edafa77',
                       'genre': 'Spotless LEG'},

                       {'name': 'THE BOURNE SUPREMACY',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTIyMDFmMmItMWQzYy00MjBiLTg2M2UtM2JiNDRhOWE4NjBhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/bourne2.mp4',
                       'genre': ''},

                       {'name': 'THE DAY AFTER TOMORROW',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTU1NTA3NzMwOV5BMl5BanBnXkFtZTcwNzEzMTEzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/theday2004.mp4',
                       'genre': ''},

                       {'name': 'The Passion of the Christ',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDY1N2IyYWMtZTY4OS00OGM1LTkxNmUtOTQzYmM5MmI2YmVmXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/x4sDIgEZ0ZTrVPxS106owD5_udbBOecMB3Lw6b8IABVzsLACI7VjExGaTt_aHTDKx1HkMsyw=m22',
                       'genre': 'Filmes'},

                       {'name': 'Todo Mundo Quase Morto',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg5Mjk2NDMtZTk0Ny00YTQ0LWIzYWEtMWI5MGQ0Mjg1OTNkXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/U4sQ9Q63ZsWI9qUSwfwhejHGjiRNOVtUQxjyhiyGY57gxBR0ddsgFqCMNuYIi6eAzZc=m18',
                       'genre': 'Filmes'},

                       {'name': 'TV Antares',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTYxMmQxY2UtMmQ3ZC00MDIyLWFhMzYtNjc3ZTZiYWU5MjUzXkEyXkFqcGdeQXVyNDkzNTM2ODg@._V1_UY268_CR9,0,182,268_AL_.jpg',
                       'video': 'http://srv3.zoeweb.tv:1935/z99-live/stream/livestream.m3u8',
                       'genre': 'BRAZIL'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/u/56/rv1lf_tnl_2 8.jpg?ts=20141111004527,A Janela Secreta',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNmI5MWNlMjYtZTAxNy00N2Q3LTkwZDgtMWRjOWQ1ZjJiN2Y4XkEyXkFqcGdeQXVyNDQ2MTMzODA@._V1_UY268_CR5,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/56/rv1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/v/n6/g6ulf_tnl_2 8.jpg?ts=20140828000203,Resident Evil - Apocalipse',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTc1NTUxMzk0Nl5BMl5BanBnXkFtZTcwNDQ1MDIzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/v/n6/g6ulf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Um Amor de Verao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg2NTM0NDY1NV5BMl5BanBnXkFtZTcwMjU5OTkyMQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/16/0o1lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Um Amor de Verao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg2NTM0NDY1NV5BMl5BanBnXkFtZTcwMjU5OTkyMQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/16/0o1lf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Um Amor de Verao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTg2NTM0NDY1NV5BMl5BanBnXkFtZTcwMjU5OTkyMQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/16/0o1lf_480p.mp4?',
                       'genre': 'ROMANCE'},

                       {'name': 'Uma Garota Encantada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGI1MjMzMWEtZDc3Ni00Y2RiLTllOGQtMTVlZjRkOGE3MGNlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/h6/57vlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Uma Garota Encantada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGI1MjMzMWEtZDc3Ni00Y2RiLTllOGQtMTVlZjRkOGE3MGNlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/h6/57vlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=a74735d107566069',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=6a7d1579b02f6f22',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=e4dc5948d0dea851',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=69416ef40fc3bab2',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=dc0efa1b90f2fe56',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=be1271015f5f79ef',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=702aacfab49d4f6c',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=79205b3d4716ccc7',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=ec1cdc1e526d7e13',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=b65331e90dac6324',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=1f746dbc169235fc',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=438cc33720d21583',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=fd43dcc65bbb9ade',
                       'genre': 'Van Helsing DUB'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=46a5d6a860f72025',
                       'genre': 'Van Helsing LEG'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=50994959babc6120',
                       'genre': 'Van Helsing LEG'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=ccc13a636241b2b2',
                       'genre': 'Van Helsing LEG'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=ec2b208cdf1afd03',
                       'genre': 'Van Helsing LEG'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=1b3cc661d3dceec1',
                       'genre': 'Van Helsing LEG'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=e81768ea68148bc5',
                       'genre': 'Van Helsing LEG'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=f9b3fecdd793a083',
                       'genre': 'Van Helsing LEG'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=e83a5dc72e5e3939',
                       'genre': 'Van Helsing LEG'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=46a54784946b5c51',
                       'genre': 'Van Helsing LEG'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=a2aeba4a9fe9edb4',
                       'genre': 'Van Helsing LEG'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=6766c1993f3da253',
                       'genre': 'Van Helsing LEG'},

                       {'name': 'Van Helsing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODRmY2NhNDItOWViNi00OTIyLTk3YjYtYzY0YTFlMDg1YzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=63a3d618524490f7',
                       'genre': 'Van Helsing LEG'},

                       {'name': ',Desaparecidas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/9/l6/wjwlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Lagrimas do Sol',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmI3YjQ4NjctZTk0Zi00ZDFhLTgyZjAtYWRjZTJjMjMwNjM2L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/7/16/1p1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Desaparecidas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/9/l6/wjwlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Desaparecidas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/9/l6/wjwlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Escola De Rock',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/dkwcaU2Dhn7UFZXeFKD9jDkxcWBn87M1hE2awbVIeM5RE9PqTZoEGd5GQ-56Tur0otzcCoVbtaGRvvbklw=m22',
                       'genre': 'Filmes'},

                       {'name': 'FINDING NEMO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjMxYzBiNjUtZDliNC00MDAyLTg3N2QtOWNjNmNhZGQzNDg5XkEyXkFqcGdeQXVyNjE2MjQwNjc@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/nemo2003.mp4',
                       'genre': ''},

                       {'name': 'Lagrimas do Sol',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmI3YjQ4NjctZTk0Zi00ZDFhLTgyZjAtYWRjZTJjMjMwNjM2L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/7/16/1p1lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Lagrimas do Sol',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmI3YjQ4NjctZTk0Zi00ZDFhLTgyZjAtYWRjZTJjMjMwNjM2L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/7/16/1p1lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Mystic River',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzNDUyMjA4MV5BMl5BanBnXkFtZTYwNDc4ODM3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/mdlGH1FI0_csxftHvCOppyCyOD3f5wUgCvAQnN_9l6jwPkaliZ5DtoiOypqv1FD2naA=m18',
                       'genre': 'Filmes'},

                       {'name': 'O Senhor dos Anéis - O Retorno do Rei',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWY1ZWQ5YjMtMDE0MS00NWIzLWE1M2YtODYzYTk2OTNlYWZmXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/-5bfqjTOINkzsW0tdWn1EI_Pyow7FQ7y31eevOxelLqUxW5g-uwdp5Qb-U93Bh-P57xNgg-iuKwf9p5fZg=m22',
                       'genre': 'Filmes'},

                       {'name': 'OLD SCHOOL',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BN2VjNDQ4MDctMDY3Yy00MmZmLTlhM2MtMWE4NjJhZTlmNTAxL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/oldschool1.mp4',
                       'genre': ''},

                       {'name': 'Ong-Bak - Guerreiro Sagrado',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIzMTUzMzc2MF5BMl5BanBnXkFtZTcwMjIyMzAzMQ@@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/n6/sy2lf_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'Premonição 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjExMTMyODAzN15BMl5BanBnXkFtZTYwNjc5NDQ3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://transfvanila1.com/videos/RedeCanais/RCFServer1/ondemand/PRMNCAO2.mp4',
                       'genre': 'Filmes'},

                       {'name': 'THE LORD OF THE RINGS:THE RETURN OF THE KING',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWY1ZWQ5YjMtMDE0MS00NWIzLWE1M2YtODYzYTk2OTNlYWZmXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/returnking1.mp4',
                       'genre': ''},

                       {'name': 'THE MATRIX RELOADED',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYzM3OGVkMjMtNDk3NS00NDk5LWJjZjUtYTVkZTIyNmQxNDMxXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/matrix2.mp4',
                       'genre': ''},

                       {'name': 'THE MATRIX REVOLUTIONS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzNlZTZjMDctZjYwNi00NzljLWIwN2QtZWZmYmJiYzQ0MTk2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/matrix3.mp4',
                       'genre': ''},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=3c7b335e9b08f95c',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=97e90c2f1760de65',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=acf8555d553012f4',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=409f3cb1bc2ed94c',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=6f5d090012552800',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=47df111ac82df945',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=5f2e7e1d5989b501',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=fb70652929b413a1',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=9794c006d1497806',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=797bc551700f3b72',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=be19a663d60b60cd',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=73f8f5f58abf17cd',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=ff7dcfe199cab6f7',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=7e3be2fb58120dff',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=28866669dfe462ca',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Missing',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=4a8120a634f2e79',
                       'genre': 'The Missing LEG'},

                       {'name': 'The Recruit',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjE5MDMzOTk3MV5BMl5BanBnXkFtZTYwNTE0NTg2._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/r3OBzkUADbVFk3yxHiqkrPdGoJ53ka7JnWumB90ijltGwUv3r7NMWB4xq14ifaJd6SU=m18',
                       'genre': 'Filmes'},

                       {'name': 'TV Aparecida',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWM1ZmU5NWItZDM0ZC00MTk5LThiMTktZGUxOThjNzI5NTcyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://caikron.com.br:1935/tvaparecida/tvaparecida.stream/playlist.m3u8?PEDROJUNIORTUTORIAIS',
                       'genre': 'Filmes'},

                       {'name': ',A festa nunca termina',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BM2YxZDgyNzMtODVmNi00NDE2LWI0MTQtNDIzMWQ0MmEzMmZjXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/f6/85ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',A Guerra de Hart',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYzMDg5ODQ1OF5BMl5BanBnXkFtZTYwMjc2Nzc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/v6/01zlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',A Ultima Profecia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjVmNDNjYWYtNzk0Mi00ZTU4LTljNDYtNDczZDE4NGMzZmQwXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/n6/zy2lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Ouro Branco',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTQ1NTUwNTAzN15BMl5BanBnXkFtZTYwMzM0Njk5._V1_UY268_CR4,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/h6/y7vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Resident Evil - O Hospede Maldito',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BN2Y2MTljNjMtMDRlNi00ZWNhLThmMWItYTlmZjYyZDk4NzYxXkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/b/h6/q8vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': '28 DAYS LATER',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTFkM2ViMmQtZmI5NS00MjQ2LWEyN2EtMTI1ZmNlZDU3MTZjXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/28days.mp4',
                       'genre': ''},

                       {'name': 'A festa nunca termina',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BM2YxZDgyNzMtODVmNi00NDE2LWI0MTQtNDIzMWQ0MmEzMmZjXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/f6/85ylf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'A festa nunca termina',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BM2YxZDgyNzMtODVmNi00NDE2LWI0MTQtNDIzMWQ0MmEzMmZjXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/f6/85ylf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'A festa nunca termina',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BM2YxZDgyNzMtODVmNi00NDE2LWI0MTQtNDIzMWQ0MmEzMmZjXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/f6/85ylf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'A Guerra de Hart',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYzMDg5ODQ1OF5BMl5BanBnXkFtZTYwMjc2Nzc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/v6/01zlf_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'A Guerra de Hart',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYzMDg5ODQ1OF5BMl5BanBnXkFtZTYwMjc2Nzc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/v6/01zlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'A Guerra De Hart',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYzMDg5ODQ1OF5BMl5BanBnXkFtZTYwMjc2Nzc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/v6/01zlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'A Ultima Profecia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjVmNDNjYWYtNzk0Mi00ZTU4LTljNDYtNDczZDE4NGMzZmQwXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/n6/zy2lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Femme Fatale',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGM5NWVhYTMtZjg5Zi00ODVkLWFmM2ItMDZkMTA5NGQzMDQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/c/16/e7wlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Femme Fatale',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGM5NWVhYTMtZjg5Zi00ODVkLWFmM2ItMDZkMTA5NGQzMDQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/c/16/e7wlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Harry Potter e a Camara Secreta',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTcxODgwMDkxNV5BMl5BanBnXkFtZTYwMDk2MDg3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/nW2IhHUyTvHCsar2-1HMIEcZz6zKOxiMT-8_EjrGPB6rY-rLaMGT5C5Yx-pkgiz_8wSrg_YR=m22',
                       'genre': 'Filmes'},

                       {'name': 'JACKASS 3D',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTgwMmU0YzktOGNhNi00MDcyLTg1OGEtZGQwM2RlMTAyYzhlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/jackass3d.mp4',
                       'genre': ''},

                       {'name': 'Laurel Canyon - A Rua das Tentacoes',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTgxMjMxMDA2Ml5BMl5BanBnXkFtZTYwMjE5MTI3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/l6/8ewlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Laurel Canyon - A Rua das Tentacoes',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTgxMjMxMDA2Ml5BMl5BanBnXkFtZTYwMjE5MTI3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/l6/8ewlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Laurel Canyon - A Rua das Tentacoes',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTgxMjMxMDA2Ml5BMl5BanBnXkFtZTYwMjE5MTI3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/l6/8ewlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Nicholas Nickleby',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjQxNjMzODA3NF5BMl5BanBnXkFtZTgwMjU4MDcxMDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/a/h6/n8vlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Nicholas Nickleby',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjQxNjMzODA3NF5BMl5BanBnXkFtZTgwMjU4MDcxMDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/a/h6/n8vlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'O CONDE DE MONTE CRISTO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDM0ZWRjZDgtZWI0MS00ZTIzLTg4MWYtZjU5MDEyMDU0ODBjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/jjx5jWG9ol6ZNNyRmGH55BZwGzaeVtRAmDj5Ro5ZUHrNKecyDXZ41NYra9cP4b1tRBr3oDVFRmxcag=m22',
                       'genre': 'Filmes'},

                       {'name': 'O Senhor dos Anéis - As Duas Torres',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDY0NmI4ZjctN2VhZS00YzExLTkyZGItMTJhOTU5NTg4MDU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/nkqgwKXZHO1lvQFh-ulGM8krlUVdo4hyX9fjuLiA2hI1htN1uxW6pvYTmPPde4fQCCnTYIK22x3vbRy7Mg=m22',
                       'genre': 'Filmes'},

                       {'name': 'Ouro Branco',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTQ1NTUwNTAzN15BMl5BanBnXkFtZTYwMzM0Njk5._V1_UY268_CR4,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/h6/y7vlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Ouro Branco',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTQ1NTUwNTAzN15BMl5BanBnXkFtZTYwMzM0Njk5._V1_UY268_CR4,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/h6/y7vlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Ouro Branco',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTQ1NTUwNTAzN15BMl5BanBnXkFtZTYwMzM0Njk5._V1_UY268_CR4,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/h6/y7vlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'PAID IN FULL',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTQ1NTUwNTAzN15BMl5BanBnXkFtZTYwMzM0Njk5._V1_UY268_CR4,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/paidin.mp4',
                       'genre': ''},

                       {'name': 'Resident Evil - O Hospede Maldito',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BN2Y2MTljNjMtMDRlNi00ZWNhLThmMWItYTlmZjYyZDk4NzYxXkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/b/h6/q8vlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Resident Evil - O Hospede Maldito',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BN2Y2MTljNjMtMDRlNi00ZWNhLThmMWItYTlmZjYyZDk4NzYxXkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/b/h6/q8vlf_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'STAR WARS 2 - O ATAQUE DOS CLONES',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOWNkZmVjODAtNTFlYy00NTQwLWJhY2UtMmFmZTkyOWJmZjZiL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UY268_CR10,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/9euSzYWZLCyRincdWbU8PtiqnoKsJfRmVPMu55--51vhReJ4sLvsY1lcBuVWTaiqeqti2EfATjeMVcm4JA=m22',
                       'genre': 'Filmes'},

                       {'name': 'THE BOURNE IDENTITY',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BM2JkNGU0ZGMtZjVjNS00NjgyLWEyOWYtZmRmZGQyN2IxZjA2XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/bourne1.mp4',
                       'genre': ''},

                       {'name': 'THE LORD OF THE RINGS:THE 2 TOWERS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDY0NmI4ZjctN2VhZS00YzExLTkyZGItMTJhOTU5NTg4MDU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/twotowers.mp4',
                       'genre': ''},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/5/8l/y7cyb_tnl_2 8.jpg?ts=20130817044800,Nicholas Nickleby',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjQxNjMzODA3NF5BMl5BanBnXkFtZTgwMjU4MDcxMDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/a/h6/n8vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/s/im/cpdyb_tnl_2 8.jpg?ts=20131029003846,Femme Fatale',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMGM5NWVhYTMtZjg5Zi00ODVkLWFmM2ItMDZkMTA5NGQzMDQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/c/16/e7wlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://www.omelete.com.br/imagens/cinema/artigos/laurel_canyon/poster.jpg,Laurel Canyon - A Rua das Tentacoes',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTgxMjMxMDA2Ml5BMl5BanBnXkFtZTYwMjE5MTI3._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/l6/8ewlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Kung-Fu Futebol Clube',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjdiYTBiMDUtNTg0Yy00N2NhLWIxZmEtMTEwNDNlYzRkMGY3L2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR15,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/0/d6/83vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': '.1 Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=60254385fbb876d6',
                       'genre': 'Atlantis LEG'},

                       {'name': '.2 Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=ad787a8378115dca',
                       'genre': 'Atlantis LEG'},

                       {'name': 'A. I. INTELIGENCIA ARTIFICIAL',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNWU2NzEyMDYtM2MyOS00OGM3LWFkNzAtMzRiNzE2ZjU5ZTljXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/zGObhl09jf9_ArY7ePMbNZJER_KEKB4wTgJkM4JjoCL-qXwO4K17J606ojer_Me7mpn1LjPlDU442A=m22',
                       'genre': 'Filmes'},

                       {'name': 'A.I. Inteligência Artificial',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNWU2NzEyMDYtM2MyOS00OGM3LWFkNzAtMzRiNzE2ZjU5ZTljXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/gWGITRAsQQ4R-HMrWVp_WkzVHsMEEAk3IB9HRL60buqE_W-uUrUFZjxWts4luf8fsgeLXsDI07Cg9WynIUtqtcUasJ7g4ZpSA-vXVuy5Zna_XpHj8QSFYVHgGB56gjhgaLD-bMk=m18',
                       'genre': 'Filmes'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=50ff395640f5d745',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=426e72b5608c4804',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=39544e785fc11ea5',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=8e55bc94f902a4',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=fda11976b3ab0ef3',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=381225d6afbf14fe',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=f0e243f006eb70de',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=35474e0a05da0c41',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=2a710916fd539f2b',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=303f5f7cc706bbb',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=8cc1d4e751e3d3c8',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=e729b04b11cba9fb',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=9713235ec2bb829d',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=7edcd4e510c754f6',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d7056b40df988e7a',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=3cc4b7c46b5576d',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d8677749aea44b6e',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=55a94321724b6d0',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=bf04f5621e8ba473',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d279f580a01d7d4a',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=528266f26629fa70',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=7f32d1bd46957f66',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=681ef0c81f66d50b',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Atlantis',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjM2NzNjMDAtZTAyMi00NTQzLWFlMTctNTUzMGE1ODE2NDRlXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=f4f73f3b699ffecf',
                       'genre': 'Atlantis LEG'},

                       {'name': 'Falcão Negro em Perigo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWMwMzQxZjQtODM1YS00YmFiLTk1YjQtNzNiYWY1MDE4NTdiXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/sQbAzuFsJsdGlJsTnjedIv9Rw_83000o58cmuJ5CRwaYvG7OJ_-HnOiKk0YHYy38nXakKL3Fdg=m22',
                       'genre': 'Filmes'},

                       {'name': 'Final Fantasy',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWRjZTBlMWQtOGU2OS00NTNiLWEyNDUtNDA1NjI3ODE3OTJhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UY268_CR9,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/4LBIcNUlkjDN-fxn37Y_PN01uRmE3eogsT6kGjoFqx_tPA7MbM8iNQ4oo2KLhQiZgHQ3e6wHeg=m18',
                       'genre': 'Filmes'},

                       {'name': 'Kung-Fu Futebol Clube',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjdiYTBiMDUtNTg0Yy00N2NhLWIxZmEtMTEwNDNlYzRkMGY3L2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR15,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/0/d6/83vlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Kung-Fu Futebol Clube',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjdiYTBiMDUtNTg0Yy00N2NhLWIxZmEtMTEwNDNlYzRkMGY3L2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR15,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/0/d6/83vlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Kung-Fu Futebol Clube',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjdiYTBiMDUtNTg0Yy00N2NhLWIxZmEtMTEwNDNlYzRkMGY3L2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR15,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/0/d6/83vlf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'Le fabuleux destin dAmélie Poulain',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDg4NjM1YjMtYmNhZC00MjM0LWFiZmYtNGY1YjA3MzZmODc5XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/xK7PledMyqPBEB5guIRZWLXzTm5XxCs98rr5rDHfMHTdhU-AgODtQ5ogsSwYsVAIc-E=m22',
                       'genre': 'Filmes'},

                       {'name': 'Le pacte',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTkxMjg5MDYtZDkyMS00NjFlLTk5YTItMWUyOTNkOTg4YmRhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/cs9A3n0coNPiHzigwr83u0-IPMHDxHS9PURpi7LD2VWc3TYk40mkM-k8L9MSNlu95jo=m18',
                       'genre': 'Filmes'},

                       {'name': 'Moulin Rouge!',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMWFhYjliNjYtYjNhNS00OGExLWFhMjQtNDgwOWYyNWJiYzhmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/Z5UnWTTkWHFWYoC7IZ7wlncYT1sVhdKMKjRy_b6R30syihld43YhZYOkVnk7OLyjXgw=m18',
                       'genre': 'Filmes'},

                       {'name': 'O Senhor dos Anéis - A Sociedade do Anel',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/9hSGQ45SUUcuvErzNBN_sts_RGK7P3wMQo874dcqxZQyA17vNNttW6q9IVWrkCHf4DyJObUBOcSy-i9iUQ=m22',
                       'genre': 'Filmes'},

                       {'name': 'PEARL HARBOR',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ3MDc0MDc1NF5BMl5BanBnXkFtZTYwODI1ODY2._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/j4z51xiNcns1kZcud9IE-gYqb-g-AQbaL1jZk3h50th9q2l3sWaTF8Iumvmrz7SxSJv40wTnBd4C9DS1AJAH_In5FZ3uF5P61NKeWVGHYG8c8posMD3OBnXP8DBrjme3lDnJnr2KiipcQh4hoIhuflBbCQgG7a6DoHQ5Tw4lKUOSOpIW-UoXTiwv5MwmUD8hdbp0x8OnjeYfAeFU9Po6ICIh6VRIB-TyqF3WNWhz3UItG2YmAQHk6R6yoDZ3PS8e8FBhKxPcfoy6X2CG3lpoy3gp_WZ9PBKSZPAtUHz7ihsFOr05VscMXy2xMyQ-ThcoFdY9gOjVh4lbHKVL8uwVZc4L0YnF1DBMeDUNTePyzZtEJAlCctjghUtO1EDCkRb5r8b4jQ-5LAayR7kh4zXttI-It8sG-PsudLmdharvxOy8u8mCe0PVS2mlALgQ1NUfYjD67V-Qzkm7xTojP4fbTsPCvXe_oV6pCx6hLaDuGI-vniVa47tMCGatJij4vOin_UgDhG02OOFAEhL2BSosT6sTHuZ9374G-xS1Wn7l4musEQNxRMfHOWIZZjR18uJrDhfiEzvNaiCJ-bYc3-tdKN8h0LjpbjrkQrwbxPrgzSNDck2kr0y-ebuFT2lcllAzUHDDHCV6Aa6G_rzff0Vc-E1_P8DRXiKMm6x7sThGjqyNbA=m22',
                       'genre': 'Filmes'},

                       {'name': 'Rock Star',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzAxNzNmMzMtYTU4Ni00Y2IxLTk4MGEtZGExNmFiMzBjN2MyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/qV8dn6_guOoxNqCcf1mHqYBaTcUDzrz1OqunIeIMjVErPUOoM4XL0yUtW3lWAjDh-AHW-PZnxc36gjvIxw=m22',
                       'genre': 'Filmes'},

                       {'name': 'Swordfish',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzk5ZmQxMWYtM2QyNi00MTY3LTlmNjItYjUwODY3Y2YwOTIwXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/wuWAdgypi_-yhBtziUbo9ViuDHUGmMeJciecfcA3whVILxpLvYdFEIUlG0HEraxApvg=m18',
                       'genre': 'Filmes'},

                       {'name': 'THE LORD OF THE RINGS:THE FELLOWSHIP OF THE RING',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/fellowship1.mp4',
                       'genre': ''},

                       {'name': 'TRAINING DAY',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/training.mp4',
                       'genre': ''},

                       {'name': 'Training Day',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=38d3fbbef0ad1f98',
                       'genre': 'Training Day LEG'},

                       {'name': 'Training Day',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=90f1ba8476caa87f',
                       'genre': 'Training Day LEG'},

                       {'name': 'Training Day',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=8fb03042a0f7b82a',
                       'genre': 'Training Day LEG'},

                       {'name': 'Training Day',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=c27acc85f72f3e4',
                       'genre': 'Training Day LEG'},

                       {'name': 'Training Day',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d1b67a2f38dec0a7',
                       'genre': 'Training Day LEG'},

                       {'name': 'Training Day',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=c31de461fbfa57f7',
                       'genre': 'Training Day LEG'},

                       {'name': 'Training Day',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=27dd865707feac34',
                       'genre': 'Training Day LEG'},

                       {'name': 'Training Day',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=24ed858e8a85e213',
                       'genre': 'Training Day LEG'},

                       {'name': 'Training Day',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=18ebb3ea0bd5fbda',
                       'genre': 'Training Day LEG'},

                       {'name': 'Training Day',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=b048bc3354a27287',
                       'genre': 'Training Day LEG'},

                       {'name': 'Training Day',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=71b6eabca92b8d9f',
                       'genre': 'Training Day LEG'},

                       {'name': 'Training Day',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=790ad9903044e9ef',
                       'genre': 'Training Day LEG'},

                       {'name': 'CORPO FECHADO (240p A 720p)',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDIwMjAxNzktNmEzYS00ZDY5LWEyZjktM2Y0MmUzZDkyYmZkXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://content.uplynk.com/acde39d6f5554d52a64f1aa3e4244e00.m3u8',
                       'genre': 'Filmes'},

                       {'name': 'Erin Brockovich - Uma Mulher de Talento',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTA1NWRkNTktNDMxNS00NjE4LWEzMDAtNzA3YzlhYzRhNDA4L2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/f6/f5ylf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Erin Brockovich - Uma Mulher de Talento',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTA1NWRkNTktNDMxNS00NjE4LWEzMDAtNzA3YzlhYzRhNDA4L2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/f6/f5ylf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Erin Brockovich - Uma Mulher de Talento',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTA1NWRkNTktNDMxNS00NjE4LWEzMDAtNzA3YzlhYzRhNDA4L2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/f6/f5ylf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Premonição',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZTI0NGM2OGYtNzVmMi00NGQ2LTk2MDAtN2RmYjIzMGRkZGYxXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://transfvanila1.com/videos/RedeCanais/RCFServer1/ondemand/PRMNCAO1.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://4.bp.blogspot.com/_v42LCUO_1aQ/TL2LFXX-i3I/AAAAAAAABBA/xUJMV51UyKY/s1600/ErinBrockovich.jpeg,Erin Brockovich - Uma Mulher de Talento',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTA1NWRkNTktNDMxNS00NjE4LWEzMDAtNzA3YzlhYzRhNDA4L2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/f6/f5ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',8mm - Oito Milimetros',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjQwMmZmNWUtNGE0MS00ZjQ5LTkwNGItYWY3M2FhZDU5ZjBhXkEyXkFqcGdeQXVyNjU0NTI0Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/4/v6/51zlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',8mm - Oito Milimetros 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjQwMmZmNWUtNGE0MS00ZjQ5LTkwNGItYWY3M2FhZDU5ZjBhXkEyXkFqcGdeQXVyNjU0NTI0Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/9/v6/n2zlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',O Colecionador de Ossos',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOWQxN2ZmNDMtMzA2Ny00ZDJhLTlkNTgtMWMyZjljY2QzMzNhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/f/f6/14ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',O Paizao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjAzNzQ4YzEtZWFlOS00YWVkLWE2NDctZDBiZTUxYjgwOTYzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/v6/q1zlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=4fc3fc31c5cab647',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=bc3daee00b1bd07d',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=66fe3e3f462d9bfd',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=ac8ae20fc3c49d27',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=ee6c48b2201677b8',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=f070031cc138ce7a',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=1a8ce3d925734901',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d058b38fce71ad9a',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=fc9477e2494d16ca',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=367bfcee532b690b',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=ddda53204cf2bfa2',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=b026c7b35f062c20',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=95f5ab7bc0e02dae',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=1b81ce86058477d5',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d35ff38f2b423bfc',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=e9606ea35aa5c5eb',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=4f7eed42ca4c4e9e',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=29d05c0120b736a0',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=8e22220fa7bcc51f',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=7e0f197c0c78b85',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '13 Andar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODYxZTZlZTgtNTM5MC00N2RhLTg3MjUtNGVkMDJjMGY3YzA5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/t/96/301lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': '8mm - Oito Milimetros',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjQwMmZmNWUtNGE0MS00ZjQ5LTkwNGItYWY3M2FhZDU5ZjBhXkEyXkFqcGdeQXVyNjU0NTI0Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/4/v6/51zlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': '8mm - Oito Milimetros',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjQwMmZmNWUtNGE0MS00ZjQ5LTkwNGItYWY3M2FhZDU5ZjBhXkEyXkFqcGdeQXVyNjU0NTI0Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/4/v6/51zlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': '8mm - Oito Milimetros',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjQwMmZmNWUtNGE0MS00ZjQ5LTkwNGItYWY3M2FhZDU5ZjBhXkEyXkFqcGdeQXVyNjU0NTI0Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/4/v6/51zlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': '8mm - Oito Milimetros 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjQwMmZmNWUtNGE0MS00ZjQ5LTkwNGItYWY3M2FhZDU5ZjBhXkEyXkFqcGdeQXVyNjU0NTI0Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/9/v6/n2zlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': '8mm - Oito Milimetros 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjQwMmZmNWUtNGE0MS00ZjQ5LTkwNGItYWY3M2FhZDU5ZjBhXkEyXkFqcGdeQXVyNjU0NTI0Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/9/v6/n2zlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'A Bruxa de Blair',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzQ1NDBlNDItMDAyYS00YTI2LTgwMmYtMzAwMzg4NDFlM2ZmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/acL54MhPJD22e1G8iwl0L8YUp-sPFuIGrzfpMUrYCIHd7-96_UI535-hlV5ad28tzNYfZ8qELthkMA=m18',
                       'genre': 'Filmes'},

                       {'name': 'A BRUXA DE BLAIR',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzQ1NDBlNDItMDAyYS00YTI2LTgwMmYtMzAwMzg4NDFlM2ZmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/a/16/7y4lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'A Informante',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODg0YjAzNDQtOGFkMi00Yzk2LTg1NzYtYTNjY2UwZTM2ZDdkL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR2,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/l6/ydwlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'A Informante',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODg0YjAzNDQtOGFkMi00Yzk2LTg1NzYtYTNjY2UwZTM2ZDdkL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR2,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/l6/ydwlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'AUSTIN POWERS: THE SPY WHO SHAGGED ME',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmFkZGQxN2YtODNlYS00MzM5LTk3NjQtNTUxYmQ1YzkwMDhmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/austin2.mp4',
                       'genre': ''},

                       {'name': 'Clube da Luta',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzFjMWNhYzQtYTIxNC00ZWQ1LThiOTItNWQyZmMxNDYyMjA5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/DDGienbPyLgdJuQcDva10ZJcqSlIc0Qfx4ttlsGXSKziZRM6g_3YwXbTtHhXthp_1Uw=m18',
                       'genre': 'Filmes'},

                       {'name': 'Clube da Luta',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzFjMWNhYzQtYTIxNC00ZWQ1LThiOTItNWQyZmMxNDYyMjA5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/jBdvBzEJfwYOlq-zg3pFMcKnOizjvsN3UvDGos0DTJeq9UCeQazVwfabpHQDXNTY7JKM-e3uVw=m22',
                       'genre': 'Filmes'},

                       {'name': 'DOGMA',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYzAyOWUyZjQtNDBiMy00ZDExLTgwNmMtZDdmY2ViNzkyN2Y0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/dogma1999.mp4',
                       'genre': ''},

                       {'name': 'eXistenZ',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmU1MTJkYWItMzM5Ny00NDgxLTgxOGEtNTkzNDdkZjkwNGI0XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UY268_CR2,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/d6/m3vlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'eXistenZ',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmU1MTJkYWItMzM5Ny00NDgxLTgxOGEtNTkzNDdkZjkwNGI0XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UY268_CR2,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/d6/m3vlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Fight Club',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzFjMWNhYzQtYTIxNC00ZWQ1LThiOTItNWQyZmMxNDYyMjA5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/DDGienbPyLgdJuQcDva10ZJcqSlIc0Qfx4ttlsGXSKziZRM6g_3YwXbTtHhXthp_1Uw=m18',
                       'genre': 'Filmes'},

                       {'name': 'MORTOS DE FOME',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BY2JjMDJjMWMtMTI0OC00MzUxLWEwNTktZmRlY2M2YTYwNTZkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/h5GMi-Jl2MT66fXcC63cps9Fx7p823Y-uKLabyayH_hLOCq02sEFMdZJ14Z7h7bDo6jal2sBN0vrht7eOTRSBFmPTOgiSXN-aztK38qPAVH59NVHzHgFtJJviIE4LOzxjxy3dyYGnQ=m22',
                       'genre': 'Filmes'},

                       {'name': 'O Colecionador de Ossos',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOWQxN2ZmNDMtMzA2Ny00ZDJhLTlkNTgtMWMyZjljY2QzMzNhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/f/f6/14ylf_480p.mp4?',
                       'genre': 'TERROR'},

                       {'name': 'O Colecionador de Ossos',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOWQxN2ZmNDMtMzA2Ny00ZDJhLTlkNTgtMWMyZjljY2QzMzNhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/f/f6/14ylf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Colecionador de Ossos',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOWQxN2ZmNDMtMzA2Ny00ZDJhLTlkNTgtMWMyZjljY2QzMzNhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/f/f6/14ylf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'O Homem Bicentenário',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTU4Nzg5YmItNzE0Yy00Y2VmLWI3OTYtNTFjODEzMDE0YTI4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/Cs2XFHWbv248RjCYAMYa_Pl0SFk14EaSMXEBZRT7246E0hlsK4UfaUSXkC4Bbmwom6m68hF11AUEBU_snLpO-PJM0g3WFUKh=m18',
                       'genre': 'Filmes'},

                       {'name': 'O Paizao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjAzNzQ4YzEtZWFlOS00YWVkLWE2NDctZDBiZTUxYjgwOTYzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/v6/q1zlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Paizao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjAzNzQ4YzEtZWFlOS00YWVkLWE2NDctZDBiZTUxYjgwOTYzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/v6/q1zlf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'O SEXTO SENTIDO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMWM4NTFhYjctNzUyNi00NGMwLTk3NTYtMDIyNTZmMzRlYmQyXkEyXkFqcGdeQXVyMTAwMzUyOTc@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/STkt_ehgFfhjPJ6kv04S5Ly4Pk1v-eVfPOrmKiUhiRs4zf9oSJuYzukT4ZWsVUk47zil8VFe=m22',
                       'genre': 'Filmes'},

                       {'name': 'O Suspeito Da Rua Arlington',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODAwZGM4OWYtM2FhMy00MGIwLTgyMmMtNzRlOTcyYTFkMjVlXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/x/56/4v1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Segundas Intenções',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMxNjM5OTQ2M15BMl5BanBnXkFtZTgwNjUxNzYxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/l/96/5z1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Segundas Intencoes 3',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMxNjM5OTQ2M15BMl5BanBnXkFtZTgwNjUxNzYxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/5/16/qp1lf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Segundas Intencoes 3',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMxNjM5OTQ2M15BMl5BanBnXkFtZTgwNjUxNzYxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/5/16/qp1lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Segundas Intencoes 3',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMxNjM5OTQ2M15BMl5BanBnXkFtZTgwNjUxNzYxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/5/16/qp1lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Shut Eye',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5NTUwNjI1N15BMl5BanBnXkFtZTYwOTE1ODc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=96ea0f76d6572c5d',
                       'genre': 'Shut Eye LEG'},

                       {'name': 'Shut Eye',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5NTUwNjI1N15BMl5BanBnXkFtZTYwOTE1ODc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=77acaa2423175eb0',
                       'genre': 'Shut Eye LEG'},

                       {'name': 'Shut Eye',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5NTUwNjI1N15BMl5BanBnXkFtZTYwOTE1ODc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=beaff6b0f8ba931e',
                       'genre': 'Shut Eye LEG'},

                       {'name': 'Shut Eye',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5NTUwNjI1N15BMl5BanBnXkFtZTYwOTE1ODc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=8456725b769e153c',
                       'genre': 'Shut Eye LEG'},

                       {'name': 'Shut Eye',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5NTUwNjI1N15BMl5BanBnXkFtZTYwOTE1ODc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=97f04d745da5f3d8',
                       'genre': 'Shut Eye LEG'},

                       {'name': 'Shut Eye',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5NTUwNjI1N15BMl5BanBnXkFtZTYwOTE1ODc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=3f9ba6adc73d30e6',
                       'genre': 'Shut Eye LEG'},

                       {'name': 'Shut Eye',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5NTUwNjI1N15BMl5BanBnXkFtZTYwOTE1ODc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=c7061f11d64053',
                       'genre': 'Shut Eye LEG'},

                       {'name': 'Shut Eye',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5NTUwNjI1N15BMl5BanBnXkFtZTYwOTE1ODc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=7cda0e32c2d89c86',
                       'genre': 'Shut Eye LEG'},

                       {'name': 'Shut Eye',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5NTUwNjI1N15BMl5BanBnXkFtZTYwOTE1ODc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=c2f4eb70fdb7f5c5',
                       'genre': 'Shut Eye LEG'},

                       {'name': 'Shut Eye',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjA5NTUwNjI1N15BMl5BanBnXkFtZTYwOTE1ODc5._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=edd3a69908a57a2e',
                       'genre': 'Shut Eye LEG'},

                       {'name': 'Stigmata',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjEyNWUyZTYtMTViZC00Y2ZkLWE2ZDEtNGY2ZDAxNjY2YjYzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/v6/j1zlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Stigmata',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjEyNWUyZTYtMTViZC00Y2ZkLWE2ZDEtNGY2ZDAxNjY2YjYzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/v6/j1zlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Stigmata',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjEyNWUyZTYtMTViZC00Y2ZkLWE2ZDEtNGY2ZDAxNjY2YjYzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/v6/j1zlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'THE BONE COLLECTOR',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOWQxN2ZmNDMtMzA2Ny00ZDJhLTlkNTgtMWMyZjljY2QzMzNhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/thebone1.mp4',
                       'genre': ''},

                       {'name': 'tvg-logo=http://amofilmes.net/wp-content/uploads/Segundas_Intencoes_3_DVDRIP_Xvid_Dublado.jpg,Segundas Intencoes 3',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjMxNjM5OTQ2M15BMl5BanBnXkFtZTgwNjUxNzYxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/5/16/qp1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://br.web.img2.acsta.net/medias/nmedia/18/87/25/20/19873566.jpg,Vamos Nessa',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzJhNGExMDYtMWEyOS00MzMxLWJiYTYtMDYxNTRmNjdjM2VlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/n6/69ulf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/j/l6/ydwlf_tnl_2 8.jpg?ts=20140407063858,A Informante',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODg0YjAzNDQtOGFkMi00Yzk2LTg1NzYtYTNjY2UwZTM2ZDdkL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR2,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/j/l6/ydwlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/z/km/f7eyb_tnl_2 8.jpg?ts=20140414192627,Stigmata',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjEyNWUyZTYtMTViZC00Y2ZkLWE2ZDEtNGY2ZDAxNjY2YjYzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/v6/j1zlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://upload.wikimedia.org/wikipedia/pt/thumb/e/ee/Existenz.jpg/200px-Existenz.jpg,eXistenZ',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmU1MTJkYWItMzM5Ny00NDgxLTgxOGEtNTkzNDdkZjkwNGI0XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UY268_CR2,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/d6/m3vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Um Tira Muito Suspeito',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTJkYTBlZjktYmYyYi00ZWQ0LTgyMWYtMjQ5Yzg1Y2M3YzE5XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/f/h6/75vlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Um Tira Muito Suspeito',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTJkYTBlZjktYmYyYi00ZWQ0LTgyMWYtMjQ5Yzg1Y2M3YzE5XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/f/h6/75vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Vamos Nessa',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzJhNGExMDYtMWEyOS00MzMxLWJiYTYtMDYxNTRmNjdjM2VlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/n6/69ulf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Vamos Nessa',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzJhNGExMDYtMWEyOS00MzMxLWJiYTYtMDYxNTRmNjdjM2VlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/n6/69ulf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Vamos Nessa',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzJhNGExMDYtMWEyOS00MzMxLWJiYTYtMDYxNTRmNjdjM2VlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/n6/69ulf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': ',O Oposto do Sexo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTA3NTQ1MmUtZTI0NS00MWFjLTlkZmYtY2Y4MzMxMzI5MDE0XkEyXkFqcGdeQXVyMjM5ODMxODc@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/e/l6/gdwlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'A NIGHT AT ROXBURY',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYTczZmEyYWMtMTE5MC00YzcyLWJhMDAtZDA5Mzg2YmQwNWQyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/roxbury.mp4',
                       'genre': ''},

                       {'name': 'Amor Além da Vida',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTg5ZWRjNTctNmMyMi00NTJmLTg3YjktMzJlMDRiYWQ0MjMzL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/r6xQ5g9_5qnUhAUOz_gB6-yBJm_r4YMA6GnbJHmQDl6R8KPw4sc5j5RGSA03ITVXpAYPyRbNajnuGtqUhcixJCWMjNku33bC=m18',
                       'genre': 'Filmes'},

                       {'name': 'CRIME PERFEITO',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTcwODQxNTEyN15BMl5BanBnXkFtZTYwNTE3NzI3._V1_UY268_CR4,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/8kO3DGYb3iqkWyxMrDcn_gIGxlKPs5kY0Nx0F4nxuniEfVEGua4N-S5qlcs2G0fWBoERezIG9Jk7_w=m22',
                       'genre': 'Filmes'},

                       {'name': 'Garotas Selvagens 3',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODMyYTlkNWYtODAzMC00ZjFiLWE3YjctMGUyMzM1MDk3ZDFlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/o/z6/lrvlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Garotas Selvagens 4',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODMyYTlkNWYtODAzMC00ZjFiLWE3YjctMGUyMzM1MDk3ZDFlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/16/9o1lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Garotas Selvagens 4',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODMyYTlkNWYtODAzMC00ZjFiLWE3YjctMGUyMzM1MDk3ZDFlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/16/9o1lf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Garotas Selvagens 4',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODMyYTlkNWYtODAzMC00ZjFiLWE3YjctMGUyMzM1MDk3ZDFlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/16/9o1lf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'Jogos, Trapaças e Dois Canos Fumegantes',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAyN2JmZmEtNjAyMy00NzYwLThmY2MtYWQ3OGNhNjExMmM4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/n/um/rbeyb_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Jogos, Trapaças e Dois Canos Fumegantes',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAyN2JmZmEtNjAyMy00NzYwLThmY2MtYWQ3OGNhNjExMmM4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/n/um/rbeyb_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Jogos, Trapaças e Dois Canos Fumegantes',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAyN2JmZmEtNjAyMy00NzYwLThmY2MtYWQ3OGNhNjExMmM4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/n/um/rbeyb_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Jogos, Trapacas E Dois Canos Fumegantes',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTAyN2JmZmEtNjAyMy00NzYwLThmY2MtYWQ3OGNhNjExMmM4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/n/um/rbeyb_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'Mal Posso Esperar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGY5NDIwNWMtN2IxZC00ODYxLWI1ZjgtOTQ4ZjhlYzMyZGEyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/v/96/a41lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Mal Posso Esperar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGY5NDIwNWMtN2IxZC00ODYxLWI1ZjgtOTQ4ZjhlYzMyZGEyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/v/96/a41lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'O Oposto do Sexo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTA3NTQ1MmUtZTI0NS00MWFjLTlkZmYtY2Y4MzMxMzI5MDE0XkEyXkFqcGdeQXVyMjM5ODMxODc@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/e/l6/gdwlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Oposto do Sexo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTA3NTQ1MmUtZTI0NS00MWFjLTlkZmYtY2Y4MzMxMzI5MDE0XkEyXkFqcGdeQXVyMjM5ODMxODc@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/e/l6/gdwlf_480p.mp4?',
                       'genre': 'ROMANCE'},

                       {'name': 'O Oposto do Sexo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTA3NTQ1MmUtZTI0NS00MWFjLTlkZmYtY2Y4MzMxMzI5MDE0XkEyXkFqcGdeQXVyMjM5ODMxODc@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/e/l6/gdwlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'O PEQUENO GUERREIRO,01',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=8cfc0d88f587636c',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,02',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=8ef4d8233e6545ca',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,03',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=14daeb159f1e3945',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,04',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=81528d7447fdb2e8',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,05',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=7fd914bed68b9ea6',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,06',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=6792862fea2aeb20',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,07',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=aed2ad0bca23a89f',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,08',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=529372fdaeca7668',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,09',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=4f9fb3cf22abbbef',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,10',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=aac90c62673bdf62',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,11',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=2ff889247679345a',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,12',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=bd5ac76413ed26a1',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,13',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=d66f15caa55c580a',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,14',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=63011396806a12bf',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,15',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=99ed52b6b80fdf92',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,16',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=3a518257df6fb37e',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,17',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=7ae86853c081bbc5',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,18',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=5db69a507bb01c38',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,19',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=58f5c69cb1aa9589',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,20',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=b7e535f7e459bf74',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,21',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=ea6f5af7a7722f3b',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,22',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=b8a8e84ec7fd00c6',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,23',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=9c546aae2782a427',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,24',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=8c0d150727d4451d',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,25',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=1ef759eee7088592',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,26',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=61e05c64cc191eb8',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,27',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=517eb1320affe4f9',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,28',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=e6f754d27b367d66',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,29',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=96c4b11c4d269cd6',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,30',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=7e15277809c3a10f',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,31',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=4ee77361df031e79',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,32',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=2fb50c99fb5a71f9',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,33',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=fa829314b3a7fbf0',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,34',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=8f35e9e012ebd886',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,36',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=2ddfaeb137120242',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,37',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=8a3a9988bcb26367',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,38',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=c7ef936c6d39b0f4',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,39',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=7e5182c8408d9c33',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,40',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=5771fb96e8e43b1d',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,41',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=7c6ce3cada9d983b',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,42',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=fad341d19fa3131c',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,43',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=1b59fee673f89923',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,44',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=e7910b8c1f9665dc',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,45',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=195f74c200035fb5',
                       'genre': ''},

                       {'name': 'O PEQUENO GUERREIRO,46',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNzhiZmZkYjQtMTFlZi00YmQ2LTg5NGEtM2M4ZTg4ZjAyNzI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR7,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=7c1bf766a6e053bf',
                       'genre': ''},

                       {'name': 'RED LINE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjEzMTM2NjAtNWFmZC00MTVlLTgyMmQtMGQyNTFjZDk5N2NmXkEyXkFqcGdeQXVyNzQ1ODk3MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://iptvperu@media-es-am.crackle.com/1/l/h0/jlmyk_480p_1mbps.mp4?',
                       'genre': ''},

                       {'name': 'The Thin Red Line',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjEzMTM2NjAtNWFmZC00MTVlLTgyMmQtMGQyNTFjZDk5N2NmXkEyXkFqcGdeQXVyNzQ1ODk3MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.youtube.com/watch?v=OvZUsKJ9e_k',
                       'genre': 'Filmes'},

                       {'name': 'THE WEDDING SINGER',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjM5YTQ0ZGYtMWExZi00MTFmLTg0YjUtZDcyMGNiYzE5MmNmL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/wedding1998.mp4',
                       'genre': ''},

                       {'name': 'tvg-logo=http://br.web.img1.acsta.net/pictures/14/03/19/20/14/334055.jpg,Garotas Selvagens 4',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BODMyYTlkNWYtODAzMC00ZjFiLWE3YjctMGUyMzM1MDk3ZDFlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/1/16/9o1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/v/96/a41lf_tnl_2 8.jpg?ts=20141222175917,Mal Posso Esperar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGY5NDIwNWMtN2IxZC00ODYxLWI1ZjgtOTQ4ZjhlYzMyZGEyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/v/96/a41lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',O Principal Suspeito',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWQyNzdhNTQtZjUzYS00Yzk2LTk3OTEtYzhkYjc4YzJiMGYyXkEyXkFqcGdeQXVyNjU0NTI0Nw@@._V1_UY268_CR11,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/h6/z7vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Advogado do Diabo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BM2M2MDJhMDgtMmJkYy00MTgzLTkyZTktODM5NzE1MWUyNDA4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://network.vstreaming.net/movies/advogadododiabo-dub-720p.mp4',
                       'genre': ''},

                       {'name': 'Amigo de Casa',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzRiMGE2MmMtM2RhMy00OWNiLTljYTktOThmMmE1YjY1NjYyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/z6/ksvlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Gattaca a Experiencia Genetica',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDQxOTc0MzMtZmRlOS00OWQ5LWI2ZDctOTAwNmMwOTYxYzlhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/z6/yuvlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Homens Perigosos',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmExY2QyMDYtZjc1NC00YzRmLWJlYzUtODY1MzA2OTliNmE1XkEyXkFqcGdeQXVyMTMxMTY0OTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/b/h6/o8vlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Homens Perigosos',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmExY2QyMDYtZjc1NC00YzRmLWJlYzUtODY1MzA2OTliNmE1XkEyXkFqcGdeQXVyMTMxMTY0OTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/b/h6/o8vlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Homens Perigosos',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmExY2QyMDYtZjc1NC00YzRmLWJlYzUtODY1MzA2OTliNmE1XkEyXkFqcGdeQXVyMTMxMTY0OTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/b/h6/o8vlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Inimigo Íntimo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYzMDA1OTc4OF5BMl5BanBnXkFtZTgwODc2MzkyMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/n/z6/irvlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'O Principal Suspeito',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWQyNzdhNTQtZjUzYS00Yzk2LTk3OTEtYzhkYjc4YzJiMGYyXkEyXkFqcGdeQXVyNjU0NTI0Nw@@._V1_UY268_CR11,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/h6/z7vlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'O Principal Suspeito',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWQyNzdhNTQtZjUzYS00Yzk2LTk3OTEtYzhkYjc4YzJiMGYyXkEyXkFqcGdeQXVyNjU0NTI0Nw@@._V1_UY268_CR11,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/h6/z7vlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Principal Suspeito',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWQyNzdhNTQtZjUzYS00Yzk2LTk3OTEtYzhkYjc4YzJiMGYyXkEyXkFqcGdeQXVyNjU0NTI0Nw@@._V1_UY268_CR11,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/h6/z7vlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Red Corner',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzE0MjU5NzQxNV5BMl5BanBnXkFtZTcwMzQzNzU2NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/l/56/ur1lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Red Corner',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzE0MjU5NzQxNV5BMl5BanBnXkFtZTcwMzQzNzU2NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/l/56/ur1lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/3/sm/epfyb_tnl_2 8.jpg?ts=20140826224642,Red Corner',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzE0MjU5NzQxNV5BMl5BanBnXkFtZTcwMzQzNzU2NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/l/56/ur1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/6/8l/27cyb_tnl_2 8.jpg?ts=20130904015547,Homens Perigosos',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmExY2QyMDYtZjc1NC00YzRmLWJlYzUtODY1MzA2OTliNmE1XkEyXkFqcGdeQXVyMTMxMTY0OTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/b/h6/o8vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Jovens Bruxas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4MjQ2MzU1OV5BMl5BanBnXkFtZTgwNTM2Mjc3ODE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/f/l6/hdwlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Swingers - Curtindo a Noite',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjg1ZmViMmEtYzIxNi00MzJlLTk4MDktNTE2ZDkwMzEyMjBhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/h6/v7vlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': '.1 Queima de Arquivo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTczMTNlN2UtMWE2NS00ZTUyLTgzYTQtYTFkNWIzODJkYzIwXkEyXkFqcGdeQXVyNDc2NjEyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=99520aa12c15f946',
                       'genre': 'Burn Notice DUB'},

                       {'name': 'DONT BE A MENACE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BY2NmM2M2MWItNjdlMC00ZWI3LTkwODUtZDNkYWZjYjgzZjY3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/menace.mp4',
                       'genre': ''},

                       {'name': 'Jovens Bruxas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4MjQ2MzU1OV5BMl5BanBnXkFtZTgwNTM2Mjc3ODE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/f/l6/hdwlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Jovens Bruxas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4MjQ2MzU1OV5BMl5BanBnXkFtZTgwNTM2Mjc3ODE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/f/l6/hdwlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Jovens Bruxas',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY4MjQ2MzU1OV5BMl5BanBnXkFtZTgwNTM2Mjc3ODE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/f/l6/hdwlf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'Ligadas pelo desejo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjcwN2RhYWYtOWY1NC00M2JkLTllYWItYzZhOTg4NjZmMDcwXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.youtube.com/watch?v=OM29TpjYmr0',
                       'genre': 'Novos no [COLOR red]Cinebox![/COLOR]'},

                       {'name': 'Matilda',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZTA4MmI5YzgtOTU1Yy00NGVjLTgyMGQtNjNlMDY2YWVlZmYyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://ia601504.us.archive.org/27/items/LHMTVfilmes2/M4t.LHMTv.mp4?LHMTv',
                       'genre': 'Classicos'},

                       {'name': 'Matilda',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZTA4MmI5YzgtOTU1Yy00NGVjLTgyMGQtNjNlMDY2YWVlZmYyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://ia601504.us.archive.org/27/items/LHMTVfilmes2/M4t.LHMTv.mp4?LHMTv',
                       'genre': 'Classicos'},

                       {'name': 'Matilda',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZTA4MmI5YzgtOTU1Yy00NGVjLTgyMGQtNjNlMDY2YWVlZmYyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://dropapk.com/vidembed-sxn3hjll2a4o.mp4',
                       'genre': 'Diversos'},

                       {'name': 'O Povo contra Larry Flint',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTY3NjA3OTY2Nl5BMl5BanBnXkFtZTgwMjAyNjQxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/16/ip1lf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Swingers - Curtindo a Noite',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjg1ZmViMmEtYzIxNi00MzJlLTk4MDktNTE2ZDkwMzEyMjBhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/h6/v7vlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Swingers - Curtindo a Noite',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjg1ZmViMmEtYzIxNi00MzJlLTk4MDktNTE2ZDkwMzEyMjBhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/h6/v7vlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Swingers - Curtindo a Noite',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjg1ZmViMmEtYzIxNi00MzJlLTk4MDktNTE2ZDkwMzEyMjBhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/u/h6/v7vlf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/x/n6/oy2lf_tnl_2 8.jpg?ts=20150325003622,O Contrato',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZDI0ZmFmYTgtMTQ5OS00MTVmLTgwNWYtNzIyY2Y5NjYxNzgyXkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_UY268_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/x/n6/oy2lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Apollo 13',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjEzYjJmNzgtNDkwNy00MTQ4LTlmMWMtNzA4YjE2NjI0ZDg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/ld7AXlabXPnq3Xl4kX7XmiCgSqbqbNobyxGxQOgBcXECnT4UhrnutbamueMPgOkioHM=m18',
                       'genre': 'Filmes'},

                       {'name': 'Apollo 13',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjEzYjJmNzgtNDkwNy00MTQ4LTlmMWMtNzA4YjE2NjI0ZDg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/ld7AXlabXPnq3Xl4kX7XmiCgSqbqbNobyxGxQOgBcXECnT4UhrnutbamueMPgOkioHM=m18',
                       'genre': 'Filmes'},

                       {'name': 'APOLLO 18',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjEzYjJmNzgtNDkwNy00MTQ4LTlmMWMtNzA4YjE2NjI0ZDg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/Lmr1unP4GRBZ-bIN9JFL2Bg8Jmc6B3sdzdj3PeAoN2au2bCPRDiltYMe-4XwonOZ8paPh1cg=m22',
                       'genre': 'Filmes'},

                       {'name': 'ASSASSINOS CIBERNETICOS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BM2M2ZGM0NDUtODRhNS00MjcxLTg3ZWYtYjkyZDJkYmVjOWYwXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/AgmOT7RSIJ5B-K95NDetSsi4MFfhpVfiWLxkusH8K5-i1BBJ1o4HdDPeHYhv6Wsi63eV6hhUOl3jPw=m22',
                       'genre': 'Filmes'},

                       {'name': 'Braveheart',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzkzMmU0YTYtOWM3My00YzBmLWI0YzctOGYyNTkwMWE5MTJkXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/n77CZ_63y0jeN9na3fryqeZTiA3CvMeIGhHZ-UW_58ea7aj8_NUDN_-n0gLP4ia8EDpKjifD=m22',
                       'genre': 'Filmes'},

                       {'name': 'CoraCAo Valente',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzkzMmU0YTYtOWM3My00YzBmLWI0YzctOGYyNTkwMWE5MTJkXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/K5WZzBDc94I3zVJSr6E6mAUSZ-5DvDxdgRc4YxpAZAF6ofzGgARbh6u7vwGTCAzEhVGv_0tM7w=m18',
                       'genre': 'Filmes'},

                       {'name': 'Crimson Tide',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmFkY2IxNTAtMWRiNS00MWU2LWI1NDYtY2YxYTQyYTk5OTBhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/nyspuWa5TzE9LU1dwP5-1ubh13GV-nclKLfKv7HBa5_tXL_ySpQfJIkl_tNX4G-DTB4=m18',
                       'genre': 'Filmes'},

                       {'name': 'DANGEROUS MINDS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZjk2YjNkYTYtOTZkNy00ZmRkLWI5ODEtYzA4MTM3MzMyZjhlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/minds.mp4',
                       'genre': ''},

                       {'name': 'DEAD PRESIDENTS',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjdhZWEzMzEtMjNhZS00OThhLWFiZWUtM2EwMWU5MWE0MDA4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/deadp.mp4',
                       'genre': ''},

                       {'name': 'Gasparzinho - o Fantasminha Camarada',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZThhYTlhMDUtMDhjZi00MTljLTkwMDYtOGU3ZjVlMWE4NDk4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR5,0,182,268_AL_.jpg',
                       'video': 'http://ia601504.us.archive.org/27/items/LHMTVfilmes2/GPZ-O.f.c.LHMTv.mp4?LHMTv',
                       'genre': 'Classicos'},

                       {'name': 'Hackers - Piratas de Computador',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNmExMTkyYjItZTg0YS00NWYzLTkwMjItZWJiOWQ2M2ZkYjE4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/16/1o1lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'HACKERS - PIRATAS DE COMPUTADOR',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNmExMTkyYjItZTg0YS00NWYzLTkwMjItZWJiOWQ2M2ZkYjE4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/WvCWHoYtJbfhXrfxlH6l1u9TGs9pCCp_yK6oHY_CFUDMHUf4Uib9LfiUyFEyJ-PH2FMeKL-rH26X9A=m22',
                       'genre': 'Filmes'},

                       {'name': 'Hackers - Piratas de Computador',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNmExMTkyYjItZTg0YS00NWYzLTkwMjItZWJiOWQ2M2ZkYjE4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/16/1o1lf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Hackers - Piratas de Computador',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNmExMTkyYjItZTg0YS00NWYzLTkwMjItZWJiOWQ2M2ZkYjE4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/16/1o1lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'KICKING AND SCREAMING',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNWU2YjdlN2ItNTk2OS00MzMwLTlhYjctNDI0MDI0NTQ3OWY0XkEyXkFqcGdeQXVyNzI1NzMxNzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/kicking.mp4',
                       'genre': ''},

                       {'name': 'Mar?ermelha',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmFkY2IxNTAtMWRiNS00MWU2LWI1NDYtY2YxYTQyYTk5OTBhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/nyspuWa5TzE9LU1dwP5-1ubh13GV-nclKLfKv7HBa5_tXL_ySpQfJIkl_tNX4G-DTB4=m18',
                       'genre': 'Filmes'},

                       {'name': 'Rápida E Mortal',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BOTI2ZTZmMmItMmM3YS00ZjUwLWJiODMtMmRjMWM4NDE0OWFhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/96/s01lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/x/om/gefyb_tnl_2 8.jpg?ts=20140613195929,Hackers - Piratas de Computador',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNmExMTkyYjItZTg0YS00NWYzLTkwMjItZWJiOWQ2M2ZkYjE4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/z/16/1o1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'ÚLTIMOS PASSOS DE UM HOMEM',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTM3NzA1MjM2N15BMl5BanBnXkFtZTcwMzY3MTMzNA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.googleapis.com/drive/v3/files/0B_JatFT_TpCKUWwxb2V5QlRYQ00?key=AIzaSyAHfTjunuAnmyVgGADZo4HD4XN2YAO0MnQ&alt=media',
                       'genre': 'Filmes'},

                       {'name': ',Atraidos Pelo Destino',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYzMxOGUzOWEtMGUxMi00ZWM1LWE3ODgtNzc4OGVjZmJhMmFmXkEyXkFqcGdeQXVyODY0NzcxNw@@._V1_UY268_CR9,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/e/l6/edwlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Adoraveis Mulheres',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNmEyODc3MzctM2RiYS00N2MwLTk5MjktYmExYjkwYTU4YjhmXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/f6/s7ylf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Adoraveis Mulheres',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNmEyODc3MzctM2RiYS00N2MwLTk5MjktYmExYjkwYTU4YjhmXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/f6/s7ylf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Adoraveis Mulheres',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNmEyODc3MzctM2RiYS00N2MwLTk5MjktYmExYjkwYTU4YjhmXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/f6/s7ylf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Atraidos Pelo Destino',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYzMxOGUzOWEtMGUxMi00ZWM1LWE3ODgtNzc4OGVjZmJhMmFmXkEyXkFqcGdeQXVyODY0NzcxNw@@._V1_UY268_CR9,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/e/l6/edwlf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'Atraidos Pelo Destino',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYzMxOGUzOWEtMGUxMi00ZWM1LWE3ODgtNzc4OGVjZmJhMmFmXkEyXkFqcGdeQXVyODY0NzcxNw@@._V1_UY268_CR9,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/e/l6/edwlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Atraidos Pelo Destino',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYzMxOGUzOWEtMGUxMi00ZWM1LWE3ODgtNzc4OGVjZmJhMmFmXkEyXkFqcGdeQXVyODY0NzcxNw@@._V1_UY268_CR9,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/e/l6/edwlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Born To Kill',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI2NTU2Nzc0MV5BMl5BanBnXkFtZTcwMzY1OTM2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d08a722616b74598',
                       'genre': 'Born To Kill DUB'},

                       {'name': 'Born To Kill',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI2NTU2Nzc0MV5BMl5BanBnXkFtZTcwMzY1OTM2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=90d9a92974bfc0d3',
                       'genre': 'Born To Kill LEG'},

                       {'name': 'Born To Kill',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI2NTU2Nzc0MV5BMl5BanBnXkFtZTcwMzY1OTM2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=8c90832c8fd40447',
                       'genre': 'Born To Kill LEG'},

                       {'name': 'Born To Kill',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTI2NTU2Nzc0MV5BMl5BanBnXkFtZTcwMzY1OTM2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=e3af78874c6e55dd',
                       'genre': 'Born To Kill LEG'},

                       {'name': 'Lendas da Paixao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYwMjYxNTAyN15BMl5BanBnXkFtZTgwMTc3MjkyMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/8/l6/ujwlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Lendas da Paixao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYwMjYxNTAyN15BMl5BanBnXkFtZTgwMTc3MjkyMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/8/l6/ujwlf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Lendas da Paixao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYwMjYxNTAyN15BMl5BanBnXkFtZTgwMTc3MjkyMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/8/l6/ujwlf_480p.mp4?',
                       'genre': 'ROMANCE'},

                       {'name': 'Meu Papai é Noel',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTZlNzk1MjItYjJlYy00MTAxLWJkNjEtZmNiNmVlNjQ4NDE5XkEyXkFqcGdeQXVyMzI0NDc4ODY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/ADpgBNio1vp7jVn4nC2qoimt4o_g1hhAfU0-DlWKm3A-vquVpH7YRrJ_gzRHpPVFktPelPL6fw=m18',
                       'genre': 'Filmes'},

                       {'name': 'STARGATE 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYWEyYTQzNzQtZTg5OS00NDhkLTg1NjYtMzA5Y2MyYjYzNWQ5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/X28YLj3fIom_Cz1LvAU7KUo3n179gvAAf9cuxDfMp--Lrlp9WFM64gzLCC5aWBcIM_82_5ky=m22',
                       'genre': 'Filmes'},

                       {'name': 'The Last Seduction',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZmYwYWRhY2MtNTU3NS00M2E0LWI5YjUtY2M1NGJkM2Y4NTdmXkEyXkFqcGdeQXVyNjU0NTI0Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.youtube.com/watch?v=KhHuFGpgzOY',
                       'genre': 'Filmes'},

                       {'name': 'Tres Formas de Amar',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BM2E1MjU5ZmUtYzJkMC00NDM2LTk1MjctMGY3ZGU4ZGNkNWFiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/p/h6/b7vlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/3/f6/s7ylf_tnl_2 8.jpg?ts=20140407230223,Adoraveis Mulheres',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNmEyODc3MzctM2RiYS00N2MwLTk5MjktYmExYjkwYTU4YjhmXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/f6/s7ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-am.crackle.com/1/8/l6/ujwlf_tnl_2 8.jpg?ts=20140407115042,Lendas da Paixao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTYwMjYxNTAyN15BMl5BanBnXkFtZTgwMTc3MjkyMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/8/l6/ujwlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Um Sonho de Liberdade',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/PttWqpC4SIb67kGC4UUL61R0JR0Jqde-F8Pr-Iu7Qu-KzZzUCFWhhe3gwkgp3gaozK0=m18',
                       'genre': 'Filmes'},

                       {'name': 'Um Sonho de Liberdade',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://lh3.googleusercontent.com/PttWqpC4SIb67kGC4UUL61R0JR0Jqde-F8Pr-Iu7Qu-KzZzUCFWhhe3gwkgp3gaozK0=m18',
                       'genre': 'Filmes'},

                       {'name': ',Kalifornia - Uma Viagem ao Inferno',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDE2ODZhYzUtMTBhYi00ODgxLWJlNTAtODljN2Q2NDhjZmVhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/v6/lkvlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Uma Noiva e Tanto',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjU0YzdhNjYtNzdlZi00ZDIwLWIzNWUtOWE2NmVjOGI2ZThiXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/c/n6/96ulf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Feitico do Tempo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWIxNzM5YzQtY2FmMS00Yjc3LWI1ZjUtNGVjMjMzZTIxZTIxXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/d/f6/t4ylf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Feitico do Tempo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWIxNzM5YzQtY2FmMS00Yjc3LWI1ZjUtNGVjMjMzZTIxZTIxXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/d/f6/t4ylf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Feitiço do Tempo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZWIxNzM5YzQtY2FmMS00Yjc3LWI1ZjUtNGVjMjMzZTIxZTIxXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/d/f6/t4ylf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Kalifornia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDE2ODZhYzUtMTBhYi00ODgxLWJlNTAtODljN2Q2NDhjZmVhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/v6/lkvlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Kalifornia - Uma Viagem ao Inferno',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDE2ODZhYzUtMTBhYi00ODgxLWJlNTAtODljN2Q2NDhjZmVhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/v6/lkvlf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Kalifornia - Uma Viagem ao Inferno',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDE2ODZhYzUtMTBhYi00ODgxLWJlNTAtODljN2Q2NDhjZmVhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/v6/lkvlf_480p.mp4?',
                       'genre': 'TERROR'},

                       {'name': 'Kalifornia - Uma Viagem ao Inferno',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDE2ODZhYzUtMTBhYi00ODgxLWJlNTAtODljN2Q2NDhjZmVhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/v6/lkvlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'MENACE II SOCIETY',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTFlMDg2MGEtODk2My00MGNhLThkMDAtY2Y5OWNlM2FkNjQ1XkEyXkFqcGdeQXVyNTI4MjkwNjA@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/menace2.mp4',
                       'genre': ''},

                       {'name': 'MRS DOUBTFIRE',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjExMDUzODE1N15BMl5BanBnXkFtZTgwNTU5NTYxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/doubtfire.mp4',
                       'genre': ''},

                       {'name': 'O Sangue de Romeo',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNTY1OTA1ZDEtNzVmNi00MWEwLWJlYjItM2UyZDhmNmZiZDE2L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNDkzNTM2ODg@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/v6/hkvlf_480p.mp4?',
                       'genre': 'ROMANCE'},

                       {'name': 'O Ultimo Grande Heroi',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjdhOGY1OTktYWJkZC00OGY5LWJhY2QtZmQzZDA2MzY5MmNmXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/n6/s9ulf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'O Ultimo Grande Heroi',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjdhOGY1OTktYWJkZC00OGY5LWJhY2QtZmQzZDA2MzY5MmNmXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/n6/s9ulf_480p.mp4?',
                       'genre': 'ACAO'},

                       {'name': 'Rudy',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGUzMDU1YmQtMzBkOS00MTNmLTg5ZDQtZjY5Njk4Njk2MmRlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_UY268_CR5,0,182,268_AL_.jpg',
                       'video': 'https://lh3.googleusercontent.com/OMQZxAQrbytTPFOIYmIsSd2hv4tW5fnOOFRgx0-2l4jAkvfsjjbaEXyil4h6zs8kJA2wGUNINTxE5m9l=m22',
                       'genre': 'Filmes'},

                       {'name': 'Seis Graus de Separacao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ5ODk1NTI4NV5BMl5BanBnXkFtZTcwNDYzMjI3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/_/h6/scwlf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Seis Graus de Separacao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ5ODk1NTI4NV5BMl5BanBnXkFtZTcwNDYzMjI3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/_/h6/scwlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://eovideolevou.com.br/imgProduto/70303_f1.jpg,Seis Graus de Separacao',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTQ5ODk1NTI4NV5BMl5BanBnXkFtZTcwNDYzMjI3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/_/h6/scwlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'tvg-logo=http://images-br-az.crackle.com/profiles/channels/100000114/BrowserPanelChannelBackground_300x169.jpg?ts=20121026110620,O Ultimo Grande Heroi',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjdhOGY1OTktYWJkZC00OGY5LWJhY2QtZmQzZDA2MzY5MmNmXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/n6/s9ulf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Uma Noiva e Tanto',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjU0YzdhNjYtNzdlZi00ZDIwLWIzNWUtOWE2NmVjOGI2ZThiXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/c/n6/96ulf_480p_1mbps.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Uma Noiva e Tanto',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjU0YzdhNjYtNzdlZi00ZDIwLWIzNWUtOWE2NmVjOGI2ZThiXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/c/n6/96ulf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Uma Noiva e Tanto',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjU0YzdhNjYtNzdlZi00ZDIwLWIzNWUtOWE2NmVjOGI2ZThiXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/c/n6/96ulf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'Vestigios do Dia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDYwOThlMDAtYWUwMS00MjY5LTliMGUtZWFiYTA5MjYwZDAyXkEyXkFqcGdeQXVyNjY1NTQ0NDg@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/96/b41lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Vestígios do Dia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDYwOThlMDAtYWUwMS00MjY5LTliMGUtZWFiYTA5MjYwZDAyXkEyXkFqcGdeQXVyNjY1NTQ0NDg@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/96/b41lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'Vestígios do Dia',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNDYwOThlMDAtYWUwMS00MjY5LTliMGUtZWFiYTA5MjYwZDAyXkEyXkFqcGdeQXVyNjY1NTQ0NDg@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/w/96/b41lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': ',Codigo de Honra',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZTJkMDFkYzgtMTFkYS00MDFhLTljNzEtNTAzN2Y2ZjBkYTE1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/16/kp1lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': ',Mulher Solteira Procura',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjNmMTNjYzEtNGIzOC00ZDc2LWFjN2UtZTNmZjgxZDJkNzBlXkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/r6/2gvlf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': '.1 Twin Peaks',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzc5ODcyNTYtMDAwNy00MDhjLWFmOWUtNGVhMDRlYjE1YzNjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=eec20d95a1e060f7',
                       'genre': 'Twin Peaks LEG'},

                       {'name': '.1 Twin Peaks',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzc5ODcyNTYtMDAwNy00MDhjLWFmOWUtNGVhMDRlYjE1YzNjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=e288155d20a4041b',
                       'genre': 'Twin Peaks LEG'},

                       {'name': '.2 Twin Peaks',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzc5ODcyNTYtMDAwNy00MDhjLWFmOWUtNGVhMDRlYjE1YzNjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=f2f312d1e884eaa1',
                       'genre': 'Twin Peaks LEG'},

                       {'name': '.2 Twin Peaks',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzc5ODcyNTYtMDAwNy00MDhjLWFmOWUtNGVhMDRlYjE1YzNjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=2b9151b319c83571',
                       'genre': 'Twin Peaks LEG'},

                       {'name': '1 Twin Peaks',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzc5ODcyNTYtMDAwNy00MDhjLWFmOWUtNGVhMDRlYjE1YzNjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=75c6421faf9df746',
                       'genre': 'Twin Peaks LEG'},

                       {'name': '2 Twin Peaks',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzc5ODcyNTYtMDAwNy00MDhjLWFmOWUtNGVhMDRlYjE1YzNjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=fe492e693d6f66a5',
                       'genre': 'Twin Peaks LEG'},

                       {'name': 'CLASS ACT',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMjc1ZjdlMTQtMDA5MS00NGQzLWIzM2ItOTViNTlkOGVlODAzXkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/classact.mp4',
                       'genre': ''},

                       {'name': 'Codigo de Honra',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZTJkMDFkYzgtMTFkYS00MDFhLTljNzEtNTAzN2Y2ZjBkYTE1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/16/kp1lf_480p.mp4?',
                       'genre': 'DRAMA'},

                       {'name': 'Codigo de Honra',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZTJkMDFkYzgtMTFkYS00MDFhLTljNzEtNTAzN2Y2ZjBkYTE1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/16/kp1lf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Codigo de Honra',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZTJkMDFkYzgtMTFkYS00MDFhLTljNzEtNTAzN2Y2ZjBkYTE1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/3/16/kp1lf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Mulher Solteira Procura',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjNmMTNjYzEtNGIzOC00ZDc2LWFjN2UtZTNmZjgxZDJkNzBlXkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/r6/2gvlf_480p.mp4?STANIPTV',
                       'genre': 'Filmes'},

                       {'name': 'Mulher Solteira Procura',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjNmMTNjYzEtNGIzOC00ZDc2LWFjN2UtZTNmZjgxZDJkNzBlXkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/y/r6/2gvlf_480p.mp4?',
                       'genre': 'COMEDIA'},

                       {'name': 'O Mariachi',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BNjMwNzA1NmQtYjUyYS00MTNlLWJiNDktODM3YTFlZDA0ZWUxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/q/96/n01lf_480p.mp4',
                       'genre': 'Filmes'},

                       {'name': 'P-1 Twin Peaks Fire Walk with Me',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzc5ODcyNTYtMDAwNy00MDhjLWFmOWUtNGVhMDRlYjE1YzNjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=31dc7824d6fb9897',
                       'genre': 'Twin Peaks LEG'},

                       {'name': 'P-2 Twin Peaks Fire Walk with Me',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMzc5ODcyNTYtMDAwNy00MDhjLWFmOWUtNGVhMDRlYjE1YzNjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=fdc294c52885fe16',
                       'genre': 'Twin Peaks LEG'},

                       {'name': 'Pure',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGZjNTM3YTUtNzg3MS00NTc4LThkN2ItMzEzOTNhZDljYTA1XkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=a8105aadd3ec0bb9',
                       'genre': 'Pure LEG'},

                       {'name': 'Pure',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGZjNTM3YTUtNzg3MS00NTc4LThkN2ItMzEzOTNhZDljYTA1XkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=bfc0f910e69c2b22',
                       'genre': 'Pure LEG'},

                       {'name': 'Pure',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGZjNTM3YTUtNzg3MS00NTc4LThkN2ItMzEzOTNhZDljYTA1XkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=3ee611b133bfb219',
                       'genre': 'Pure LEG'},

                       {'name': 'Pure',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGZjNTM3YTUtNzg3MS00NTc4LThkN2ItMzEzOTNhZDljYTA1XkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=b9276fd1ce0444f0',
                       'genre': 'Pure LEG'},

                       {'name': 'Pure',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGZjNTM3YTUtNzg3MS00NTc4LThkN2ItMzEzOTNhZDljYTA1XkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=a1949597eb277b26',
                       'genre': 'Pure LEG'},

                       {'name': 'Pure',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BZGZjNTM3YTUtNzg3MS00NTc4LThkN2ItMzEzOTNhZDljYTA1XkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=ba1f7f42d865f807',
                       'genre': 'Pure LEG'},

                       {'name': 'ROMPER STOMPER',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMTIxNjgxNDA4MV5BMl5BanBnXkFtZTcwNTY4NDEzMQ@@._V1_UY268_CR3,0,182,268_AL_.jpg',
                       'video': 'http://www.deadlyblogger.com/NewRelease/romper.mp4',
                       'genre': ''},

                       {'name': 'Solteira Procura 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjNmMTNjYzEtNGIzOC00ZDc2LWFjN2UtZTNmZjgxZDJkNzBlXkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/n6/05ulf_480p.mp4?LHMTv',
                       'genre': 'Filmes'},

                       {'name': 'Solteira Procura 2',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BYjNmMTNjYzEtNGIzOC00ZDc2LWFjN2UtZTNmZjgxZDJkNzBlXkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_UY268_CR1,0,182,268_AL_.jpg',
                       'video': 'http://media-br-am.crackle.com/1/r/n6/05ulf_480p.mp4?',
                       'genre': 'TERROR'} ]}
                       
def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
