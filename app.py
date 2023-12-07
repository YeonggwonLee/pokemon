import streamlit as st

st.title("포켓몬 도감")

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}
    
    
initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp",
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
]

example_pokemon = {
    "name": "알로라 디그다",
    "types": ["땅", "강철"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/alora_digda.webp"
}

# st.session_state로 페이지 리로딩시 데이터값 그대로 저장하기 처음에는이니셜 포켓몬으로 저장 
if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons
    
auto_complete = st.toggle("예시 데이터로 채우기")

#폼/예시 데이터 채우기
with st.form("form",clear_on_submit=True):
    col1,col2 = st.columns(2)
    with col1:
        name = st.text_input(label="포켓몬 이름",
                             value=example_pokemon["name"] if auto_complete else "")
    with col2:
        types = st.multiselect(
            label="포켓몬 속성",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_pokemon["types"] if auto_complete else []
        )
    image_url = st.text_input(label="포켓몬 이미지",
                              value=example_pokemon["image_url"] if auto_complete else "")
    submit = st.form_submit_button("제출")
    
    
#예외 처리
    if submit:
        if not name:
            st.error("포켓몬의 이름을 입력해주세요!")
        elif not types:
            st.error("포켓몬의 타입을 입력해주세요!")
        elif not image_url:
            st.error("포켓몬의 이미지 url을 입력해주세요!")
        else:
            st.session_state.pokemons.append({
                "name":name,
                "types":types,
                "image_url":image_url
            })

    


#포켓몬 도감 보여주기

for i in range(0,len(st.session_state.pokemons),3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        pokemon = row_pokemons[j] 
        with cols[j]:
            with st.expander(
                label=f"**{i+j+1}.{pokemon['name']}**",expanded=True):
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text("/".join(emoji_types))
                delete_button = st.button("삭제",key=(i+j),use_container_width=True)
                if delete_button:
                    del st.session_state.pokemons[i+j]
                    st.rerun()
