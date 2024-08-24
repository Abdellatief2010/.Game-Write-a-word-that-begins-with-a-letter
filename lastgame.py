letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
input_user_letter = input('Enter letter : ').lower()
while input_user_letter not in letters :
    continue_game = input('are you want to continue that game (yes / no ): ')
    if continue_game == "yes" :
        input_user_letter = input(f'"{input_user_letter}" not letter enter letter : ')
    elif continue_game == 'no' :
        print('Good bay')
        exit()

# هذا الجزء من الكود لادخال الحرف و معرفة ان كان المستخدم يريد اكمال اللعبة او لا   
#====================================================================================================================================     
else:
 the_total=0  #   هذا المتغير لحفظ قيمة المجموع 
 catigories ={'boys':['ahmed','basem','charles','deiab','emad','fares','gamal','hamed','islam','jack','kareem','lawson','mohamed','nour','omar','pranch','qays','ramy','salem','tamer','umer','vini','waseem','xan','yaseen','zeiad'],
             'girls':['ava','beatrice','callie','dayner','evelynmae','florence','giselle','harmony','izabella','johander','kehlanee','luna','montezuma','nyte','odessa','paislee','qaisara','reagan','shulim','tatum','urja','vienna','wendy','xara','yasmine','zahra'],
             'animals':['aardvark','babirusa','cabbage moth','dachsador','eagle','fainting goat','gaboon viper','haasts eagle','ibex','ibis','jabiru','kagu','lion','macaque','nabarlek','oak toad','pachycephalosaur','quagga','rabbit','saanen goat','taco terrier','uakari','valley bulldog','wahoo fish','x-ray tetra','yabby','yak','zebra',],
             'plants':['apple','babby rabber plants','cabbage','daffodil','early girl tomato','flower','galaxy petunia','hackberry tree','ice plant','jacaranda tree','kalanchoe','lace aloe','macadamia nut tree','njoy photos','oak mistletoe','pacific rhododen','quaking aspen','radish','saffron crocus','tall fescue gras','umbrella plant','valerian','wall germander','xylosma''yarrow','zebra grass',],
             'things':['airplane','ball','car','door','egg','fan','game','hammer','ice','jar','key','leaf','moon','necklace','onion','paint','queen','rabbit','saw','tree','umbrella','van','water','xylophone','yacht','zero'],
             'countries':['albania','burkina faso','cameroon','dominica','egypt','france','gabon','hungary','iraq','japan','kenya','luxembourg','mali','nigeria','oman','palestine','qatar','russia','samoa','thailand','ukraine','vanuatu','Wallis','xina','yemen','zambia'],
 }
#    هذا الديكشنري يحتوي عل الفئات التي تحتوي على الكلمات التابعة لكل فئة
 enter_boy = input(f'enter boy with {input_user_letter} : ').lower()
 enter_girl = input(f'enter girl with {input_user_letter} : ').lower()
 enter_animal = input(f'enter animal with {input_user_letter} : ').lower()
 enter_plant = input(f'enter plant with {input_user_letter} : ').lower()
 enter_thing = input(f'enter thing with {input_user_letter} : ').lower()
 enter_country = input(f'enter country with {input_user_letter} : ').lower()
#           هذه المتغيرات لحفظ القيم التي يدخلها اليوزر بناءا على طلب ادخال كلمة لكل فئة 

 error_ = 0
       
 def check_word(enter_,catigory) :#   the_total  او error_ هذا الفانكشن لمعرفة هل مدخلات اليوزر صحيحة ام لا و اظهار النتيجة بحيث يتمكنم اي فانكشن من استدعاء المتغير  
    global the_total
    global error_
    if enter_ in catigories[catigory] and enter_.startswith(input_user_letter) :
      the_total+=10
    else:
        the_total+=0
        error_+=1


def errors(enter_,catigory):#    هذا الفانكشن لارسال رسالة لليوزر في حالة ادخاله اجابة خاطئة تخبره بخطئه فيها 
    global error_
    if error_ != 0 :
        print(f'"{enter_}" not {catigory} start with {input_user_letter}')
        error_=0
    

check_word(enter_boy,'boys')
errors(enter_boy,'boy')

check_word(enter_girl,'girls')
errors(enter_girl,'girl')

check_word(enter_animal,'animals')
errors(enter_animal,'animal')

check_word(enter_plant,'plants')
errors(enter_plant,'plant')

check_word(enter_thing,'things')
errors(enter_plant,'thing')

check_word(enter_country,'countries')
errors(enter_plant,'country')
#   تستدعي هنا الفانكشن التي صنعناها
print(f'your total is {the_total}/60')#     نقوم هنا بارسال رسالة لليوزر نخبره فيها بمجموعه 
