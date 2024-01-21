from random import choice

# create list of teams
teams = [   ['Eka', 'Ega', 'Eki'],
            ['Ihsan', 'Aang', 'Tedi'],
            ['Dwipa', 'Alif', 'Hadi'],
            ['Hirlan', 'Raihan', 'Risman']
        ]
total_team = len(teams)

# # print a random name from teams
# print(f'Kelompok yang terpilih hari ini iadalah {choice(teams)}')

#  input member name
nama = input('Masukkan nama: ')
ada = True
# print(total_team)

#  loop and find matching team
for i in range(0,total_team) :
    if nama == teams[i][0] or nama == teams[i][1] or nama == teams[i][2] :
        print(f'{nama} adalah bagian dari tim {teams[i]}')
        break
    else :
        print(f'Nama {nama} tidak ada di dalam list!')
