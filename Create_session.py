import datetime
import random

now = datetime.datetime.now()
print(now)

#program should create training sessions

#lists of the sorted exercises
power=["a", "b", "c", "d", "e", "f", "g", "h", "i"]
power_izom=["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1"]
cond=["A", "B", "C", "D"]
top=["1", "2", "3", "4", "5", "6"]
top_izom=["1A", "2A", "3A", "4A", "5A", "6A"]
stam=["Z", "Y", "X", "U", "T"]
izom=["10", "11", "12", "13", "14", "15"]
abs_ex=["€", "&", "@", "(", ")"]
abs_ex_izom=["111", "112", "113", "114", "115"]


#choosing what type with input

print("Vyberte si typ vasho treningu")
print("napiste cislo zhodne s vasim treningom")
print("1 Chcem si vybraty Klasicky treninguk")
print("2 Chcem si vybrat Izometricky trening")
print("3 Chcem si vybrat Kondicny trening")



#checking correct input
try:
    x = int(input("Chcem si zostavit trening: "))

except ValueError:
    print("Zadajte, prosím, platné číslo.")
    
else:
    def choose():
        cur_session = []
        
        if x==1:
            first_exercise=random.choice(power)
            cur_session.append(first_exercise)
            second_exercise=random.choice(power)
            cur_session.append(second_exercise)
            third_exercise=random.choice(cond)
            cur_session.append(third_exercise)
            fourth_exercise=random.choice(top)
            cur_session.append(fourth_exercise)
            fifth_exercise=random.choice(stam)
            cur_session.append(fifth_exercise)
            sixth_exercise=random.choice(abs_ex)
            cur_session.append(sixth_exercise)

            return cur_session

        if x==2:
            first_exercise = random.choice(power_izom)
            cur_session.append(first_exercise)
            second_exercise = random.choice(power_izom)
            cur_session.append(second_exercise)
            third_exercise = random.choice(top_izom)
            cur_session.append(third_exercise)
            fourth_exercise = random.choice(abs_ex_izom)
            cur_session.append(fourth_exercise)
            fifth_exercise = random.choice(abs_ex_izom)
            cur_session.append(fifth_exercise)
            sixth_exercise = random.choice(abs_ex)
            cur_session.append(sixth_exercise)

            return cur_session

        if x==3:
            first_exercise = random.choice(power_izom)
            cur_session.append(first_exercise)
            second_exercise = random.choice(power)
            cur_session.append(second_exercise)
            third_exercise = random.choice(top)
            cur_session.append(third_exercise)
            fourth_exercise = random.choice(stam)
            cur_session.append(fourth_exercise)
            fifth_exercise = random.choice(cond)
            cur_session.append(fifth_exercise)
            sixth_exercise = random.choice(cond)
            cur_session.append(sixth_exercise)
            seventh_exercise = random.choice(stam)
            cur_session.append(seventh_exercise)
            eighth_exercise = random.choice(abs_ex)
            cur_session.append(eighth_exercise)

            return cur_session

        else:
            #ValueError
            return("vyberte a napiste cislo pre trening")
        
    #printing created training session
    session=choose()
    def show_session():
        for exercise in session:
            print (exercise)
        
    print(session)
    show_session()



try:
    y = int(input("Kolko treningov chcete zostavit: "))

except ValueError:
    print("Zadajte, prosím, platné číslo.")
    
else:
    if y>=2:
        def more_sessions():
            all_sessions = []
            for i in range(1, (y+1)):
                new_session = choose()
                all_sessions.append(new_session)
            for session in all_sessions:
                print("Novy trening:")
                for exercise in session:
                    print(exercise)
    if y == 1:
        for exercise in session:
            print(exercise)
