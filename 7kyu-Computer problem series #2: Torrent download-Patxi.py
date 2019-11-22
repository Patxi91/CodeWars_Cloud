def torrent(files):
    max = 0
    time = []
    for x in range(len(files)):
          temp = files[x]
          time_temp = (temp['size_GB']*1000*8)/temp['speed_Mbps']
          time.append( time_temp )
    time_s = sorted(time)
    max = time_s[len(time_s)-1]
    ordered = []
    count = 0
    print(len(files), files)
    print(time_s)
    for x in range(len(files)):
          sub_list = []
          print(count)
          if count > 1: #Jump as many repeated time_s
              count -= 1
              if count == 1:
                  count = 0
              continue
          elif ( x < len(files)-1 and time_s[x] == time_s[x+1] ): # Until second-to-last check if time_s elements repeat
              for y in range(len(files)):
                  temp = files[y]
                  if time_s[x] == (temp['size_GB']*1000*8)/temp['speed_Mbps']:
                      count +=1
                      sub_list.append(temp['name'])
              sub_list.sort()
              ordered.extend(sub_list)
          elif ( x == len(files)-1 and time_s[x] != time_s[x-1]): #Last time_s element
              for y in range(len(files)):
                  temp = files[y]
                  if time_s[x] == (temp['size_GB']*1000*8)/temp['speed_Mbps']:
                      ordered.append(temp['name'])
          else : # Regular not repeated times
              for y in range(len(files)):
                  temp = files[y]
                  if time_s[x] == (temp['size_GB']*1000*8)/temp['speed_Mbps']:
                      ordered.append(temp['name'])
    return (ordered, max)
