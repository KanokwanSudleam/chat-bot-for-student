def add(x):
    return 2*x

import PyICU
def isThai(chr):
    cVal = ord(chr)
    if(cVal >= 3584 and cVal <= 3711):
        return True
    return False
def tokenize(txt):
    bd = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
    bd.setText(txt)
    lastPos = bd.first()
    retTxt = ""
    try:
        while(1):
            currentPos = next(bd)
            retTxt += txt[lastPos:currentPos]
            if(isThai(txt[currentPos-1])):
                if(currentPos<len(txt)):
                    if(isThai(txt[currentPos])):
                        retTxt+="|"
            lastPos = currentPos
    except StopIteration:
        pass
    return retTxt

questions_class1 = ["วันนี้อากาศเป็นไง","วันนี้อากาศเป็นไง","อากาศเป็นยังไง","บ้านแกร้อนป้ะ","อากาศเป็นไง","ฝนจะตกไหม"
,"ร้อนมั้ย","วันนี้ฝนตกปะ","อากาศดีมั้ย","ฝนตกป้ะ","อากาศดีมั๊ย","ร้อนมั๊ย","อากาศเป็นยังไง","ฝนตกปะ"
,"วันนี้ฝนตกป่าว","วันนี้แถวนั้นอากาศดีปะ","ฝนตกป่ะ","ฟ้าเป็นไงบ้าง","อากาศร้อนมั้ย","ฝนตกป้ะมึง"
,"ตอนนี้อากาศดีมั้ย","แดดแรงไหมมึง","อากาศวันนี้เป็นไงบ้าง","ร้อนมั้ย","ข้างนอกร้อนป่ะ","อากาศดีป่ะ","ฝนตกมั้ย"
,"ร้อนป่าว","บ้านมึงร้อนปะ","อากาศเป็นไงบ้างวะ","ร้อนทั้งวันมึงว่าไหม","วันนี้อากาศป็นไงมั้ง?","ข้างนอกฝนตกไหม",
"แดดร้อนไหม","ที่นู่นหนาวมั้ย","ฝนตกหรือป่าว","วันนี้ฟ้าเปิดไหม","อากาศเป็นไงบ้าง","อากาศดีปะ","วันนี้ฝนตกป่าววะ"]

questions_class2 = ["พรุ่งนี้อากาศจะเป็นไง","พรุ่งนี้อากาศจะเป็นไง","พรุ่งนี้ฝนจะตกปะ","พรุ่งนี้ฝนจะตกปะ","พรุ่งนี้ฝนจะตกมั้ย"
,"พรุ่งนี้ฝนจะตกมั้ย","พรุ่งนี้อากาศเป็นยังไง","พรุ่งนี้แกว่าฝนจะตกป่ะวะ","มึงว่าพรุ่งนี้มึงจะซักผ้าได้ปะ","มึงว่าพุ่งนี้ฝนตกปะ"
,"พรุ่งนี้อากาศเป็นเช่นไร","คิดว่าพรุ่งนี้ต้องพกร่มมั้ย","คิดว่าพรุ่งนี้จะแดดร้อนแบบนี้ปะ","อากาศพรุ่งนี้เป็นไง","พรุ่งนี้ฝนจะตกไหม"
,"พรุ่งนี้ฝนจะตกเปล่า","พุ่งนี้อากาศจะเป็นไงบ้าง","พรุ่งนี้อากาศเปนยังไง","พรุ่งนี้อากาศเป็นไงรู้ปะ","ฝนตกป่าว","มึงพอรู้ปะช่วงนี้ฝนตกบ่อยไหม"
,"คิดว่าพรุ่งนี้อากาศเป็นไง","คนก่อนป็อปนี่ชื่อไรนะ","คิดว่าพรุ่งนี้ฝนจะตกไหม","พรุ่งนี้ฝนจะตกป้ะวะ","พรุ่งนี้อากาศดีมั้ย"
,"พยากรณ์อากาศพรุ่งนี้ว่าไงบ้าง","มึงดูพยากรณ์อากาศปะวะ","พรุ่งนี้อากาศเป็นไง","มึงว่าพรุ่งนี้ฝนจะตกป่ะ","มึงว่าพน.ฝนตกปะ"
,"แล้วพรุ่งนี้อากาศจะเป็นไง","อากาศแมร่งร้อนชัวพรุ่งนี้มึงว่าไหม?","ช่วยดูสภาพอากาศพรุ่งนี้ให้หน่อย","ช่วงนี้ฝนตกบ่อยปะ"
,"พรุ่งนี้จะตกมั้ย","พรุ่งนี้ฝนตกไหม","พรุ่งนี้จะครึ้มไหมเนี่ย","พรุ่งนี้อากาศจะเป็นยังไง","พรุ่งนี้อากาศจะดีปะ"
,"พรุ่งนี้จะร้อนป่าววะ"]

