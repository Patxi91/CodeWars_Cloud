parts_list = ['0|111', '(1|00)0', '001*0', '100', '011', '1101*0|101', '01', '(1|00)1|0101*0', '1']

parts_dict = {
    'part_1': parts_list[0],
    'part_2': parts_list[1],
    'part_3': parts_list[2],
    'part_4': parts_list[3],
    'part_5': parts_list[4],
    'part_6': parts_list[5],
    'part_7': parts_list[6],
    'part_8': parts_list[7],
    'part_9': parts_list[8]
}

sub_pattern = '((({})({})*({}))|{})'

part_1 = sub_pattern.format(parts_dict['part_4'], parts_dict['part_2'], parts_dict['part_5'], parts_dict['part_1'])
part_3 = sub_pattern.format(parts_dict['part_9'], parts_dict['part_2'], parts_dict['part_8'], parts_dict['part_3'])
part_6 = sub_pattern.format(parts_dict['part_4'], parts_dict['part_2'], parts_dict['part_8'], parts_dict['part_6'])
part_7 = sub_pattern.format(parts_dict['part_9'], parts_dict['part_2'], parts_dict['part_5'], parts_dict['part_7'])

solution = '^(' + sub_pattern.format(part_6,part_3,part_7,part_1) +')+$'
