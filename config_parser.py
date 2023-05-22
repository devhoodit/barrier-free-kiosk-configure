from __future__ import annotations
from typing import List
from dataclasses import dataclass
import json
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Okt

DEFAULT_STOP_WORDS = "을 를 이 가 에 에서"

def parse_config(path):
    with open(path, "r", encoding="utf-8") as f:
            menu_data: dict = json.load(f)

    config_menu = menu_data["items"]
    menus = []
    for menu in config_menu:
        menus.append(Menu(menu["name"], menu["price"], menu["description"], menu["image"]))
    return Dispenser(menus)

def pre_process(corpus: List[str]):
    okt = Okt()
    edited = []
    for cor in corpus:
        edited.append(" ".join(okt.morphs(cor)))
    return edited

def get_tfidf_vector(corpus: List[str], stopwords: str=DEFAULT_STOP_WORDS):
    vec = TfidfVectorizer(stop_words=stopwords.split(" "))
    vec.fit(corpus)
    return vec


@dataclass
class Menu:
    name: str
    price: str
    description: str
    image_path: str

class Dispenser:
    def __init__(self, menus: List[Menu]) -> None:
        self.menus = menus
        corpus = [menu.name + " " + menu.description for menu in self.menus]
        corpus = pre_process(corpus)
        self.vec = get_tfidf_vector(corpus)
        self.tfidf_vector = self.vec.transform(corpus)

    def get_rank(self, sentence):
        corpus = pre_process([sentence])
        counter_vec = self.vec.transform(corpus)
        cosine_sim_metrix = cosine_similarity(self.tfidf_vector, counter_vec)
        rank = [(i, cosine_sim_metrix[i][0]) for i in range(len(cosine_sim_metrix))]
        rank = sorted(rank, key=lambda x: x[1], reverse=True)
        return rank