import math

def is_member_of_AP(a,d, num):
    return ((num - a)%d == 0 & int((num - a)/d) >= 0)

def is_part_of_series(lst):
    rejected_elem = []
    for elem in lst:
        if elem == 0 or elem == 1:
            continue
        
        neg_status = elem<0
        pow_val = math.log2(abs(elem))
        if math.ceil(pow_val) == math.floor(pow_val):
            if neg_status and (is_member_of_AP(2,4,pow_val) or is_member_of_AP(3,4,pow_val)):
                continue
            if not neg_status and (is_member_of_AP(0,4,pow_val) or is_member_of_AP(1,4,pow_val)):
                continue

        rejected_elem.append(elem)
    return rejected_elem
                    

def generate_series(range_val):
    series = [0,1]
    for i in range(2,range_val):
        series.append(2*series[i-1] - 2*series[i-2])
    print(series)

if __name__ == "__main__":
    inp_list = list(map(int, input().split(' ')))
    # generate_series(int(input()))
    
    rejected_elem = is_part_of_series(inp_list)

    if len(rejected_elem)==0:
        print('[INFO] All entered elements are part of the series.')
    else:
        print(f'[INFO] These elements {rejected_elem}, are not part of the series.')
