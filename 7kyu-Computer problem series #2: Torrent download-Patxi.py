def torrent(files):
    print(len(files), files)
    max = 0
    time = []
    for x in range(len(files)):
          temp = files[x]
          time_temp = int((temp['size_GB']*1000*8)/temp['speed_Mbps'])
          time.append( time_temp )
    time_s = sorted(time)
    max = time_s[len(time_s)-1]
    ordered = []
    count = 0
    for x in range(len(files)):
          sub_list = []
          if count > 0: #Jump as many repeated time_s
              count -= 1
          elif ( x < len(files)-1 and time_s[x] == time_s[x+1] ): # Until second-to-last check if time_s elements repeat
              for y in range(len(files)):
                  temp = files[y]
                  if time_s[x] == int((temp['size_GB']*1000*8)/temp['speed_Mbps']):
                      count +=1
                      sub_list.append(temp['name'])
              sub_list.sort()
              ordered.extend(sub_list)
          elif ( x == len(files) and time_s[x] != time_s[x-1]): #Last time_s element
              for y in range(len(files)):
                  temp = files[y]
                  if time_s[x] == int((temp['size_GB']*1000*8)/temp['speed_Mbps']):
                      ordered.append(temp['name'])
          else : # Regular not repeated times
              for y in range(len(files)):
                  temp = files[y]
                  if time_s[x] == int((temp['size_GB']*1000*8)/temp['speed_Mbps']):
                      ordered.append(temp['name'])
    return (ordered, max)
