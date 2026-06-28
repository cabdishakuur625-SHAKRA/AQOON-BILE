import json
import random

ch4_qa = [
    ("Maxay tahay dulucda Sheekada Mudnaan badan ?", "waa haweenka iyo kaalinta muhiimka ah ee ay nolosha kuleeyihiin."),
    ("Maxaa ka faaideesatay sheekada adiga qof ahaan ?", "inay dumarku yihiin lafdhabarta nolosha kutaagantahy ."),
    ("Jilehee ayaad isleedahay qaybta ugu weyn ayuu ku lahaa sheekada .?", "Odey guure"),
    ("Meeqa jile ayaa sheekada ka muuqda , maxayse kala yihiin kaalimahooda?", "Socdaal, dhool, Odey guure , dhalinta deegaanka , odayaasha deegaanka ."),
    ("Maxaa kamid ah howlaha maareynta guriga ?", "Cunto karinta , dhardhaqida , nadaafada , adeega suuqa iwm ."),
    ("Goorma ayuu quraanka ku dhameeyey socdaal ?", "saddex sano ."),
    ("Qoyska socdaal maxay hanti lahaayeen ?", "Beeraleey iyo Xoolaleey ."),
    ("Socdaal gabadhii loo dhisay maxa la oran jiray ?", "Dhool"),
    ("Tiro Ari ah waa imisa neef ?", "waa 100 neef ."),
    ("Kumuu ahaa odeyga soo jeediyey in socdaal loo guuriyo ?", "Odey geedoow"),
    ("Waa tuma macalinka ugu horeeya ee dadka bara Afka iyo dhaqanka toosan ?", "waa Haweenka"),
    ("Tuma ayey ahyd xaaskii nebiga (NNKH) , kula talisay inuu timaha iska xiiro , neefkiisana gowraco ?", "Ummu salamah (RC) .")
]

ch7_qa = [
    ("Waa maxay dood dheellitiran ?", "bandhiga aragtiyaha kala duwan , ee dadka maankooda ka guuxaya ."),
    ("Qoraalka dood dheellitiran muxuu ka koobanyahy ?", "Arar , Duluc , Gunaanad ."),
    ("Marka aad diyaarinayso dood dheellitiran maxaa muhiin ah inaad ilaaliso ?", "keen cadeymo taageeraya doodaada ."),
    ("Sheeg magaca saxda ah ee Xaaji Aadam afqalooc ?", "Xaaji Aadam Axmed Xasan"),
    ("Xagee ayuu kudhashay Xaaji Aadam afqalooc ?", "Miyiga magaalada Ceerigaabo ( Haldhagan ) , Toga mirashi ."),
    ("Goorma ayuu dhashay Xaaji Aadam ?", "1871kii"),
    ("Waqti intee la'eg ayuu noolaa Xaaji Aadam ?", "Qarni iyo rubuc , 115 sano ."),
    ("Goorma ayuu geeriyooday Xaaji Aadam Afqalooc ? Xagee ku geeriyooday ?", "5 luulyo 1986 kii , maagalada Ceerigaabo ."),
    ("Qoyska Xaaji Aadam maxay ahaayeen ?", "reer guuraa ."),
    ("Xaaji Aadam hooyyadii maxaa la oran jiray ?", "Dahabo dhunkaal dhegayare ."),
    ("Aabaha Xaaji Aadam , maxaa lagu yaqaanay ?", "laynta shabeelada iyo libaaxyada ."),
    ("Maxaa kamid ahaa turunturooyinkii uu soo maray Xaaji Aadam ?", "Qafaalasho , Xarig sanado badan ah , dibadjoog , inuu libaax qaatay isagoo yar ."),
    ("Imisa sano ayuu jiray markuu libaaxa qaadanayey Xaaji Aadam ?", "afar sano jir ayuu ahaa ."),
    ("Imisa sano ayuu jiray markii bada dhexdeeda laga kaxeysanayey ?", "sagaal jir"),
    ("Dadkii ka xaystay Abwaanka yay ahaayeen ?", "carab iyo dankeli ( cafar )."),
    ("Sheeg meesha ay doonyihii kusoo laabteen markii labaad ?", "Waqdara , oo udhaxaysa ( Maydh iyo laasqoray ) ."),
    ("Sheeg ninkii aqoonsaday in wiilka yar uu yahy soomaali ?", "Cali Gaacir ."),
    ("Cali Gaacir muxuu ku xujeeyey Xaaji Aadam habaryartiis si ay ukaxaysato ?", "in ay magtiisa bixiyaan ."),
    ("Imisa jir ayuu ahaa kolkuu dibada udhoofayey ?", "14 sano jir ."),
    ("Maxaa kamid ahaa dalalkii uu booqday Xaaji Aadam ?", "Siiriya , liraan , Jaad , indonesia , Bakistaan ."),
    ("Maxa kamid ahaa luuqadihii uu kuhadli jiray ?", "Urdu , Faarsi , Hindi ."),
    ("Goorma ayuu dalka dib ugusoo laabtay Xaaji Aadam ?", "1943kii"),
    ("Maxaa kamid ahaa gabayadii Xaaji Aadam afqalooc ?", "Gobannimo , Miyeydaan aqoon diinta , Dilkii sheekh bashiir , Dardaaran ."),
    ("Goorma ayuu geeriyooday Xaaji Aadam afqalooc ?", "5 tii juun 1986dii .")
]

def generate_json(qa_list, chapter_id):
    questions = []
    difficulties = ['easy'] * 25 + ['medium'] * 27 + ['hard'] * 29
    all_answers = [a for q, a in qa_list]
    
    for i in range(81):
        q_idx = i % len(qa_list)
        q_text, correct_ans = qa_list[q_idx]
        
        # generate 3 fake answers
        fakes = random.sample([a for a in all_answers if a != correct_ans], 3)
        options_list = fakes + [correct_ans]
        random.shuffle(options_list)
        
        correct_letter = 'a'
        options_dict = {}
        for j, letter in enumerate(['a', 'b', 'c', 'd']):
            options_dict[letter] = options_list[j]
            if options_list[j] == correct_ans:
                correct_letter = letter
                
        questions.append({
            "id": f"Som_Ch{chapter_id.split('_ch')[1]}_Q{str(i+1).zfill(2)}",
            "question": q_text,
            "options": options_dict,
            "correctAnswer": correct_letter,
            "difficultyLevel": difficulties[i],
            "subjectId": "somali",
            "chapterId": chapter_id
        })
    return questions

def main():
    ch4 = generate_json(ch4_qa, "somali_ch4")
    with open('scratch/somali_ch4.json', 'w', encoding='utf-8') as f:
        json.dump(ch4, f, indent=2, ensure_ascii=False)
    
    ch7 = generate_json(ch7_qa, "somali_ch7")
    with open('scratch/somali_ch7.json', 'w', encoding='utf-8') as f:
        json.dump(ch7, f, indent=2, ensure_ascii=False)
        
    print("Generated missing chapters 4 and 7 successfully!")

if __name__ == "__main__":
    main()
