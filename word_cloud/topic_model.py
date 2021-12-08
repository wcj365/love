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
    SOURCE = "../src/classic_poems/qi_jue"
    files = os.listdir(SOURCE)
    doc_list = []
    for file in files:
        if not file.endswith(".md"):    
            continue 

        with open(f"{SOURCE}/{file}", "r") as f_read:
            lines = f_read.readlines()
        strinfo = re.compile('[0-9a-zA-Z()【】，。,;#-_"!><?]')
        content = strinfo.sub('', " ".join(lines))

        sstop_path = open("stopwords.txt", 'r',encoding='UTF-8')
        stop = stop_path.readlines()
        stop = [x.replace('\n', '') for x in stop]
        word = list(set(content) - set(stop))
        result = result[result['word'].isin(word)]
        word_list = jieba.lcut(content,cut_all=True)   # 结巴词库切分词 精准模式
        doc_list.append(word_list)
    return doc_list

def main():

    doc_list = usecase_1()
    lda_model, viz, _, _, _ = topic_model(doc_list, 5)
    pyLDAvis.save_html(viz, "lda.html")


if __name__ == "__main__":
    main()