questions_class3 = ["ไปไง","ไปไง","ไปไง","ไปยังไง","ไปยังไง","ไปไงอ่ะ","ไปไงอ่ะ","จะนั่งรถไรไปดีวะ","กูอยากไป "
,"ไปทางไหนไวๆถูกๆบ้าง","ลาดกระบังอยู่ตรงไหนของกทมวะ?","จะไปได้อย่างไร","จะไปทางไหนได้บ้าง","ไปไงดี","จากไปยังไง"
,"จากไปยังไงหรอ","ไปกันมั๊ย","จากไปไปยังไงได้มั่ง","ขึ้นรถไปอนุตรงไหน","ไปไงอะ","มึงถ้ากูจะไปกูไปทางไหนได้บ้างวะ","จากมอเราไปยังไง"
,"มีรถอะไรไปได้บ้าง","นั่งรถอะไรไปได้บ้าง","จากไปยังไงได้บ้าง","อยากไป","ไปไม่เป็น","ไปยังไงง่ายสุด","รถอะไรไปบ้าง","กูจะไปนี่ ไปไงวะ"
,"อยากไปวะไปไงวะ","จากไปยังไง","มีรถแท็กซี่ไปไหม","จากไป ไปยังไงได้มั้ง","จากไปไปไง ถ้าไปรถตู้","พาไปหน่อย"
,"จะไปยังไงจากที่นี้","ไปยังไง","ไปไปยังไง"]

questions_class4 =["แปลว่าอะไร","แปลว่าอะไร","แปลว่าอะไร","แปลให้หน่อย","แปลให้หน่อย","คือไรอ่ะ"
,"มันแปลว่าไรวะ","เปิดdictแล้วงง","ไม่เข้าใจ","หมายถึงอะไร","แปลว่าอะไร","แปลว่า","ไม่รู้จริงๆ","แปลว่าอะไร"
,"แปลว่าอะไรหาให้หน่อย","แปลว่าไร","แปลว่าอะไรแปลให้หน่อย","แปลให้หน่อยดิ","เปิดดิกคำว่าให้ที","แปลให้"
,"คือไร","คำนี้แปลว่าไรวะ","มันแปลว่าไร","คือไรวะ","แม่งแปลว่าไรวะ","คือไร","คำนี้แปลว่าอะไรอะ","รู้ความหมายของคำนึ้ปะ"
,"หมายความว่าไง","รู้ความหมายคำนี้ป่ะ","คำนี้แปลว่าไร","แปลว่าไร","แปลว่ารัย"]

