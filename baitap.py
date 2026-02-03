import time
import sys
import random
import numpy as np
# Tăng giới hạn đệ quy để tránh lỗi khi chạy QuickSort trên mảng đã sắp xếp
# Mặc định Python là 1000, không đủ cho mảng lớn.
sys.setrecursionlimit(2000000)

def partition(arr, low, high):
	# chọn pivot ngẫu nhiên
	rand_idx = random.randint(low, high)
	# Đổi chỗ phần tử ngẫu nhiên đó về vị trí cuối (high)
	arr[high], arr[rand_idx] = arr[rand_idx], arr[high]
	pivot = arr[high]
	i = low - 1
	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1

def quick_sort(arr, low, high):
	if low < high:
		p = partition(arr, low, high)
		quick_sort(arr, low, p - 1)
		quick_sort(arr, p + 1, high)

def heapify(arr, n, i): # hàm sắp xếp sao cho mỗi parent lớn hơn children
	highest = i
	left = 2*i + 1
	right = 2*i +2
	if left < n and arr[left] > arr[highest]:
		highest = left
	if right < n and arr[right] > arr[highest]:
		highest = right 
	if highest != i:
		arr[highest], arr[i] = arr[i], arr[highest]
		heapify(arr, n, highest)

def heap_sort(arr):
	n = len(arr)
	# Sắp xếp lại các node theo đúng trình tự trong binary tree 
	for i in range(n//2 -1,-1,-1):
		heapify(arr, n, i)
	#Đổi chổ phần tử ở đầu chuỗi binary tree với phần tử cuối cùng của dãy và lặp lại quá trình đó
	for i in range(n-1,0,-1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)
	return arr

def merge_sort(arr):
	if len(arr) > 1:
		# Chẻ đôi mảng
		mid = len(arr)//2
		Left = arr[:mid]
		Right = arr[mid:]
		merge_sort(Left)
		merge_sort(Right)
		# chia mảng đến khi thành mảng đã được sort
		i = j = k = 0
		#merge 2 mảng lại 
		while i < len(Left) and j < len(Right):
			if Left[i] < Right[j]:
				arr[k] = Left[i]
				i+=1
			else:
				arr[k] = Right[j]
				j+=1
			k+=1
		# Nếu chạy vòng while trên mà chưa duyệt hết hết mảng bên trái tức là các phần tử bên trái lớn hơn nên xếp tiếp vào phần sau của mảng
		while i < len(Left): 
			arr[k] = Left[i]
			i+=1
			k+=1
		# Tương tự nếu chưa duyệt hết bên phải thì bên phải lớn hơn và xếp tiếp vào mảng
		while j < len(Right):
			arr[k] = Right[j]
			j+=1
			k+=1
	return arr


# Tạo dữ liệu
def create_data_set():
	data_set = []
	size = 1000000
	print(f"Đang tạo bộ dữ liệu có kích thước {size} phần tử")

	arr1 = np.random.randint(0,1000000, size)
	arr1.sort()
	data_set.append({"type":"Int 1", "data":arr1})

	arr2 = np.random.randint(0,1000000, size)
	arr2.sort
	arr2 = arr2[::-1]
	data_set.append({"type":"Int 2", "data":arr2})

	for i in range(3):
		arr = np.random.randint(0, 1000000, size)
		label = f"Int {i+1}" 
		data_set.append({"type": label, "data": arr})

	for i in range(5):
		arr = np.random.uniform(0, 100000, size)
		label = f"Float {i+1}"
		data_set.append({"type": label, "data": arr})
	return data_set

def run():
	data_set = create_data_set()
	results = []
	for idx, ds in enumerate(data_set):
		print("*"*30)
		print(f"Chạy lần {idx+1}")
		#copy để không làm hỏng bộ dữ liệu
		data_copy = ds["data"]

		#Quick sort
		arr = list(data_copy)
		start = time.time()
		quick_sort(arr, 0, len(arr)-1)
		print(f"Quick sort:  {(time.time()-start)*1000}")
		results.append((time.time()-start)*1000)

		#Heap sort
		arr = list(data_copy)
		start = time.time()
		heap_sort(arr)
		print(f"Heap sort:   {(time.time()-start)*1000}")
		results.append((time.time()-start)*1000)

		#Merge sort 
		arr = list(data_copy)
		start = time.time()
		merge_sort(arr)
		print(f"Merge sort:  {(time.time()-start)*1000}")
		results.append((time.time()-start)*1000)

		# Numpy sort 
		arr = np.array(data_copy)
		start = time.time()
		np.sort(arr)
		print(f"Numpy sort:  {(time.time() - start) * 1000}")
		results.append((time.time()-start)*1000) 
run()
