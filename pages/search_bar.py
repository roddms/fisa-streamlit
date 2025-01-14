import streamlit as st


# 1. text 입력 검색창
# 2. list에 있는 글자가 일부라도 들어가면
# img_list에 있는 해당 그림 출력되는 검색창

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

input_ = st.text_input("검색하실 애니메이션을 입력하세요")

if input_ == ani_list[0] :
    st.image("https://i.imgur.com/t2ewhfH.png")

elif input_ == ani_list[1] :
    st.image("https://i.imgur.com/ECROFMC.png", width= 200)

else:
    st.image("https://i.imgur.com/MDKQoDc.jpg", width= 200)


input2 = st.selectbox("Pick one", ["짱구는못말려", "몬스터", "릭앤모티"])

if input2 == ani_list[0] :
    st.image("https://i.imgur.com/t2ewhfH.png")

elif input2 == ani_list[1] :
    st.image("https://i.imgur.com/ECROFMC.png", width= 200)

else:
    st.image("https://i.imgur.com/MDKQoDc.jpg", width= 200)


# for ani in ani_list:
#     if input_ in ani :
#         img_idx = ani_list.index(input_)

# st.image(img_list[img_idx])

# if input_ != '' : # 초기 상태를 이미지 없이 실행
#     st.image(img_list[img_idx])
