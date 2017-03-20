graph = {'Sukamandi': ['Sukamundur', 'Sukasedih','Sukarugi','Akuarius','Gemini'],
             'Gemini': ['Sukasedih', 'Pisces','Leo','Akuarius','Sukamandi'],
             'Akuarius': ['Sukamandi','Gemini','Leo'],
             'Leo': ['Pisces','Gemini','Akuarius'],
             'Sukasedih': ['Libra','Sukamandi','Gemini'],
             'Pisces': ['Gemini','Leo'],
             'Sukarugi': ['Sukamandi'],
             'Sukamundur': ['Sukamandi'],
             'Libra': ['Sukasedih'],
         }
 
def jalur_terpendek(graph, awal, tujuan, jalur=[]):
        jalur = jalur + [awal]
        if awal == tujuan:
            return jalur
        if not graph.has_key(awal):
            return None
        jalurpendek = None
        for node in graph[awal]:
            if node not in jalur:
                newjalur = jalur_terpendek(graph, node, tujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Kecamatan Kota Bintang")
print ("(Sukamandi,Gemini,Akuarius,Sukasedih)")
print ("(Pisces,Sukarugi,Sukamundur,Libra)")
print ("\n")
awal = raw_input("Titik Awal : ")
tujuan = raw_input("Titik Tujuan : ")
hasil = jalur_terpendek(graph, awal, tujuan, jalur=[])
print "Jalur Terpendek", hasil
