import streamlit as st

import openai

openai.api_key = "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"
def getresponse (prom):
    response  = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": prom},
            
        ]
    )
    return(response.choices[0].message.content.strip())



st.set_page_config(
    page_title="Ghorsi Matcher",
    layout="wide",
    
)


st.title ("Ghorsi Matcher")


col1, col2, col3 = st.columns([5,1,5])

with col1:
    st.subheader("set up your requirements")
    nat = st.text_input("his nationality must be?" ,key = 2 , value= " not important")
    minage = st.slider("minimum acceptable age", step=1, key  =5)
    maxage = st.slider("maximum acceptable age", step=1, key = 6)

    height = st.number_input("height around" ,max_value=200 , step= 1 , min_value= 170 , value= 170 ,key = 3)
    levels =  ["1- athiest" , "2- new revert" , "3- prays, fasts and reads Quran" , "4- level 3 + joins islamic seminars ",
                                            "5- Niaqb level" ,"6- super extrimest" ]
    relig = st.selectbox("how religous" ,levels ,key = 4)
    acad = st.multiselect("academical background ?" , ["IT related" , "Medicine" , "Engenieering" , "Not importnat" , "other"])

    residnce = st.selectbox("place of residence ?" , ["Turkey" , "UK" , "Arabian Gulf" , "Germany" , "France" , "Not important" , "any arabic contry" , "NOT Europe" , "USA"])

    

with col3:
    st.subheader("Enter the candidate Info")
    nat2 = st.text_input("his nationality is?" ,key = 12)
    age2 = st.slider("his age", step=1, key  =15)

    height2 = st.number_input("his height" ,max_value=200 , step= 1 , min_value= 170 , value= 170 ,key = 13)
    relig2 = st.selectbox("how religous is he?" , ["1- athiest" , "2- new revert" , "3- prays, fasts and reads Quran" , "4- level 3 + joins islamic seminars ",
                                            "5- Niaqb level" ,"6- super extrimest" , "7- i dont know" ] ,key = 14)
    acad2 = st.multiselect("his academical background ?" , ["IT related" , "Medicine" , "Engenieering" , "Not importnat" , "other"])

    residnce2 = st.selectbox("he lives in ?" , ["Turkey" , "UK" , "Arabian Gulf" , "Germany" , "France" , " an arabic contry" , "NOT Europe" , "USA"])
    extra = st.text_area("Any extra notes?" , height= 150)
    love = st.select_slider("how much do you love him? 5 the highest" , [1,2,3,4,5] )


p = f'''
my name is Shahd and i am looking to settle down and get married. 
my reqiremnts are as follows: to me, his natinlity should be {nat} and his height at least be
around {height}, his age can be between { minage} and {maxage}. i am expecting him
to be living in {residnce} and since religuos is an important topic to me, i am expecting
his level to be {relig} in accordance with the list of available options given as {levels}
and finally the academic background is : {acad} or somthing similar.

based on the criterias i gave to you, i want you to tell me in percentage how
good is the following guy to me. along with a detaield exaplination on how you decided this.
here is his info :
the guy is {nat2} and his heights is {height2}. he is {age2} years old and his academical background
is {acad2}. he lives in {residnce2}. on the religion scale he is {relig2}.
in terms of love, i can say i love him {love*20} percent. and here are some extra notes about him : {extra}.


the output is expected to be like this: 
match: XX%
explinaton : Hi Shahed, based on ... etc
recomendation: 

    
            '''
with col3:
    but = st.button("MATCH ME")
if but:
    st.text_area(label = 'report' , value = getresponse(p) , height=500)