questions_class5 = ["รถไฟรอบหน้ามากี่โมง","รถไฟรอบหน้ามากี่โมง","รถไฟรอบหน้ามากี่โมง","รถไฟรอบต่อไปมากี่โมง"
,"รถไฟรอบต่อไปมากี่โมง","รถไฟมากี่โมง","รถไฟมากี่โมง","จะทันรถไฟรอบหน้าป้ะ","มึงขึ้นรถไฟประจำปะ กูอยากรู้ว่าขาขึ้นมันจะมาอีกทีกี่โมง"
,"รอบหน้าตอนไหน","อีกกี่นาทีกว่ารถไฟจะมา","เฮ้ยตกรถไฟอะ ต้องรอนานแค่ไหนอะถึงจะมาอีกคัน","รถไฟรอบต่อไปมากี่โมงวะ"
,"รถไฟรอบต่อไปจะมากี่โมง","อีกกี่นาทีรถไฟจะมา","รถไฟมากี่โมง","รถไฟรอบต่อไปมาเมื่อไหร่","รถไฟรอบต่อไปมากี่โมง"
,"เปิดตารางรถไฟดิ","ต่อไปรถไฟจะมากี่โมง","เร็วสุดกี่โมง","อีกกี่นาทีรถไฟจะมาวะ","รถไฟจะมาอีกทีกี่โมงอ่ะ","รถไฟรอบหลังจากมากี่โมง"
,"รอบต่อไปกี่โมง","อีกนานไหมกว่าจะมา","อีกนานมั้ยกว่ารถจะมา","รถไฟต่อไปรอบไร","รถไฟจะมาอีกทีตอนไหนวะ","รถไฟมากี่โมง","ตารางรถไฟมีรอบไหนบ้าง"
,"เอาตารางรถไฟจากไหน","ตารางรฟไฟหาได้จากไหนอะ","ขอดูตารางรถไฟหน่อย","รถไฟรอบนี้ออกไปยัง ต้องรออีกกี่นาที"
,"รอไฟมากี่โมง","รถไฟขบวนต่อไปกี่โมง","รถไฟรอบต่อไปกี่โมง","รถไฟมาอีกทีกี่โมง"]

questions_class6 = ["ขอตารางรถไฟหน่อย","ขอตารางรถไฟหน่อย","ขอตารางรถไฟหน่อย","ขอตารางรถไฟหน่อย"
,"ขอตารางรถไฟหน่อย","ขอตารางรถไฟหน่อย","ขอตารางรถไฟหน่อย","ขอตารางรถไฟหน่อย","ขอตารางรถไฟหน่อย"
,"มีตารางรถไฟป่าว","มีตารางรถไฟป่าว","มีตารางรถไฟไหม","มีตารางรถไฟไหม","ขอดูตารางรถไฟหน่อยดิ่"
,"มึงขึ้นรถไฟประจำปะ กูอยากได้ตารางเวลาของรถไฟ","รถไฟออกกี่โมงบ้าง","ต่อจากข้อข้างบน","ไหนๆมีให้ดูปะ"
,"ใครมีตารางรถไฟให้ยืมมั้ง","ตารางรถไฟให้หน่อย","รู้ตารางรถไฟสายนี้ไหม","มีตารางปะ","ขอตารางรถไฟฟน่อย"
,"มึงมีตารางรถไฟไทยปะ","อยากได้ตารางเวลารถไฟ","ขอตารางรถไฟหน่อยดิ","มีรถไฟรอบไหนบ้าง","ดูตารางรถไฟให้หน่อย"
,"มีตารางรถไฟปะ","รถไฟมีรอบกี่โมงบ้าง","มีตารางรถไฟป่ะ","ดูตารางรถไฟจากที่ไหนได้บ้าง","ตารางรถไฟหาได้จากไหนอะ"
,"ยืมตารางรถไฟหน่อย","มีรอบรถไฟเที่ยวปะ","ตารางรถไฟขอที่ไหนอะ","ใครมีตารางรถไฟมั่ง","ขอตารางถไฟหน่อย"
,"ขอตารางรถไฟหน่อยดิ้"]


#tokenize the question
def questiontokenize(questions):
    words = []
    for question in questions:
        temp = tokenize(question).split("|")
        for word in temp:
            words.append(word)
    return words
#generate dictionary
def freq(words):
    from collections import defaultdict
    wordsFreq = defaultdict(int)
    for word in words:
        wordsFreq[word] = wordsFreq[word]+1
    return wordsFreq


