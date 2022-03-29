condong_index = None # This variable will determine is pivot start from the right side or from the left side

def check_palindrome(kata) :
    banyak_kata = len(kata)
    i = 0
    j = (banyak_kata - 1)

    checker = 0

    while i < banyak_kata :

        if kata[i] == kata[j] :
            checker += 1

        i += 1
        j -= 1

    if checker == banyak_kata :
        return 1
    else :
        return 0

def guess_the_word(kata) :
    global condong_index
    banyak_kata = len(kata)
    i = 0
    j = (banyak_kata - 1)

    if kata[i] == kata[j] :
        i += 1
        j -= 1
    else :
        if banyak_kata > 4 :
            if kata[i + 1] != kata[j] :
                if kata[i + 1 + 1] != kata[j] :
                    if kata[j - 1] != kata[i] :
                        if kata[j - 1 - 1] != kata[i] :
                            return 0 # The sentence that inserted by user cannot be palindrome
                        else :
                            titik_point = j - 1 - 1
                            condong_index = 1
                            return titik_point
                    else :
                        titik_point = j - 1
                        condong_index = 1
                        return titik_point
                else :
                    titik_point = i + 1 + 1
                    condong_index = 0
                    return titik_point
            else :
                titik_point = i + 1
                condong_index = 0
                return titik_point
        else :
            if kata[i + 1] != kata[j]:
                    if kata[j - 1] != kata[i]:
                        return 0 # The sentence that inserted by user cannot be palindrome
                    else:
                        titik_point = j - 1
                        condong_index = 1
                        return titik_point
            else :
                titik_point = i + 1
                condong_index = 0
                return titik_point


def reverse_iterasi_from(point, kalimat) :
    global condong_index
    kata_yang_hilang = ""
    banyak_kata = len(kalimat)

    if condong_index == 0:
        i = (point - 1)
        while i >= 0 :
            kata_yang_hilang += kalimat[i]
            i -= 1
    
    else :
        i = (banyak_kata - 1)
        while i > point :
            kata_yang_hilang += kalimat[i] 
            i -= 1

    return kata_yang_hilang

def penyatuan_kalimat(kalimat,missing_word,point) :
    global condong_index
    if condong_index == 0 :
        kalimat += missing_word
        return kalimat
    else :
        missing_word += kalimat
        return missing_word






print()
print("============================ Guess Word To Be Palindrome =================================")
print()
print()
print()

uji_Kata = input("Please insert 1 sentece and let the program guess the palindrome : ")

isPalindrome = check_palindrome(uji_Kata)

if isPalindrome == 1 :
    print("The sentence that you are inserted have not any palindrome!")
else :
    titik_pivot = guess_the_word(uji_Kata)
    kata_hilang = reverse_iterasi_from(titik_pivot,uji_Kata)
    prediksi_kalimat = penyatuan_kalimat(uji_Kata,kata_hilang,titik_pivot)
    print("Palindrome from the word that you inserted : {0}" .format(prediksi_kalimat))
        
