def sing():
    lyrics = []
    for num in range(99, 0, -1):
        if num > 1:
            lyrics.append(f"{num} bottles of beer on the wall, {num} bottles of beer.")
            if num-1 > 1:
                lyrics.append(f"Take one down and pass it around, {num-1} bottles of beer on the wall.")
            else:
                lyrics.append(f"Take one down and pass it around, 1 bottle of beer on the wall.")
        else:
            lyrics.append("1 bottle of beer on the wall, 1 bottle of beer.")
            lyrics.append("Take one down and pass it around, no more bottles of beer on the wall.")

    lyrics.append("No more bottles of beer on the wall, no more bottles of beer.")
    lyrics.append("Go to the store and buy some more, 99 bottles of beer on the wall.")

    return lyrics
