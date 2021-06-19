import easyocr.easyocr as easyocr

print('Start OCR License Plate : ')

reader = easyocr.Reader(['ko'])

result = None 
temp = None 
for i in range(23) : 
    str_i = str(i+5)
    if result is not None:
        temp = result 
    result = easyocr.reader.readtext('./result/frame/detected'+str_i+'.jpg', detail = 0)

    str_result = "\n".join(result)
           
    if temp != result : 
        with open("./result/번호판.txt", "a") as f:
            f.write(str_i)
            f.write(':')
            f.write(str_result)
            f.write('\n')
        print(result)
        