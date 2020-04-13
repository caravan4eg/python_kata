def pick_peaks(arr):
    d = {'pos': [], 'peaks': []}
    for i in range(1, len(arr)-1):
        if arr[i-1]< arr[i] > arr[i+1] or arr[i-1] < arr[i] >= arr[i+1]:
            d['pos'].append(i)
            d['peaks'].append(arr[i])

    print(d)

pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3])
