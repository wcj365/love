#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://zhuanlan.zhihu.com/p/347738635
# https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/
# https://datascienceplus.com/evaluation-of-topic-modeling-topic-coherence/

import os
import re
#import matplotlib.pyplot as plt
#import pandas as pd
import gensim
from gensim import corpora, models
import pyLDAvis
import pyLDAvis.gensim_models 
import jieba



def topic_model(doc_list, num_topics):

    dictionary = corpora.Dictionary(doc_list)
    bow_corpus = [dictionary.doc2bow(doc) for doc in doc_list]

    # LDA using Bag of Words (BoW)
    lda_model = models.LdaMulticore(
        corpus=bow_corpus, 
        num_topics=num_topics, 
        id2word=dictionary, 
        passes=10, 
        workers=2,
        random_state=100
    )

    # Creating Topic Distance Visualization.
    viz = pyLDAvis.gensim_models.prepare(
        lda_model, 
        corpus=bow_corpus, 
        dictionary=dictionary
    )
    
    # Compute Coherence Score
    coherence_model = models.CoherenceModel(
            model=lda_model, 
            texts=doc_list,
            dictionary=dictionary, 
            coherence='c_v')
    c_v = coherence_model.get_coherence()

    # Compute Coherence Score
    coherence_model = models.CoherenceModel(
            model=lda_model, 
            texts=doc_list,
            dictionary=dictionary, 
            coherence='u_mass')

    u_mass = coherence_model.get_coherence()

    # Compute Perplexity - a measure of how good the model is. lower the better.
    perplexity = lda_model.log_perplexity(bow_corpus)

    return lda_model, viz, c_v, u_mass, perplexity



def optimal_topics(doc_list):

    x = list(range(25,36,1))
    #x = list(range(5,50,5))
    y = []
    z = []
    u = []
    for i in x:
        lda_model, viz, c_v, u_mass, perplexity = topic_model(doc_list, i)
        y.append(c_v)
        z.append(u_mass)
        u.append(perplexity)
        print(f"# Topics: {i} - Perplexity: {perplexity} - c_v: {c_v} - u_mass: {u_mass}") 

    return [x,y,z,u]


def plot_metrics(metrics):

    fig, axs = plt.subplots(2, figsize=(8,4), sharex=True) 
    axs[0].plot(metrics[0],metrics[1])
    axs[1].plot(metrics[0], metrics[2])
    fig.savefig("../images/optimal_topics2.png")


def exp8_optimal():

    df_good, _ = prepare_data("../data/exp8_params.csv")
    metrics = optimal_topics(df_good["document"])
    plot_metrics(metrics)

def usecase_1():
    SOURCE = "../src/classic_poems"
    poems = ["wu_jue", "qi_jue", "wu_lv", "qi_lv"]
    doc_list = []
    for poem in poems:
        files = os.listdir(SOURCE + "/" + poem)

        for file in files:
            if file.startswith("README") or not file.endswith(".md"):    
                continue 

            with open(f"{SOURCE}/{poem}/{file}", "r") as f_read:
                lines = f_read.readlines()
    #       strinfo = re.compile('[0-9a-zA-Z()【】，。,;#-_"!><?]')
    #       content = strinfo.sub('', " ".join(lines))
            content_list = []
            for line in lines:
                if line.startswith("注") or line.startswith("附"):
                    break
                if line.startswith("#") or line.startswith("!"):
                    continue
                else:
                    content_list.append(line)

            content = " ".join(content_list)

            stop_path = open("cn_stopwords.txt", 'r',encoding='UTF-8')
            stop = stop_path.readlines()
            stop = [x.replace('\n', '') for x in stop]
            my_stop = ["【", "】", "-", "_", ">","<", "（", "）", "。","，",",","’","?", "!", ";","\n"]
            
            for stop_word in my_stop:
                content.replace(stop_word, "")

            word_list = jieba.lcut(content,cut_all=False)   # 结巴词库切分词 精准模式
            new_list = []
            for word in word_list:
                if len(word.strip()) == 0 or word in my_stop + stop:
                    continue
                else:
                    new_list.append(word)
            print(new_list)
            print("\n\n")
            doc_list.append(new_list)

    return doc_list

def main():

    doc_list = usecase_1()
    lda_model, viz, _, _, _ = topic_model(doc_list, 4)
    pyLDAvis.save_html(viz, "lda.html")


if __name__ == "__main__":
    main()

