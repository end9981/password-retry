password = 'a123456'
c = 3
while True:
	x = input('請輸入密碼:')
	
	if x == 'a123456':

		print('登入成功')
		break

	else:
		
			c = c - 1
			print('輸入密碼錯誤','剩餘次數',c)
			if c == 0 :
				break

