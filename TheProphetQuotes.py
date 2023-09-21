import streamlit as st
import random
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.buy_me_a_coffee import button

def main():

    custom_css = """
        <style>
            .element-container,
            .stButton {
                display: flex;
                justify-content: center;
            }

            .stButton>button {

                width: 220px;
                height: 55px;
                font-size: 20px;
                background-color: #557AB1;
                border: none;
                border-radius: 25px;
                color: #F6F6F6;
            }
        </style>
    """
    
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #335575;'> </p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color:#335575; font-size: 38px;'>رسالة من الحبيب المصطفى</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #335575; font-size: 18px'>ألفاظ الرسول الكريم ﷺ الوجيزة القليلة اللفظ الكثيرة المعاني الجامعة للأحكام والحكم لعلها تكون رسالة تلامس قلبك وتنير دربك</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #335575;'>💙</p>", unsafe_allow_html=True)
    

    QUOTES = [
        "إنَّما الأعمالُ بالنِّيَّاتِ ","المَرْءُ معَ مَن أَحَبَّ.","أَسْلِمْ تَسْلَمْ","الْحَرْبُ خَدْعَةٌ",
        "ليسَ الشَّديدُ بالصُّرَعَةِ ، إنَّما الشَّديدُ الَّذي يملِكُ نفسَه عندَ الغَضبِ","وأيُّ داءٍ أدْوَى مِن البُخلِ","الأرواح جنودٌ مُجنَّدةٌ، فما تعارف منها ائتلف، وما تناكر منها اختلف","إنَّ مِنَ البَيَانِ لَسِحْرًا",
        "إنَّ من الشِّعرِ حكمةً","نِعْمَتانِ مَغْبُونٌ فِيهِما كَثِيرٌ مِنَ النَّاسِ: الصِّحَّةُ والفَراغُ","من غَشَّنَا فَلَيْسَ مِنَّا","مَنْ كَانَ يُؤْمِنُ بِاللَّهِ وَالْيَوْمِ الآخِرِ فَلْيَقُلْ خَيْرًا أَوْ لِيَصْمُتْ",
        "لَا يَحِلُّ لِمُسْلِمٍ أَنْ يَهْجُرَ أَخَاهُ فَوْقَ ثَلَاثِ لَيَالٍ","اليدُ العُلْيَا خير من اليدِ السُّفْلَى","تَركُ الشَّرِّ صَدَقَةٌ","الحَياءُ كُلُّهُ خَيْرٌ",
        "إنَّ الدِّينَ يُسْرٌ","ولنْ يشادَّ الدِّينُ إلاَّ غَلَبه","فسدِّدُوا وقَارِبُوا وَأَبْشِرُوا","الغنى غنى النفس",
        "أَحَبُّ الأعمالِ إلى اللهِ أدْومُها و إن قَلَّ","تُنْكَحُ المَرْأَةُ لأرْبَعٍ: لِمالِها، ولِحَسَبِها، وجَمالِها، ولِدِينِها، فاظْفَرْ بذاتِ الدِّينِ، تَرِبَتْ يَداكَ","المُسلمُ من سَلِمَ المُسلمونَ من لِسانِه ويَدِه","المهاجرُ من هجر ما نهى اللهُ عنه",
        "كُنْ في الدُّنيا كأنَّك غريبٌ أو كعابرِ سبيلٍ","اتَّقِ دَعوةَ المظلومِ؛ فإنَّهُ ليسَ بينَها وبينَ اللَّهِ حجابٌ","انْصُرْ أخاكَ ظالِمًا أوْ مَظْلُومًا","اعْمَلُوا، فَكُلٌّ مُيَسَّرٌ لِما خُلِقَ له",
        "مَا نَقَصَتْ صَدَقَةٌ مِنْ مَالٍ","وما تواضعَ أحدٌ للَّهِ إلَّا رفعَهُ اللَّهُ","الذي يَعُودُ في هِبَتِهِ كالكَلْبِ يَرْجِعُ في قَيْئِهِ","وابدأْ مَنَ تعولُ",
        "كلُّ معروفٍ صدقةٌ","وَالْكَلِمَةُ الطَّيِّبَةُ صَدَقَةٌ","الدُّنيا حُلوةٌ خضِرةٌ","كلُّكم راعٍ وكلُّكم مسؤولٌ عن رعيتِهِ",
        "اللهمَّ بارِكْ لأُمَّتِي في بُكورِها","إِذَا أَحَبَّ الرَّجُلُ أَخَاهُ، فَلْيُخْبِرْهُ أَنَّهُ يُحِبُّهُ","لا يُلْدَغُ المؤمِنُ من جُحْرٍ مَرَّتيْنِ","تَعِسَ عبْدُ الدِّينَارِ وَالدِّرْهَمِ وَالقَطيفَةِ وَالخَمِيصَةِ، إِنْ أُعْطِيَ رَضِيَ، وَإِنْ لَمْ يُعْطَ لَمْ يَرْضَ",
        "سَاقى القَوْمِ آخِرُهُمْ يعنى: شرْبًا","الناسُ معادِنٌ كمعادِنِ الذهبِ والفضةِ","احرص على ما ينفعك، واستعن بالله، ولا تعجزن","مِنْ حُسْنِ إِسْلَامِ الْمَرْءِ تَرْكُهُ مَا لَا يَعْنِيهِ",
        "جُبِلت القلوبُ على حبِّ من أحسن إليها","التَّائبُ من الذَّنبِ كمن لا ذنبَ له","اتَّقوا النَّار ولو بشِقِّ تمرةٍ فإنْ لم تجِدوا فبكلمةٍ طيِّبةٍ","الدُّنيا سجنُ المؤمنِ وجنَّةُ الْكافرِ",
        "إن اللهَ يُحبُّ الملحِّين في الدعاءِ","لا تَعْجِزُوا في الدعاءِ ، فإنه لن يَهْلِكَ مع الدعاءِ أَحَدٌ","إنَّ الرَّجُلَ ليُحرَمُ الرِّزقَ بالذَّنبِ يُصيبُه، ولا يَرُدُّ القَدَرَ إلَّا الدُّعاءُ، ولا يَزيدُ في العُمُرِ إلَّا البِرُّ","لايغني حذر من قدر. والدعاء بنفع ممانزل ومما لم بنزل، وان البلاء لينزل فيلقاه الدعاء فيعتلجانالى يوم القيامة",
    ]

    
    col1, col2, col3, col4, col5 = st.columns([1,1,2,1,1])
    with col3:
        center_button = st.button('رسالة   اليوم')

    if center_button:
        st.markdown("<hr style='border:4px solid lightgrey'>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: #335575; font-size: 28px;'>{random.choice(QUOTES)}</p>", unsafe_allow_html=True)
        st.markdown("<hr style='border:4px solid lightgrey'>", unsafe_allow_html=True)
    #ٍ Spaces
        st.markdown("<p> </p>", unsafe_allow_html=True)
        st.markdown("<p> </p>", unsafe_allow_html=True)
        st.markdown("<p> </p>", unsafe_allow_html=True)
        
        st.markdown("<p style='text-align: center; font-size: 16px;'><a href='https://twitter.com/RayanArab7' target='_blank'>ريان عرب</a></p>", unsafe_allow_html=True)
        
        button(username="rayan3rab7", floating=False, width=221)

    st.markdown("<p style='text-align: center; color: grey; font-size: 16px;'>:المصادر</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: grey; font-size: 14px;'> كتاب مختصر سيرة الرسول ﷺ للشيخ عبدالله بن محمد بن عبدالوهاب</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: grey; font-size: 14px;'>كتاب الداء والدواء للامام محمد الدمشقي</p>", unsafe_allow_html=True)

    

if __name__ == "__main__":
    main()