#preprocessing
def preprocessing(questions):
    return freq(questiontokenize(questions))


class1 = preprocessing(questions_class1)
class2 = preprocessing(questions_class2)
class3 = preprocessing(questions_class3)
class4 = preprocessing(questions_class4)
class5 = preprocessing(questions_class5)
class6 = preprocessing(questions_class6)

all_class_data = [(class1,"class1"),(class2,"class2"),(class3,"class3"),
             (class4,"class4"),(class5,"class5"),(class6,"class6")]

#inputtokenize
def inputtokenize(input):
    return tokenize(input).split("|")

def naivebayes(inputwords):
    inputwords = inputtokenize(inputwords)
    all_class_probs = []
    for data in all_class_data:     #data = all_class_data[i]
        prob = 1
        countn = sum(data[0].values())+len(inputwords)   #count all word in current class
        for word in inputwords:    
            prob = prob*(data[0][word]+1)/countn
        all_class_probs.append(prob)
    #return all_class_probs

    if(all_class_probs.index(max(all_class_probs))==0):
        return "weather"
    elif(all_class_probs.index(max(all_class_probs))==1):
        return "weather tommorow"
    elif(all_class_probs.index(max(all_class_probs))==2):
        return "google map"
    elif(all_class_probs.index(max(all_class_probs))==3):
        return "translate"
    elif(all_class_probs.index(max(all_class_probs))==4):
        return "next train"
    elif(all_class_probs.index(max(all_class_probs))==5):
        return "train"


english = ["w","e","E","r","R","t","T","y","u","U","i","I","o","p","P","[","{","]",
           "a","A","s","S","d","D","f","F","g","G","h","H","j","J","k","K","l","L",
           ";",":","q","z","x","c","C","v","V","b","n","N","m",",","<",".",">","/","?",
           "1","4","5","6","^","7","8","9","0","-","="]
thai =    ["ไ","ำ","ฎ","พ","ฑ","ะ","ธ","ั","ี","๊","ร","ณ","น","ย","ญ","บ","ฐ","ล","ฟ",
           "ฤ","ห","ฆ","ก","ฏ","ด","โ","เ","ฌ","้","็","่","๋","า","ษ","ส","ศ","ว","ซ","ง",
           "ผ","ป","แ","ฉ","อ","ฮ","ิ","ื","์","ท","ม","ฒ","ใ","ฬ","ฝ","ฦ",
           "ๅ","ภ","ถ","ุ","ู","ึ","ค","ต","จ","ข","ช"]

#thai to english
def ThaiToEng(x):
    #convert to array
    temp = []
    for i in x:
        temp.append(i)
    #get index
    index = []
    for i in temp:
        if(i in thai):
            index.append(thai.index(i))
    #convert to english
    b = ""
    for i in index:
        b = b+english[i]
    return b

#english to thai
def EngToThai(x):
    #convert to array
    temp = []
    for i in x:
        temp.append(i)
    #get index
    index = []
    for i in temp:
        if(i in english):
            index.append(english.index(i))
    #convert to thai
    b = ""
    for i in index:
        b = b+thai[i]
    return b







import sys, json

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])
    #return lines[0]
"""
def main():
    #get our data as an array from read_in()
    lines = read_in()

    # Sum  of all the items in the providen array
    total_sum_inArray = 0
    for item in lines:
        total_sum_inArray += item

    #return the sum to the output stream
    print(total_sum_inArray)
"""

def main():
    lines = read_in()
    #return naivebayes(lines)
    return naivebayes(EngToThai(lines))
    #return lines
"""
class1 = อยากรู้ลมฟ้าอากาศ
class2 = อยากได้พยากรณ์ฟ้าอากาศพุ่งนี้
class3 = อยากหาทางไปสยามจากลาดกระบัง
class4 = อยากได้คำแปล
class5 = อยากรู้ตารางรถไฟรอบต่อไป
class6 = อยากได้ตารางรถไฟ

"""
# Start process
print(main())
#rint(main())
