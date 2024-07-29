def solution(phone_book):
    phone_book.sort() 
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False 
    return True

#def solution(phone_book) :
#    hash_map = {}
#    for nums in phone_book:
#        hash_map[phone_number] = 1
        
#    for phone_number in phone_book:
#        jubdoo = ""
#        for number in phone_number:
#            jubdoo += number 
            
#            if jubdoo in hash_map and jubdoo != phone_number:
#                return False 
#    return True
